def sext(reg,bit):
    if(reg[1]>0):
        regbin = "0"+str(bin(reg[1]))[2:]
    else:
        regbin = "1"+str(bin(reg[1]))[3:]
    flag = "0"
    if(regbin[0]=="1"):
        flag = "1"
    elif(regbin[0]=="0"):
        flag = "0"
    s=(bit-len(regbin)-1)*flag
    s+=regbin
    return s

def add(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "000"
    rd[1] = rs1[1]+rs2[1]
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def sub(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0100000"
    funct3 = "000"
    rd[1] = rs1[1]-rs2[1]
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def slt(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "010"
    rs1bin  = str(bin(rs1[1]))
    rs2bin  = str(bin(rs2[1]))
    # if(len(rs1bin)>len(rs2bin))

RegList = [["00000",0],["00001",0],["00010",0],["00011",18],["00100",0],["00101",0],["00110",0],["00111",0],["01000",0],["01001",0],["01010",0],["01011",0],["01100",0],["01101",0],["01110",0],["01111",0],["10000",0],["10001",0],["10010",0],["10011",0],["10100",0],["10101",0],["10110",0],["10111",0],["11000",0],["11001",0],["11010",0],["11011",0],["11100",0],["11101",0],["11110",0],["11111",0]]


# print(sext(RegList[3],32))