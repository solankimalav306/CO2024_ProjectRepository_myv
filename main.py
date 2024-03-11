def sext(imm,bit):
    if(imm>0):
        regbin = "0"+str(bin(imm))[2:]
    else:
        regbin = "1"+str(bin(imm))[3:]
    flag = "0"
    if(regbin[0]=="1"):
        flag = "1"
    elif(regbin[0]=="0"):
        flag = "0"
    s=(bit-len(regbin)-1)*flag
    s+=regbin
    return s

# def bintodeci(binval,bit):
#     flag = 0
#     if(binval[0] == "1"):
#         flag = 1
#     else:
#         flag  = 0
#     s=""
    

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
def sltu (rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="011"
    if rs1[1] < rs2[1]:
        rd[1]=1
    else:
        rd[1]=0
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode    
def lw(rd,imm,rs):
    opcode="0000011"
    funct3="010"
    sextimm = sext(imm,11)
    sextrs = sext(rs[1])
    rd[1]=sextrs+sextimm
    return sextimm+rs[0]+funct3+rd[0]+opcode

def slt(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "010"
    if(sext(rs1,32)<sext(rs2,32)):
        rd[1] = 1
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def xor_bitwise(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "100"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode
def or_bitwise(rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="110"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode
def srl(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "101"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def and_bitwise(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "111"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def sw(imm,rs1,rs2):
    opcode = "0100011"
    funct3 = "010"
    immbin = sext(imm,11)
    return immbin[0:7]+rs2[0]+rs1[0]+funct3+immbin[7:]+opcode
def addi(rd,rs,imm):
    opcode = "0010011"
    funct3= "000"
    sextimm=sext(imm,11)
    return sextimm+rs+funct3+rd+opcode

def sltiu(rd,rs,imm):
    opcode = "0010011"
    funct3 = "011"
    sextimm = sext(imm,11)
    if rs[1]<imm:
        rd[1]=1
    return sextimm+rs[0]+funct3+rd[0]+opcode

def jalr(rd,offset):
    opcode = "1100111"
    funct3 = "000"
    rd[1]= offset + 4
    sextoff=sext(offset,11)
    return sextoff+RegList[5][0]+funct3+rd[0]+opcode

RegList = [["00000",0],["00001",0],["00010",0],["00011",18],["00100",0],["00101",0],["00110",0],["00111",0],["01000",0],["01001",0],["01010",0],["01011",0],["01100",0],["01101",0],["01110",0],["01111",0],["10000",0],["10001",0],["10010",0],["10011",0],["10100",0],["10101",0],["10110",0],["10111",0],["11000",0],["11001",0],["11010",0],["11011",0],["11100",0],["11101",0],["11110",0],["11111",0]]

zero=RegList[0]
ra=RegList[1]
sp=RegList[2]
gp=RegList[3]
tp=RegList[4]
t0=RegList[5]
t1=RegList[6]
t2=RegList[7]
s0=RegList[8]
fp=RegList[8]
s1=RegList[9]
a0=RegList[10]
a1=RegList[11]
a2=RegList[12]
a3=RegList[13]
a4=RegList[14]
a5=RegList[15]
a6=RegList[16]
a7=RegList[17]
s2=RegList[18]
s3=RegList[19]
s4=RegList[20]
s5=RegList[21]
s6=RegList[22]
s7=RegList[23]
s8=RegList[24]
s9=RegList[25]
s10=RegList[26]
s11=RegList[27]
t3=RegList[28]
t4=RegList[29]
t5=RegList[30]
t6=RegList[31]


with open("coprj_mvy\input.txt") as f:
    x = f.readlines()
    for i in range(len(x)):
        if(i!=len(x)-1):
            x[i] = x[i][:-2]
    print(x)
