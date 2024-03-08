


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
        #storing first word of line in variable (instruction)in inst
        inst=line.split()[0]
        if inst == 'add':
            Addition_R(line)
        elif inst == 'addi':
            Addition_I(line)
        elif inst == 'jal':
            jal(line)
        elif inst =='sub':
            Subtraction(line)
        elif inst == 'sll':
            Shift_Left(line)
        elif inst == 'srl':
            Shift_Right(line)
        elif inst == 'or':
            OR_Gate(line)
        elif inst == 'and':
            AND_Gate(line)
            
def Addition_R():
    return

def Addition_I():
    return

def jal():
    return

def Subtraction():
    return

def Shift_Left():
    return

def Shift_Right():
    return

def OR_Gate():
    return

def AND_Gate():
    return


