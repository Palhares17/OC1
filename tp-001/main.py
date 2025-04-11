def register_map(r):
    for i in range(32):
        reg = f"x{i}"
        binario = format(i, "05b")

        if r == reg:
            return binario

# Inicio do formato R
def montar_tipo_r(rd, rs1, rs2, funct7, funct3, opcode="0110011"):
    bin_rs2 = register_map(rs2)
    bin_rs1 = register_map(rs1)
    bin_rd  = register_map(rd)
    return funct7 + bin_rs2 + bin_rs1 + funct3 + bin_rd + opcode

def montar_add(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "000")

def montar_xor(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "100")

def montar_sll(rd, rs1, rs2):
    return montar_tipo_r(rd, rs1, rs2, "0000000", "001")

# Fim do formato R

# Inicio do formato I
def montar_tipo_i(rd, rs1, imm, funct3, opcode):
    imm_bin = format(int(imm) & 0xFFF, "012b")  # 12 bits com sinal
    bin_rs1 = register_map(rs1)
    bin_rd  = register_map(rd)
    return imm_bin + bin_rs1 + funct3 + bin_rd + opcode

def montar_addi(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "000", "0010011")

def montar_lw(rd, rs1, imm):
    return montar_tipo_i(rd, rs1, imm, "010", "0000011")
# Final do formato I

def montar_tipo_s(rs1, rs2, imm, funct3="010", opcode="0100011"):
    imm = int(imm) & 0xFFF
    imm_bin = format(imm, "012b")
    imm_11_5 = imm_bin[:7]
    imm_4_0 = imm_bin[7:]
    bin_rs1 = register_map(rs1)
    bin_rs2 = register_map(rs2)
    return imm_11_5 + bin_rs2 + bin_rs1 + funct3 + imm_4_0 + opcode

def montar_tipo_b(rs1, rs2, imm, funct3="001", opcode="1100011"):
    imm = int(imm) & 0x1FFF
    imm_bin = format(imm, "013b")
    imm_12 = imm_bin[0]
    imm_10_5 = imm_bin[1:7]
    imm_4_1 = imm_bin[7:11]
    imm_11 = imm_bin[11]
    bin_rs1 = register_map(rs1)
    bin_rs2 = register_map(rs2)
    return imm_12 + imm_10_5 + bin_rs2 + bin_rs1 + funct3 + imm_4_1 + imm_11 + opcode


def montador_instrucao(linha):
    partes = linha.replace(",", "").replace("(", " ").replace(")", "").split()
    instrucao = partes[0]

    if instrucao == "add":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_add(rd, rs1, rs2)
    
    elif instrucao == "xor":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_xor(rd, rs1, rs2)
    
    elif instrucao == "sll":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_sll(rd, rs1, rs2)
    
    elif instrucao == "addi":
        rd, rs1, imm = partes[1], partes[2], partes[3]
        return montar_addi(rd, rs1, imm)
    
    elif instrucao == "lw":
        rd, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_lw(rd, rs1, imm)
    
    elif instrucao == "sw":
        rs2, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_tipo_s(rs1, rs2, imm)
    
    elif instrucao == "bne":
        rs1, rs2, imm = partes[1], partes[2], partes[3]
        return montar_tipo_b(rs1, rs2, imm)

def main():
    with open("entrada/entrada.asm", "r") as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()
        if linha == "": continue
        binario = montador_instrucao(linha)
        print(binario)

main()