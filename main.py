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


RegList = [["00000",0],["00001",0],["00010",0],["00011",0],["00100",0],["00101",0],["00110",0],["00111",0],["01000",0],["01001",0],["01010",0],["01011",0],["01100",0],["01101",0],["01110",0],["01111",0],["10000",0],["10001",0],["10010",0],["10011",0],["10100",0],["10101",0],["10110",0],["10111",0],["11000",0],["11001",0],["11010",0],["11011",0],["11100",0],["11101",0],["11110",0],["11111",0]]
