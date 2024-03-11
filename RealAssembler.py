


register = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100", "t0": "00101", "t1": "00110",
    "t2": "00111", "s0": "01000", "fp": "01000", "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100",
    "a3": "01101", "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010", "s3": "10011",
    "s4": "10100", "s5": "10101", "s6": "10110", "s7": "10111", "s8": "11000", "s9": "11001", "s10": "11010",
    "s11": "11011", "t3": "11100", "t4": "11101", "t5": "11110", "t6": "11111"
}
# defining program counter and Saved register/frame pointer in global
PC=0
s0=fp="00000000000000000000000000000000"


# defining memory(32 bit) in a dictionary
memory={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
        "11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,
        "19":19,"20":20,"21":21,"22":22,"23":23,"24":24,"25":25,"26":26,
        "27":27,"28":28,"29":29,"30":30,"31":31}

labels={}#making empty dictionary for labels (Branching)
#num is a string actually
def Binary_to_Decimal(num, num_type='signed'):
    if num_type == 'signed':
        if num[0] == 1:
            temp = 0
            temp = temp + (-2)*(len(num)-1)
            for i in range(1, len(num)):
                temp = temp + int(num[i])(2*(len(num)-i-1))
            return temp
        else:
            temp = 0
            for i in range(0, len(num)):
                temp = temp + int(num[i])(2*(len(num)-i-1))
            return temp
    if num_type=="unsigned":
        temp = 0
        for i in range(0, len(num)):
            temp = temp + int(num[i])(2*(len(num)-i-1))
        return temp

def SignExtend(digit, num):
    return digit*(32-len(bin(num)[2:])) + bin(num)[2:]


def Decimal_to_Binary(num, num_type='signed'):
    if num_type == 'signed':
        if num < 0:
            number = '0' + bin(abs(num))[2:]
            new = ''
            for i in number:
                if i == '0':
                    new = new + '1'
                else:
                    new = new + '0'
            ocomplement = int(new, 2)
            tcomplement = ocomplement + 1
            return SignExtend('1', tcomplement)
        if num > 0:
            tcomplement = num
            return SignExtend('0', tcomplement)
    if num_type == 'unsigned':
        nums = num
        return SignExtend('0', nums)
    





def Execution(line):
    global PC
    global output
    # Write the assembly instruction to the output file
    output.write(f"{line.strip()}\n")

    # Execute the instruction
    if line.strip() == 'virtual halt':
        PC = 'virtual halt'
        return
    try:
        # Execute the instruction based on the first part of the line
        firstpart = line.split()[0]
        if firstpart == 'add':
            Addition_R(line)
        elif firstpart == 'addi':
            Addition_I(line)
        elif firstpart == 'jal':
            jal(line)
        elif firstpart =='sub':
            Subtraction(line)
        elif firstpart == 'sll':
            Shift_Left(line)
        elif firstpart == 'srl':
            Shift_Right(line)
        elif firstpart == 'or':
            OR_Gate(line)
        elif firstpart == 'and':
            AND_Gate(line)
        elif firstpart == 'beq':
            Branch_Eq(line)
        elif firstpart == 'bne':
            Branch_Neq(line)
        elif firstpart =='bge':
            Branch_GreaterEq(line)
        elif firstpart == 'bgeu':
            Branch_GreaterEq_Unsigned(line)
        elif firstpart == 'blt':
            Branch_Less(line)
        elif firstpart == 'bltu':
            Branch_Less_Unsigned(line)
        elif firstpart == 'lw':
            lw(line)
        elif firstpart == 'auipc':
            auipc(line)
        elif firstpart == 'sw':
            sw(line)
        elif firstpart =='lui':
            lui(line)
        elif firstpart == 'and':
            AND_Gate(line)
    except Exception as e:
        print("An error occurred:", e)
        return        
            
def Addition_R(line):
    global PC
    global output
    # taking 2 part of the line(next to blank spaces containing registers and other stuff) as 1 part is for instruction
    # we are breaking as  add reg1, reg2, reg3 when we split line we get ["add","reg1,reg2,reg3"]
    # by taking [1] we are taking "reg1,reg2,reg3"
    secondpart=line.split()[1]
    # second_part.split(",") makes string a list like [reg1,reg2,reg3]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register: 
         '''register[lis[0]] = Binary_to_Decimal(register[lis[1]]) + Binary_to_Decimal(register(lis[2]))
         Decimal_to_Binary(register[lis[0]])'''
         rd = lis[0]
         rs1 = lis[1]
         rs2 = lis[2]
         rd_binary = register[rd]
         rs1_binary = register[rs1]
         rs2_binary = register[rs2]
         rd_binary = rd_binary.zfill(5)
         rs1_binary = rs1_binary.zfill(5)
         rs2_binary = rs2_binary.zfill(5)
         binary_instruction = f'0000000{register[lis[2]]:05b}{register[lis[1]]:05b}000{register[lis[0]]:05b}0010011\n'
         output.write(binary_instruction)
         PC=PC+1
    

    return

