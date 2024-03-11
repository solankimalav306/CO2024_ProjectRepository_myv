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
def sub(rd,x0,rs):
    opcode="0110011"
    funct7="0100000"
    funct3="000"
    rd[1]=x0-rs[1]
    return funct7+x0+rs[0]+funct3+rd[0]+opcode
def sltu (rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="011"
    if rs1[1]<rs2[1]:
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

def xor(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "100"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def addi(rd,rs,imm):
    opcode = "0010011"
    funct3= "000"
    sextimm = sext(imm,11)
    return sextimm+rs[0]+funct3+rd[0]+opcode

def sltiu(rd,rs,imm):
    opcode = "0010011"
    funct3 = "011"
    sextimm = sext(imm,11)
    if rs[1]<imm:
        rd[1]=1
    return sextimm+rs[0]+funct3+rd[0]+opcode

RegList = [["00000",0],["00001",0],["00010",0],["00011",18],["00100",0],["00101",0],["00110",0],["00111",0],["01000",0],["01001",0],["01010",0],["01011",0],["01100",0],["01101",0],["01110",0],["01111",0],["10000",0],["10001",0],["10010",0],["10011",0],["10100",0],["10101",0],["10110",0],["10111",0],["11000",0],["11001",0],["11010",0],["11011",0],["11100",0],["11101",0],["11110",0],["11111",0]]
