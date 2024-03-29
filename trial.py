# Register Set with DEFAULT VALUES
reg1 = ["0000",0]
reg2 = ["0001",0]
reg3 = ["0010",0]

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



bincode = []
with open("coprj_mvy\input.txt") as f:
    for i in f.readlines():
        x = i.split(" ")
        command  = x[0]
        x[1] = x[1][0:-1]
        # print(x)
        registers = x[1].split(",")
        reglist = []
        for i in registers:
            reglist.append(int(i[-1])-1)
        # print(reglist)
        regcount = 0
        for j in reglist:
            if regcount == 0:
                if j==0:
                    rd = reg1
                    regcount+=1
                elif j==1:
                    rd = reg2
                    regcount+=1
                elif j==2:
                    rd = reg3
                    regcount+=1
            elif regcount == 1:
                if j==0:
                    rs1 = reg1
                    regcount+=1
                elif j==1:
                    rs1 = reg2
                    regcount+=1
                elif j==2:
                    rs1 = reg3
                    regcount+=1
            elif regcount == 2:
                if j==0:
                    rs2 = reg1
                    regcount+=1
                elif j==1:
                    rs2 = reg2
                    regcount+=1
                elif j==2:
                    rs2 = reg3
                    regcount+=1
        # print(rd,rs1,rs2)
        if command=="add":
            bincode.append(add(rd,rs1,rs2))
        elif command=="sub":
            bincode.append(sub(rd,rs1,rs2))
with open("coprj_mvy\output.txt","w+") as g:
    for i in bincode:
            g.write(i+"\n")
            
            

print("Updated Register values")
print("Register 1 =",reg1[1])
print("Register 2 =",reg2[1])
print("Register 3 =",reg3[1])

# print(x)