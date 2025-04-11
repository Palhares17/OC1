from utilities import register_map, int_to_bin

def montar_tipo_i(rd, rs1, imm, funct3, opcode):
    bin_rs1 = register_map(rs1)
    bin_rd = register_map(rd)
    bin_imm = int_to_bin(imm, 12)
    return bin_imm + bin_rs1 + funct3 + bin_rd + opcode

# Imediatos aritméticos/lógicos
def montar_addi(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "000", "0010011")

def montar_andi(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "111", "0010011")

def montar_ori(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "110", "0010011")

# Loads
def montar_lb(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "000", "0000011")

def montar_lh(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "001", "0000011")

def montar_lw(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "010", "0000011")
