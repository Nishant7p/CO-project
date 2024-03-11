import re

registers = {'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100', 't0': '00101', 't1': '00110', 't2': '00111',
             's0': '01000', 'fp': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 
             'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011', 's4': '10100', 
             's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011', 
             't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111'
}
register={"zero":'00000000000000000000000000000000',"ra":"00000000000000000000000000000000","sp":"00000000000000000000000000000000","gp":"00000000000000000000000000000000","tp":"00000000000000000000000000000000","t0":"00000000000000000000000000000000","t1":"00000000000000000000000000000000","t1":"00000000000000000000000000000000","t2":"00000000000000000000000000000000",
          "s1":"00000000000000000000000000000000","a0":"00000000000000000000000000000000","a1":"00000000000000000000000000000000","a2":"00000000000000000000000000000000","a3":"00000000000000000000000000000000","a4":"00000000000000000000000000000000","a5":"00000000000000000000000000000000","a6":"00000000000000000000000000000000","a7":"00000000000000000000000000000000","s2":"00000000000000000000000000000000",
          "s3":"00000000000000000000000000000000","s4":"00000000000000000000000000000000","s5":"00000000000000000000000000000000","s6":"00000000000000000000000000000000","s7":"00000000000000000000000000000000","s8":"00000000000000000000000000000000","s9":"00000000000000000000000000000000","s10":"00000000000000000000000000000000","s11":"00000000000000000000000000000000",
          "t3":"00000000000000000000000000000000","t4":"00000000000000000000000000000000","t5":"00000000000000000000000000000000","t6":"00000000000000000000000000000000"}




output = open('output.txt', 'w+')

labels = {}

def Binary_to_Decimal(num, num_type='unsigned'):
    if num_type == 'signed':
        if num[0] == '1':
            sum = 0
            sum = sum + (-2)**(len(num)-1)
            for i in range(1, len(num)):
                sum = sum + int(num[i])(2*(len(num)-i-1))
            return sum
        if num[0] == '0':
            sum = 0
            for i in range(1, len(num)):
                sum = sum + int(num[i])(2*(len(num)-i-1))
            return sum
    else:
        sum = 0
        for i in range(0, len(num)):
            sum = sum + int(num[i])(2*(len(num)-i-1))
            return sum
        
def Sign_extend(num1, num, size=32):
    if len(bin(num)[2:]) > size:
        raise OverflowError('Error: Illegal immediate overflow')
    return num1*(size-len(bin(num)[2:])) + bin(num)[2:]

def decimaltobinary(num, num_type='unsigned', size=32):
    if num_type == 'signed':
        if num < 0:
            number = '0' + bin(abs(num))[2:]
            new = ''
            for i in number:
                if i == '0':
                    new = new + '1'
                else:
                    new = new + '0'
            onescomplement = int(new, 2)
            twoscomplement = onescomplement + 1
            return Sign_extend('1', twoscomplement, size)
        if num >= 0:
            twoscomplement = num
            return Sign_extend('0', twoscomplement, size)
    if num_type == 'unsigned':
        nums = num
        return Sign_extend('0', nums, size)
    
def contains_integers(input_string):
    pattern = r'^[+-]?\d+$'
    return bool(re.match(pattern, input_string))

