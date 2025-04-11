from utilities import register_map

def montar_tipo_b(rs1, rs2, imm, funct3="001", opcode="1100011"):
    bin_rs1 = register_map(rs1)
    bin_rs2 = register_map(rs2)
    imm = int(imm)
    bin_imm = format(imm & 0xFFF, "012b")  # 12 bits

    # Formato B: imm[12|10:5] rs2 rs1 funct3 imm[4:1|11] opcode
    imm_12   = bin_imm[0]
    imm_10_5 = bin_imm[1:7]
    imm_4_1  = bin_imm[7:11]
    imm_11   = bin_imm[11]

    return imm_12 + imm_10_5 + bin_rs2 + bin_rs1 + funct3 + imm_4_1 + imm_11 + opcode

def montar_bne(rs1, rs2, imm):
    return montar_tipo_b(rs1, rs2, imm)
