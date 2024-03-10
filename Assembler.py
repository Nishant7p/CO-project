


register={"zero":00000000000000000000000000000000,"ra":00000000000000000000000000000000,"sp":00000000000000000000000000000000,"gp":00000000000000000000000000000000,"tp":00000000000000000000000000000000,"t0":00000000000000000000000000000000,"t1":00000000000000000000000000000000,"t1":00000000000000000000000000000000,"t2":00000000000000000000000000000000,
          "s1":00000000000000000000000000000000,"a0":00000000000000000000000000000000,"a1":00000000000000000000000000000000,"a2":00000000000000000000000000000000,"a3":00000000000000000000000000000000,"a4":00000000000000000000000000000000,"a5":00000000000000000000000000000000,"a6":00000000000000000000000000000000,"a7":00000000000000000000000000000000,"s2":00000000000000000000000000000000,
          "s3":00000000000000000000000000000000,"s4":00000000000000000000000000000000,"s5":00000000000000000000000000000000,"s6":00000000000000000000000000000000,"s7":00000000000000000000000000000000,"s8":00000000000000000000000000000000,"s9":00000000000000000000000000000000,"s10":00000000000000000000000000000000,"s11":00000000000000000000000000000000,
          "t3":00000000000000000000000000000000,"t4":00000000000000000000000000000000,"t5":00000000000000000000000000000000,"t6":00000000000000000000000000000000}

# defining program counter and Saved register/frame pointer in global
PC=0
s0=fp=00000000000000000000000000000000


# defining memory(32 bit) in a dictionary
memory={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
        "11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,
        "19":19,"20":20,"21":21,"22":22,"23":23,"24":24,"25":25,"26":26,
        "27":27,"28":28,"29":29,"30":30,"31":31}

label={}#making empty dictionary for labels (Branching)
#num is a string actually
def Binary_to_Decimal(num, num_type='signed'):
    if num_type == 'signed':
        if num[0] == 1:
            temp = 0
            temp = temp + (-2)**(len(num)-1)
            for i in range(1, len(num)):
                temp = temp + int(num[i])*(2**(len(num)-i-1))
            return temp
        else:
            temp = 0
            for i in range(0, len(num)):
                temp = temp + int(num[i])*(2**(len(num)-i-1))
            return temp
    if num_type=="unsigned":
        temp = 0
        for i in range(0, len(num)):
            temp = temp + int(num[i])*(2**(len(num)-i-1))
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
        #storing first word of line in variable (instruction)in firstpart example --> "add"
        firstpart=line.split()[0]
        #matching that instruction and assigning corresponding function
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
            
def Addition_R(line):
    # taking 2 part of the line(next to blank spaces containing registers and other stuff) as 1 part is for instruction
    # we are breaking as  add reg1, reg2, reg3 when we split line we get ["add","reg1,reg2,reg3"]
    # by taking [1] we are taking "reg1,reg2,reg3"
    secondpart=line.split()[1]
    # second_part.split(",") makes string a list like [reg1,reg2,reg3]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register: #means all register are given registers only
         register[lis[0]] = Binary_to_Decimal(register[lis[1]]) + Binary_to_Decimal(register(lis[2]))
         Decimal_to_Binary(register[lis[0]])
         PC=PC+4
    

    return

def Addition_I(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        register[lis[0]]=Binary_to_Decimal(lis[1])+int(lis[2])#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4


    return

def jal(line):
    return
# bhai ye subtraction me issue hai signd lena ha unsigned liya h tune
def Subtraction(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]]) - Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4


    return

def Shift_Left(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]],"unsigned") << Binary_to_Decimal(register(lis[2]),"unsigned")
        Decimal_to_Binary(register[lis[0]],"unsigned")
        PC=PC+4

    return

def Shift_Right(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]],"unsigned") >> Binary_to_Decimal(register(lis[2]),"unsigned")
        Decimal_to_Binary(register[lis[0]],"unsigned")
        PC=PC+4

    return

def OR_Gate(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]])|Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4

    return

def AND_Gate(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]])&Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4

    return


def Branch_Eq(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])==Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])

     return 

def Branch_Neq(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])!=Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])

     return 

def Branch_GreaterEq(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])>=Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])

     return

def Branch_GreaterEq_Unsigned(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]], 'unsigned')>=Binary_to_Decimal(register[lis[1]], 'unsigned'):
             PC=PC+int(lis[2])


     return

def Branch_Less(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]])<Binary_to_Decimal(register[lis[1]]):
             PC=PC+int(lis[2])

def Branch_Less_Unsigned(line):
     secondpart=line.split()[1]
     lis=secondpart.split(",")
     if lis[0] in register and lis[1] in register:
         if Binary_to_Decimal(register[lis[0]],"unsigned")<Binary_to_Decimal(register[lis[1]],"unsigned"):
             PC=PC+int(lis[2])
             return



def lw(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        lis[0]=memory[str((int(lis[2]) + Binary_to_Decimal(lis[1]) - 65536)//4)-1]



def sltiu(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register:
        if Binary_to_Decimal(lis[1],"unsigned")<int(lis[2]):
            lis[0]=1
        PC=PC+4



def sw(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register:
         memory[(str(int(lis[2]) + Binary_to_Decimal(lis[1]) - 65536)//4)-1] = register[lis[0]]
         PC=PC+4









if __name__ == "__main__":
     with open('in.txt', 'r') as rfile:
        variables_end_index = 0
        lines = rfile.readlines()
    
     for line in lines:
        line = line.strip("\n")
        
        # print(line.split())
        if line == "":
            continue
        #if is_var(line):!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #handle_variable(line)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            break
        variables_end_index += 1
    # print(variables_end_index)
     for line in lines[variables_end_index:]:
        line = line.strip("/n")
        
        # print(line.split())
        if line == "":
            continue
        #if is_var(line):
            #print("declare all variables at the start")
            #exit()
        #if is_label(line):
            #handle_label(line)
        #counter += 1
    #address_variables()
     for line in lines[variables_end_index:-1]:
        line = line.strip("\n")
        
        # print(line.split())
        if line == "":
            continue
        #if is_label(line):
            #line = strip_label(line)
        if line == "hlt":
            print("hlt not being used as the last instruction")
            exit()
        #handle_instruction(line)
     #if is_label(lines[-1]):
        #line = strip_label(lines[-1])
        #if line == "hlt":
            #handle_instruction(line)
        #else:
            #print("Missing hlt instruction")
            #exit()
    #elif lines[-1].strip("\n").strip() != "hlt":
        #print("Missing hlt instruction")
        #exit()
   # else:
        #handle_instruction(lines[-1].strip("\n").strip())
    #make_instructions()

    # print(variables)
    # print(labels)












 



    


