


#defining register in a dictionary
register={"zero":0,"ra":0,"sp":0,"gp":0,"tp":0,"t0":0,"t1":0,"t1":0,"t2":0,
          "s1":0,"a0":0,"a1":0,"a2":0,"a3":0,"a4":0,"a5":0,"a6":0,"a7":0,"s2":0,
          "s3":0,"s4":0,"s5":0,"s6":0,"s7":0,"s8":0,"s9":0,"s10":0,"s11":0,
          "t3":0,"t4":0,"t5":0,"t6":0}

# defining program counter and Saved register/frame pointer in global
PC=0
s0=fp=0


# defining memory(32 bit) in a dictionary
memory={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
        "11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,
        "19":19,"20":20,"21":21,"22":22,"23":23,"24":24,"25":25,"26":26,
        "27":27,"28":28,"29":29,"30":30,"31":31}

label={}#making empty dictionary for labels (Branching)

def Binary_to_Decimal(num, num_type='unsigned'):
    return
def Decimal_to_Binary(num, num_type='unsigned'):
    return

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
        register[lis[0]]=Binary_to_Decimal([lis[1]]+int(lis[2]))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4


    return

def jal(line):
    return

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
        register[lis[0]] = Binary_to_Decimal(register[lis[1]]) << Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])
        PC=PC+4

    return

def Shift_Right(line):
    secondpart=line.split()[1]
    lis=secondpart.split(",")
    if lis[0] in register and lis[1] in register and lis[2] in register:
        register[lis[0]] = Binary_to_Decimal(register[lis[1]]) >> Binary_to_Decimal(register(lis[2]))
        Decimal_to_Binary(register[lis[0]])
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


