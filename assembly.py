registers = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100", "t0": "00101", "t1": "00110",
    "t2": "00111", "s0": "01000", "fp": "01000", "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100",
    "a3": "01101", "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010", "s3": "10011",
    "s4": "10100", "s5": "10101", "s6": "10110", "s7": "10111", "s8": "11000", "s9": "11001", "s10": "11010",
    "s11": "11011", "t3": "11100", "t4": "11101", "t5": "11110", "t6": "11111"
}

errorList = []

R_type = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
I_type = ["lw", "addi", "sltiu", "jalr"]
S_type = ["sw"]
B_type = ["beq", "bne", "blt", "bge", "bltu", "bgeu"]
U_type = ["lui", "auipc"]
J_type = ["jal"]

opcode = {
    "add": "0110011", "sub": "0110011", "sll": "0110011", "slt": "0110011", "sltu": "0110011", "xor": "0110011",
    "srl": "0110011", "or": "0110011", "and": "0110011", "lw": "0000011", "addi": "0010011", "sltiu": "0010011",
    "jalr": "1100111", "sw": "0100011", "beq": "1100011", "bne": "1100011", "blt": "1100011", "bge": "1100011",
    "bltu": "1100011", "bgeu": "1100011", "lui": "0110111", "auipc": "0010111", "jal": "1101111"
}

funct3 = {
    "add": "000", "sub": "000", "sll": "001", "slt": "010", "sltu": "011", "xor": "100", "srl": "101", "or": "110",
    "and": "111", "lw": "010", "addi": "000", "sltiu": "011", "jalr": "000", "sw": "010", "beq": "000", "bne": "001",
    "blt": "100", "bge": "101", "bltu": "110", "bgeu": "111"
}

funct7 = {
    "add": "0000000", "sub": "0100000", "sll": "0000000", "slt": "0000000", "sltu": "0000000", "xor": "0000000",
    "srl": "0000000", "or": "0000000", "and": "0000000"
}










def errorDetection(line, TOTAL_lines, count, errorlist):
    list = re.findall(r'\w+', line)
    instruction = list[0]
    if len(list) == 4:
        if instruction in {"add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"}:
            rd = list[1]
            rs1 = list[2]
            rs2 = list[3]
            if all(r in registers for r in (rd, rs1, rs2)):
                return 1
            else:
                errorlist.append("Invalid register at line no" + str(count))
        elif instruction in {"lw", "sw"}:
            rd = list[1]
            imm = list[2]
            rs1 = list[3]
            if ((all(r in registers for r in (rd, rs1))) and int(imm) >= -2048 and int(imm) <= 2047):
                return 1
            elif (int(imm) < -2048 and int(imm) > 2047):
                errorlist.append("Immediate number not in the range at line no" + str(count))
            else:
                errorlist.append("Invalid register at line no" + str(count))
        elif instruction in {"addi", "sltiu", "jalr"}:
            rd = list[1]
            rs = list[2]
            imm = list[3]
            if ((all(r in registers for r in (rd, rs))) and int(imm) >= -2048 and int(imm) <= 2047):
                return 1
            elif (int(imm) < -2048 and int(imm) > 2047):
                errorlist.append("Immediate number not in the range at line no" + str(count))
            else:
                errorlist.append("Invalid register at line no" + str(count))
        elif instruction in {"beq", "bne", "bge", "bgeu", "blt", "bltu"}:
            rs1 = list[1]
            rs2 = list[2]
            imm = list[3]
            if all(r in registers for r in (rs1, rs2)):
                try:
                    imm_int = int(imm)
                    if -2048 <= imm_int <= 2047:
                        return 1
                    else:
                        errorlist.append("Immediate number not in the range at line no " + str(count))
                except ValueError:
                    errorlist.append("Invalid immediate value at line no " + str(count))
            else:
                errorlist.append("Invalid register at line no " + str(count))
        else:
            errorlist.append("Typo in instruction name on line NO " + str(count))
            return 0
    if len(list) == 3:
        if instruction in {"auipc", "lui", "jal"}:
            rd = list[1]
            imm = list[2]
            if rd in registers:
                try:
                    imm_int = int(imm)
                    if -1048576 <= imm_int <= 1048575:
                        return 1
                    else:
                        errorlist.append("Immediate number not in the range at line no " + str(count))
                except ValueError:
                    errorlist.append("Invalid immediate value at line no " + str(count))
            else:
                errorlist.append("Invalid register at line no " + str(count))
        else:
            errorlist.append("Typo in instruction name on line NO " + str(count))
            return 0
    if len(list) == 4:
        if count == TOTAL_lines and list[0] == "beq" and list[1] == "zero" and list[2] == "zero" and list[3] == "0":
            return 1
        else:
            errorlist.append("hlt is not present at last ,present at line NO " + str(count))
            return 0