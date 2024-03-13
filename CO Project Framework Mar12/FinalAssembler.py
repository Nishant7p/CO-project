import os 
import re

Registers = {'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100', 't0': '00101', 't1': '00110', 't2': '00111',
             's0': '01000', 'fp': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 
             'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011', 's4': '10100', 
             's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011', 
             't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111'
}
registerr={"zero":'0',"ra":"0","sp":"0","gp":"0","tp":"0","t0":"0","t1":"0","t1":"0","t2":"0",'s0':'0',"fp":"0",
          "s1":"0","a0":"0","a1":"0","a2":"0","a3":"0","a4":"0","a5":"0","a6":"0","a7":"0","s2":"0",
          "s3":"0","s4":"0","s5":"0","s6":"0","s7":"0","s8":"0","s9":"0","s10":"0","s11":"0",
          "t3":"0","t4":"0","t5":"0","t6":"0"}


global output 
output = open('output.txt', 'w+')

labels = {}

def binary_to_decimal(bin_num, category_='unsigned'):
    if category_ != 'signed':
        result = 0
        for i in range(0, len(bin_num)):
            result += int(bin_num[i]) * (2 ** (len(bin_num)-i-1))
        return result
    else:
        if bin_num[0] == '1':
            result = 0
            result += (-2) ** (len(bin_num) - 1)
            for i in range(1, len(bin_num)):
                result += int(bin_num[i]) * (2 ** (len(bin_num)-i-1))
            return result
        if bin_num[0] == '0':
            result = 0
            for i in range(1, len(bin_num)):
                result += int(bin_num[i]) * (2 ** (len(bin_num)-i-1))
            return result





        

def signextend(digit, number, size=32):
    if len(bin(number)[2:]) > size:
        raise OverflowError('Error: Illegal immediate overflow')
    return digit*(size-len(bin(number)[2:])) + bin(number)[2:]

def decimal_to_binary(number, type_='unsigned', size=32):
    if type_ == 'unsigned':
        nums = number
        return signextend('0', nums, size)
    if type_ == 'signed':
        if number < 0:
            number = '0' + bin(abs(number))[2:]
            new = ''
            for i in number:
                if i == '0':
                    new += '1'
                else:
                    new += '0'
            ones_complement = int(new, 2)
            twos_complement = ones_complement + 1
            return signextend('1', twos_complement, size)
        if number >= 0:
            twos_complement = number
            return signextend('0', twos_complement, size)

    
def contains_integers(input_string):
    pattern = r'^[+-]?\d+$'
    return bool(re.match(pattern, input_string))


