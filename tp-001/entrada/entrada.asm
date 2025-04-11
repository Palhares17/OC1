add x2, x0, x1
sll x1, x2, x2
xor x2, x2, x1
addi x2, x1, 16
lw x3, 0(x2)
sw x3, 4(x2)
bne x2, x3, 8