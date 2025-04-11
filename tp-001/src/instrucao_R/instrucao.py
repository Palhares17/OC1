from utilities import register_map

def montar_tipo_r(rd, rs1, rs2, funct7, funct3, opcode="0110011"):
    bin_rs2 = register_map(rs2)
    bin_rs1 = register_map(rs1)
    bin_rd  = register_map(rd)
    return funct7 + bin_rs2 + bin_rs1 + funct3 + bin_rd + opcode

def montar_add(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "000")

def montar_sub(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0100000", "000")

def montar_and(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "111")

def montar_or(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "110")

def montar_xor(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "100")

def montar_sll(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "001")

def montar_srl(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "101")