def slt(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'010'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    

def sltu(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'011'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    
def add(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'000'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    
        
def sub(line):
    global output
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr:
        output.write('0100000'+Registers[lis[2]]+Registers[lis[1]]+'000'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    

        
def xor(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'100'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    
    
def sll(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'001'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    


def lw(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if '(' not in line or ')' not in line:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if len(lis) != 2:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    src_reg = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][1]
    imm = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][0]
    if lis[0] not in registerr or src_reg not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(imm):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and src_reg in registerr:
        try:
            immediate = decimal_to_binary(int(imm), 'signed', 12)
            output.write(immediate+Registers[src_reg]+'010'+Registers[lis[0]]+'0000011\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return

def sltiu(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        try:
            immediate = decimal_to_binary(int(lis[2]), 'unsigned', 12)
            output.write(immediate+Registers[lis[1]]+'011'+Registers[lis[0]]+'0010011\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return

def jalr(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        try:
            immediate = decimal_to_binary(int(lis[2]), 'signed', 12)
            output.write(immediate+Registers[lis[1]]+'000'+Registers[lis[0]]+'1100111\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return
def srl(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'101'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    

def OR(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'110'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    
        
def AND(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    
    if lis[0] in registerr and lis[1] in registerr and lis[2] in registerr:
        output.write('0000000'+Registers[lis[2]]+Registers[lis[1]]+'111'+Registers[lis[0]]+'0110011\n')
        globals()['PC'] += 4
    else:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return    
        
def addi(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        try:
            imm = decimal_to_binary(int(lis[2]), 'signed', 12)
            output.write(decimal_to_binary(int(lis[2]), 'signed', 12)+Registers[lis[1]]+'000'+Registers[lis[0]]+'0010011\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Invalid immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return
        

def sw(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if '(' not in line or ')' not in line:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if len(lis) != 2:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    src_reg = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][1]
    imm = re.findall(r'\b\w+\s*,\s*(-?\d+)\((\w+)\)', line)[0][0]
    if src_reg not in registerr or lis[0] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(imm):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return            
    if lis[0] in registerr and src_reg in registerr:
        try:
            immediate = decimal_to_binary(int(imm), 'signed', 12)
            output.write(immediate[:7]+Registers[lis[0]]+Registers[src_reg]+'010'+immediate[7:]+'0100011\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return

def beq(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4),'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return

def bne(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'001'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4),'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return

def bge(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr and lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')                    
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'101'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
            
def bgeu(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return 
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'111'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return

def blt(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            if binary_to_decimal(Registers[lis[0]], 'signed') < binary_to_decimal(Registers[lis[1]], 'signed'):
                try:
                    imm = decimal_to_binary(int(lis[2]), 'signed')
                    
                    output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')
                    globals()['PC'] += 4
                    return
                except OverflowError:
                    print('Error: Illegal immediate length')
                    os.remove('output.txt')
                    output.close()
                    output = open('output.txt', 'w+')
                    output.close()
                    globals()['PC'] = len(globals()['newlines'])*4
                    return
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                os.remove('output.txt')
                output.close()
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4),'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'100'+imm[27:31]+imm[20]+'1100011\n')                    
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return

def bltu(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 3:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr or lis[1] not in registerr:
        print('Error: No such register or invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[2]+':' not in globals()['labels'] and not contains_integers(lis[2]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr and lis[1] in registerr:
        if contains_integers(lis[2]):
            try:
                imm = decimal_to_binary(int(lis[2]), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[2].isalnum():
            try:
                imm = decimal_to_binary(labels[lis[2]+':']*4-(globals()['PC']+4), 'signed')
                
                output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'110'+imm[27:31]+imm[20]+'1100011\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return

def auipc(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 2:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(lis[1]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr:
        imm = int(lis[1])
        try:
            immediate = decimal_to_binary(imm, 'signed')
            
            output.write(immediate[:20]+Registers[lis[0]]+'0010111\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return

def lui(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 2:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(lis[1]):
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr:
        imm = int(lis[1])
        try:
            immediate = decimal_to_binary(imm, 'signed')
            output.write(immediate[0:20]+Registers[lis[0]]+'0110111\n')
            globals()['PC'] += 4
        except OverflowError:
            print('Error: Illegal immediate length')
            output.close()
            os.remove('output.txt')
            output = open('output.txt', 'w+')
            output.close()
            globals()['PC'] = len(globals()['newlines'])*4
            return

def jal(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    global output
    if len(lis) != 2:
        print('Error: Syntax error')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] not in registerr:
        print('Error: No such register')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if not contains_integers(lis[1]) and lis[1]+':' not in globals()['labels']:
        print('Error: Invalid immediate')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    if lis[0] in registerr:
        if contains_integers(lis[1]):
            imm = int(lis[1])
            try:
                imm1 = decimal_to_binary(imm, 'signed')
                output.write(imm1[11]+imm1[21:31]+imm1[20]+imm1[12:20]+Registers[lis[0]]+'1101111\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return
        elif lis[1].isalnum():
            
            try:
                imm = decimal_to_binary(labels[lis[1]+':']*4-(globals()['PC']+4), 'signed')
                
                output.write(imm[11]+imm[21:31]+imm[20]+imm[12:20]+Registers[lis[0]]+'1101111\n')
                globals()['PC'] += 4
            except OverflowError:
                print('Error: Illegal immediate length')
                output.close()
                os.remove('output.txt')
                output = open('output.txt', 'w+')
                output.close()
                globals()['PC'] = len(globals()['newlines'])*4
                return


def remove_special_characters(lines):
    newlines = []
    for i in lines:
        j = re.sub(r'\n', '', i)
        k = re.sub(r'//.*', '', j)
        l = re.sub(r'\w+:', '', k)
        newlines.append(l.strip())       
        if re.match(r'\b\w+:', k):
            labels[re.search(r'\b\w+:', k).group()] = lines.index(i)
    new_line = list(filter(lambda x: x != '', newlines))
    return new_line
            
def display():
    print(globals()['new_line'])
    print(globals()['labels'])
    
def Execution(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    Firstpart=line.split()[0] # line ka oPCode check karna
    global output
    if Firstpart == 'jal':
        jal(line)
    elif Firstpart == 'addi':
        addi(line)
    elif Firstpart == 'add':
        add(line)
    elif Firstpart =='sub':
        sub(line)
    elif Firstpart == 'slt':
        slt(line)
    elif Firstpart == 'sltu':
        sltu(line)
    elif Firstpart == 'sll':
        sll(line)
    elif Firstpart == 'srl':
        srl(line)
    elif Firstpart == 'or':
        OR(line)
    elif Firstpart == 'and':
        AND(line)
    elif Firstpart == 'xor':
        xor(line)
    elif Firstpart == 'lw':
        lw(line)
    elif Firstpart == 'sltiu':
        sltiu(line)
    elif Firstpart == 'jalr':
        jalr(line)
    elif Firstpart == 'sw':
        sw(line)
    elif Firstpart == 'beq':
        beq(line)
    elif Firstpart == 'bne':
        bne(line)
    elif Firstpart == 'bge':
        bge(line)
    elif Firstpart == 'bgeu':
        bgeu(line)
    elif Firstpart == 'blt':
        blt(line)
    elif Firstpart == 'bltu':
        bltu(line)
    elif Firstpart == 'auipc':
        auipc(line)
    elif Firstpart == 'lui':
        lui(line)
    elif Firstpart == 'jal':
        jal(line)
    elif line == 'beq zero,zero,0':
        globals()['PC'] = len(globals()['newlines'])*4
        imm = decimal_to_binary(0, 'signed')
        output.write(imm[19]+imm[21:27]+Registers[lis[1]]+Registers[lis[0]]+'000'+imm[27:31]+imm[20]+'1100011\n')
        return
    else:
        print('Error: Invalid instruction')
        output.close()
       
        globals()['PC'] = len(globals()['newlines'])*4
        return
    

with open('hard2', 'r') as f:
    lines = f.readlines()

newlines = remove_special_characters(lines)



PC = 0


if 'beq zero,zero,0' not in newlines:
    print('Error: Missing virtual halt')
    globals()['PC'] = len(globals()['newlines'])*4
if newlines.count('beq zero,zero,0') > 1:
    print('Error: Duplicate virtual halt')
    globals()['PC'] = len(globals()['newlines']) * 4


    
for label in labels:
    if label.replace(' ', '') != label:
        print('Error: Invalid labels')
        globals()['PC'] = len(globals()['newlines'])*4

while PC//4 < len(newlines):
    Execution(newlines[int(PC//4)])
    
output.close()