class assembler:
    def remove_special_characters(self, lines):
        self.new_lines = []
        for i in lines:
            j = re.sub(r'\n', '', i)
            k = re.sub(r'//.*', '', j)
            l = re.sub(r'\w+:', '', k)
            self.new_lines.append(l.strip())       
            if re.match(r'\b\w+:', k):
                labels[re.search(r'\b\w+:', k).group()] = lines.index(i)
        self.new_line = list(filter(lambda x: x != '', self.new_lines))
        return self.new_line
                
    def display(self):
        print(self.new_line)
        print(labels)
        
    def execution(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if line == 'beq zero,zero,0':
            globals()['pc'] = len(globals()['new_lines'])*4
            imm = decimaltobinary(0, 'signed')
            output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
            return
        elif line.split()[0] == 'jal':
            self.jal(line)
        elif line.split()[0] == 'addi':
            self.addi(line)
        elif line.split()[0] == 'add':
            self.add(line)
        elif line.split()[0] =='sub':
            self.sub(line)
        elif line.split()[0] == 'slt':
            self.slt(line)
        elif line.split()[0] == 'sltu':
            self.sltu(line)
        elif line.split()[0] == 'sll':
            self.sll(line)
        elif line.split()[0] == 'srl':
            self.srl(line)
        elif line.split()[0] == 'or':
            self.OR(line)
        elif line.split()[0] == 'and':
            self.AND(line)
        elif line.split()[0] == 'xor':
            self.xor(line)
        elif line.split()[0] == 'lw':
            self.lw(line)
        elif line.split()[0] == 'sltiu':
            self.sltiu(line)
        elif line.split()[0] == 'jalr':
            self.jalr(line)
        elif line.split()[0] == 'sw':
            self.sw(line)
        elif line.split()[0] == 'beq':
            self.beq(line)
        elif line.split()[0] == 'bne':
            self.bne(line)
        elif line.split()[0] == 'bge':
            self.bge(line)
        elif line.split()[0] == 'bgeu':
            self.bgeu(line)
        elif line.split()[0] == 'blt':
            self.blt(line)
        elif line.split()[0] == 'bltu':
            self.bltu(line)
        elif line.split()[0] == 'auipc':
            self.auipc(line)
        elif line.split()[0] == 'lui':
            self.lui(line)
        elif line.split()[0] == 'jal':
            self.jal(line)
        else:
            print('Error: Invalid instruction')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        
    def add(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'000'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
            
    def sub(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            output.write('0100000'+registers[lis[2]]+registers[lis[1]]+'000'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
    
    def slt(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'010'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
    
    def sltu(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'011'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
            
    def xor(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'100'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
        
    def sll(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'001'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
    
    def srl(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'101'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
    
    def OR(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'110'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
            
    def AND(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register or lis[2] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and lis[1] in register and lis[2] in register:
            output.write('0000000'+registers[lis[2]]+registers[lis[1]]+'111'+registers[lis[0]]+'0110011\n')
            globals()['pc'] += 4
            
    def addi(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            try:
                imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed', 12)
                output.write(decimaltobinary(int(line.split()[1].split(',')[2]), 'signed', 12)+registers[lis[1]]+'000'+registers[lis[0]]+'0010011\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Invalid immediate length')
                globals()['pc'] = len(globals()['new_lines'])
                return
            
    def lw(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        src_reg = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][1]
        imm = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][0]
        if lis[0] not in register or src_reg not in globals():
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(imm):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and src_reg in globals():
            try:
                immediate = decimaltobinary(int(imm), 'signed', 12)
                output.write(immediate+registers[src_reg]+'010'+registers[lis[0]]+'0000011\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])
                return
    
    def sltiu(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            try:
                immediate = decimaltobinary(int(line.split()[1].split(',')[2]), 'unsigned', 12)
                output.write(immediate+registers[lis[1]]+'011'+registers[lis[0]]+'0010011\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])*4
                return
    
    def jalr(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            try:
                immediate = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed', 12)
                output.write(immediate+registers[lis[1]]+'000'+registers[lis[0]]+'1100111\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])*4
                return
    
    def sw(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        src_reg = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][1]
        imm = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][0]
        if src_reg not in globals() or lis[0] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(imm):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return            
        if lis[0] in register and src_reg in globals():
            try:
                immediate = decimaltobinary(int(imm), 'signed', 12)
                output.write(immediate[:7]+registers[lis[0]]+registers[src_reg]+'010'+immediate[7:]+'0100011\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])*4
                return
    
    def beq(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split()[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            if line.split()[1].split(',')[2]+':' not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) == Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') == Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4),'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
    
    def bne(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split(',')[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:             #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if line.split()[1].split(',')[2]+':' not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) != Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed', 12)
    
                        output.write(imm[0]+imm[2:8]+registers[lis[1]]+registers[lis[0]]+'001'+imm[8:]+imm[1]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed', 12)
                    
                    output.write(imm[0]+imm[2:8]+registers[lis[1]]+registers[lis[0]]+'001'+imm[8:]+imm[1]+'1100011\n')
                    globals()['pc'] += 4
                    
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') != Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'001'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'001'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
    
    def bge(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register and lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split()[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            if line.split()[1].split(',')[2]+':' not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') >= Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')                    
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') >= Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4),'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                        
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'101'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
                
    def bgeu(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split()[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return 
        if lis[0] in register and line.split()[1].lis[1] in register:
            if line.split()[1].split(',')[2] not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) >= Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                        
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) >= Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
            
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
    
    def blt(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split()[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            if line.split()[1].split(',')[2] not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') < Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]], 'signed') < Binary_to_Decimal(globals()[line.split()[1].split(',')[1]], 'signed'):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return

                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4),'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')                    
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
    
    def bltu(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register or lis[1] not in register:
            print('Error: No such register or invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if line.split()[1].split(',')[2]+':' not in globals()['labels'] and not contains_integers(line.split()[1].split(',')[2]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register and line.split()[1].lis[1] in register:
            if line.split()[1].split(',')[2]+':' not in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) < Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                        
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                        
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(int(line.split()[1].split(',')[2]), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[2]+':' in globals()['labels']:
                if Binary_to_Decimal(globals()[line.split()[1].split(',')[0]]) < Binary_to_Decimal(globals()[line.split()[1].split(',')[1]]):
                    try:
                        imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()[pc]+4),'signed')
                        output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                        globals()['pc'] += 4
                        return
                    except OverflowError:
                        print('Error: Illegal immediate length')
                        globals()['pc'] = len(globals()['new_lines'])*4
                        return
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[2]+':']*4-(globals()['pc']+4),'signed')
                    
                    output.write(imm[19]+imm[21:27]+registers[lis[1]]+registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['pc'] += 4
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
    
    def auipc(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(line.split()[1].split(',')[1]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register:
            imm = int(line.split()[1].split(',')[1])
            try:
                immediate = decimaltobinary(imm, 'signed')
                
                output.write(immediate[:20]+registers[lis[0]]+'0010111\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])*4
                return
    
    def lui(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(line.split()[1].split(',')[1]):
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register:
            imm = int(line.split()[1].split(',')[1])
            try:
                immediate = decimaltobinary(imm, 'signed')
                output.write(immediate[0:20]+registers[lis[0]]+'0110111\n')
                globals()['pc'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                globals()['pc'] = len(globals()['new_lines'])*4
                return
    
    def jal(self, line):
        secondpart=line.split()[1]
        lis=secondpart.split(",")
        if lis[0] not in register:
            print('Error: No such register')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if not contains_integers(line.split()[1].split(',')[1]) and line.split()[1].split(',')[1]+':' not in globals()['labels']:
            print('Error: Invalid immediate')
            globals()['pc'] = len(globals()['new_lines'])*4
            return
        if lis[0] in register:
            if line.split()[1].split(',')[1]+':' not in globals()['labels']:
                imm = int(line.split()[1].split(',')[1])
                try:
                    imm1 = decimaltobinary(imm, 'signed')
                    
                    output.write(imm1[11]+imm1[21:31]+imm1[20]+imm1[12:20]+registers[lis[0]]+'0010111\n')
                    globals()['pc'] += 4
                    return
                except OverflowError:
                    
                    print('Error: illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
            elif line.split()[1].split(',')[1]+':' in globals()['labels']:
                
                try:
                    imm = decimaltobinary(labels[line.split()[1].split(',')[1]+':']*4-(globals()['pc']+4), 'signed', 20)
                    
                    output.write(imm[0]+imm[10:]+imm[1:9]+registers[lis[0]]+'0010111\n')
                    globals()['pc'] += 4
                    return
                except OverflowError:
                    print('Error: Illegal immediate length')
                    globals()['pc'] = len(globals()['new_lines'])*4
                    return
                

with open('text.txt', 'r') as f:
    lines = f.readlines()

x = assembler()
new_lines = x.remove_special_characters(lines)


pc = 0


if 'beq zero,zero,0' not in new_lines:
    print('Error: Missing virtual halt')
    globals()['pc'] = len(globals()['new_lines'])
    
for label in labels:
    if label.replace(' ', '') != label:
        print('Error: Invalid labels')
        globals()['pc'] = len(globals()['new_lines'])

while pc//4 < len(new_lines):
    x.execution(new_lines[int(pc//4)])
    
output.close()