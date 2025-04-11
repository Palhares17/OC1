def register_map(r):
    for i in range(32):
        reg = f"x{i}" #x0, x1, x2, ...
        binario = format(i, "05b")

        if r == reg:
            return binario

# Permite tranformar números negativos em binários de forma correta
def int_to_bin(value, bits):
    return format(int(value) & (2**bits - 1), f'0{bits}b') 
