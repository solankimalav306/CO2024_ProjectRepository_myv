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
    rd[1]=x0[1]-rs[1]
    return funct7+x0[0]+rs[0]+funct3+rd[0]+opcode
def sltu (rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="011"
    if rs1[1] < rs2[1]:
        rd[1]=1
    else:
        rd[1]=0
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode    
def lw(rd,rs,imm):
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
def Or(rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="110"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode
def sll(rd,rs1,rs2):
    opcode="0110011"
    funct7="0000000"
    funct3="001"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode
def srl(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "101"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def And(rd,rs1,rs2):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "111"
    return funct7+rs2[0]+rs1[0]+funct3+rd[0]+opcode

def sw(rs1,rs2,imm):
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
    
def lui(rd,imm):
    opcode="0110111"
    seximm=sext(imm,20)
    return seximm+rd[0]+opcode
def auipc(rd,imm):
    opcode="0010111"
    imm_binary = sext(imm,20)
    return imm_binary+rd[0]+opcode
RegList = [["zero","00000",0],["ra","00001",0],["sp","00010",0],["gp","00011",18],["tp","00100",0],["t0","00101",0],["t1","00110",0],["t2","00111",0],["s0 fp","01000",0],["s1","01001",0],["a0","01010",0],["a1","01011",0],["a2","01100",0],["a3","01101",0],["a4","01110",0],["a5","01111",0],["a6","10000",0],["a7","10001",0],["s2","10010",0],["s3","10011",0],["s4","10100",0],["s5","10101",0],["s6","10110",0],["s7","10111",0],["s8","11000",0],["s9","11001",0],["s10","11010",0],["s11","11011",0],["t3","11100",0],["t4","11101",0],["t5","11110",0],["t6","11111",0]]
r_type=["add","sub","slt","sltu","xor","sll","srl","Or","And"]
i_type=["lw","addi","sltiu","jalr"]
s_type=["sw"]
b_type=["beq","bne","bge","bgeu","blt","bltu"]
u_type=["auipc","lui"]
j_type=["jal"]
insL=[r_type,i_type,s_type,b_type,u_type,j_type]
ABIname=["zero","ra","sp","gp","tp","t0","t1","t2","s0","fp","s1","a0","a1","a2","a3","a4","a5","a6","a7","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","t3","t4","t5","t6"]
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
            x[i] = x[i][:-1]
    print(x)

def ErrorGen():
    global x , insL
    Realins=False
    MasterL=[]
    if (x[-1]=="beq zero,zero,0") or (x[-1]=="beq zero,zero,0x00000000"):
        for i in x:
            z=i.split()
            MasterL.append(z)
    else:
        return 0
    for i in MasterL:
        if len(i)==0:
            continue
        else:
            if ":" in i[0]:
                i.remove(i[0])
            ins=i[0]
            for q in insL:
                for w in q:
                    if ins==w:
                        containedinsL=q
                        Realins=True
            if Realins==False:
                return 0
            else:
                Realins==False
                x=i[1].split(",")
                if containedinsL==r_type:
                    if (x[0] in ABIname) and (x[1] in ABIname) and (x[2] in ABIname):
                        continue
                    else:
                        return 0
                elif containedinsL==i_type:
                    if i[0]=="lw":
                        lwspecialcase=x[1].split("(")
                        lwspecialcase[1]=lwspecialcase[1][:-1]
                        if (x[0] in ABIname) and (int(lwspecialcase[0])<=2047) and (lwspecialcase[1] in ABIname):
                            continue
                        else:
                            return 0
                    else:
                        if (x[0] in ABIname) and (x[1] in ABIname) and (int(x[2])<=2047):
                            continue
                        else:
                            return 0
                elif containedinsL== s_type:
                    swspecialcase=x[1].split("(")
                    swspecialcase[1]=swspecialcase[1][:-1]
                    if (x[0] in ABIname) and (int(swspecialcase[0])<=2047) and (swspecialcase[1] in ABIname):
                        continue
                    else:
                        return 0
                elif containedinsL == b_type:
                    if (x[0] in ABIname) and (x[1] in ABIname) and (int(x[2])<=4097):
                        continue
                    else:
                        return 0
                elif containedinsL == u_type:
                    if (x[0] in ABIname) and (int(x[1])<= 524287):
                        continue
                    else:
                        return 0
                elif containedinsL == j_type:
                    if (x[0] in ABIname) and (int(x[1])<= 524287):
                        continue
                    else:
                        return 0
    return 1
