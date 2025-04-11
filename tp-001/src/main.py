# Instruções do tipo R
from instrucao_R.instrucao import (
    montar_add,
    montar_sub,
    montar_and,
    montar_or,
    montar_xor,
    montar_sll,
    montar_srl
)

# Instruções do tipo I
from instrucao_I.instrucao import (
    montar_addi,
    montar_andi,
    montar_ori,
    montar_lb,
    montar_lh,
    montar_lw
)

# Instruções do tipo S
from instrucao_S.instrucao import (
    montar_sb,
    montar_sh,
    montar_sw
)

# Instruções do tipo B
from instrucao_B.instrucao import montar_bne

def montador_instrucao(linha):
    partes = linha.replace(",", "").replace("(", " ").replace(")", "").split()
    instrucao = partes[0]

    if instrucao == "add":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_add(rd, rs1, rs2)

    elif instrucao == "sub":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_sub(rd, rs1, rs2)

    elif instrucao == "and":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_and(rd, rs1, rs2)

    elif instrucao == "or":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_or(rd, rs1, rs2)

    elif instrucao == "xor":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_xor(rd, rs1, rs2)

    elif instrucao == "sll":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_sll(rd, rs1, rs2)

    elif instrucao == "srl":
        rd, rs1, rs2 = partes[1], partes[2], partes[3]
        return montar_srl(rd, rs1, rs2)

    elif instrucao == "addi":
        rd, rs1, imm = partes[1], partes[2], partes[3]
        return montar_addi(rd, rs1, imm)

    elif instrucao == "andi":
        rd, rs1, imm = partes[1], partes[2], partes[3]
        return montar_andi(rd, rs1, imm)

    elif instrucao == "ori":
        rd, rs1, imm = partes[1], partes[2], partes[3]
        return montar_ori(rd, rs1, imm)

    elif instrucao == "lb":
        rd, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_lb(rd, rs1, imm)

    elif instrucao == "lh":
        rd, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_lh(rd, rs1, imm)

    elif instrucao == "lw":
        rd, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_lw(rd, rs1, imm)

    elif instrucao == "sb":
        rs2, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_sb(rs1, rs2, imm)

    elif instrucao == "sh":
        rs2, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_sh(rs1, rs2, imm)

    elif instrucao == "sw":
        rs2, imm, rs1 = partes[1], partes[2], partes[3]
        return montar_sw(rs1, rs2, imm)

    elif instrucao == "bne":
        rs1, rs2, imm = partes[1], partes[2], partes[3]
        return montar_bne(rs1, rs2, imm)

    else:
        raise ValueError(f"Instrução '{instrucao}' não reconhecida.")

def main():
    with open("entrada/entrada_2.asm", "r") as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()
        if linha == "": continue
        binario = montador_instrucao(linha)
        print(binario)

main()