def Addition_I(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        PC=PC+1
        binary_instruction = f'{int(lis[2]):012b}{register[lis[1]]:05b}{register[lis[0]]:05b}0010011\n'
        output.write(binary_instruction)

    return


def jal(line):
    global PC
    global output
    secondpart = line.split()[1]
    lis = secondpart.split(',')
    if lis[0] in register:
        register[lis[0]] = PC*4 + 4
        immediate = Decimal_to_Binary(int(lis[1]))[20:]
        output.write(immediate[0]+immediate[10:]+immediate[9]+immediate[1:9]+register[lis[0]]+'1101111')
    return
# bhai ye subtraction me issue hai signd lena ha unsigned liya h tune
def Subtraction(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]]) - Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])'''
        PC=PC+1
        outputF = f"0100000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}000{register[lis[0]].zfill(5)}0110011"
        output.write(outputF + '\n')


    return

def xor(line):
    global PC
    global output
    secondpart = line.split()[1]
    lis = secondpart.split(',')
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]]) ^ Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])'''
        PC = PC + 1
        outputF = f"0000000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}100{register[lis[0]].zfill(5)}0110011"
        output.write(outputF + '\n')

def Shift_Left(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]],"unsigned") << Binary_to_Decimal(register(lis[2]),"unsigned")
        Decimal_to_Binary(register[lis[0]],"unsigned")'''
        PC=PC+1
        outputF = f"0000000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}001{register[lis[0]].zfill(5)}0110011"
        output.write(outputF + '\n')


    return

def Shift_Right(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]],"unsigned") >> Binary_to_Decimal(register(lis[2]),"unsigned")
        Decimal_to_Binary(register[lis[0]],"unsigned")'''
        PC=PC+1
        outputF = f"0000000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}101{register[lis[0]].zfill(5)}0110011"
        output.write(outputF + '\n')

    return

def OR_Gate(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]])|Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])'''
        PC=PC+1
        outputF = f"0000000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}110{register[lis[0]].zfill(5)}0110011"
        output.write(outputF + '\n')

    return

def AND_Gate(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        '''register[lis[0]] = Binary_to_Decimal(register[lis[1]])&Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])'''
        PC=PC+1
        outputF = f"0000000{register[lis[2]].zfill(5)}{register[lis[1]].zfill(5)}110{register[lis[0]].zfill(5)}0110011\n"
        output.write(outputF + '\n')

    return


def Branch_Eq(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])==Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '000' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '000' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
     return 

def Branch_Neq(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])!=Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '001' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '001' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)

     return 

def Branch_GreaterEq(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])>=Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '101' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '101' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)

     return

def Branch_GreaterEq_Unsigned(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]], 'unsigned')>=Binary_to_Decimal(register[lis[1]], 'unsigned'):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '111' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '111' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)


     return

def Branch_Less(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])<Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '100' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)

         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '100' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)

def Branch_Less_Unsigned(line):
     global PC
     global output
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]],"unsigned")<Binary_to_Decimal(register[lis[1]],"unsigned"):
             PC=PC+int(lis[2])//4
             Formatingimm= format(int(lis[2]), '012b') 
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '110' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
         else:
             PC = PC + 1
             Formatingimm = format(int(lis[2]), '012b')
             outputF = Formatingimm[0] + Formatingimm[2:8] + register[lis[1]].zfill(5) + register[lis[0]].zfill(5) + '00110' +  Formatingimm[8:] + Formatingimm[1] + " 1100011\n"
             output.write(outputF)
             return



def lw(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        '''lis[0]=memory[str((int(lis[1]) + Binary_to_Decimal(lis[2]) - 65536)//4)]'''
        PC = PC + 1
        output.write(f'{lis[1]}{lis[2]}010{lis[0]}0000011\n')



def sltiu(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        '''if Binary_to_Decimal(lis[1],"unsigned")<int(lis[2]):
            lis[0]=1'''
        PC=PC+1



def sw(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register:
         memory[(str(int(lis[2]) + Binary_to_Decimal(lis[1]) - 65536)//4)-1] = register[lis[0]]
         PC=PC+1
         output.write(f'{lis[1]}{lis[2]}')



def jalr(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        '''register[lis[0]]= Decimal_to_Binary(PC+1)'''
        PC = (PC + int(lis[2])//4)&~1


        return
    


def lui(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register :
        ''' register[lis[0]]=int(lis[1])<<12
        Decimal_to_Binary(lis[0])'''
        PC=PC+1


        return
    

def auipc(line):
    global PC
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register :
         '''register[lis[0]]=(int(lis[1])<<12)//4 +PC
         Decimal_to_Binary(lis[0])'''
         PC=PC+1



def main():
    global PC
    global output
    with open('text.txt', 'r') as f:
        lines = f.readlines()

    # Extracting labels and storing their positions
    for i, line in enumerate(lines):
        if ':' in line:
            label_name = line.split(':')[0].strip()
            labels[label_name] = i

    # Processing each line of assembly code
    with open("output.txt", "w+") as output:
        for line in lines:
            if ':' not in line:
                Execution(line.strip())
                # Log PC and the executed line for debugging
                #output.write(f"PC: {PC} Executed: {line.strip()}\n")

if __name__ == "__main__":
    main()