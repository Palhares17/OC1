from utilities import register_map

def montar_tipo_s(rs1, rs2, imm, funct3):
    bin_rs1 = register_map(rs1)
    bin_rs2 = register_map(rs2)
    imm = int(imm)
    bin_imm = format(imm & 0xFFF, "012b")  # 12 bits
    imm_11_5 = bin_imm[:7]
    imm_4_0  = bin_imm[7:]
    return imm_11_5 + bin_rs2 + bin_rs1 + funct3 + imm_4_0 + "0100011"

def montar_sb(rs2, rs1, imm):
    return montar_tipo_s(rs1, rs2, imm, "000")

def montar_sh(rs2, rs1, imm):
    return montar_tipo_s(rs1, rs2, imm, "001")

def montar_sw(rs2, rs1, imm):
    return montar_tipo_s(rs1, rs2, imm, "010")
