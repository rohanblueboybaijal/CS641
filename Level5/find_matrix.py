from utils import *

A = [[84, 0, 0, 0, 0, 0, 0, 0],
[119, 70, 0, 0, 0, 0, 0, 0],
[0, 30, 43, 0, 0, 0, 0, 0],
[0, 0, 1, 12, 0, 0, 0, 0],
[0, 0, 0, 104, 112, 0, 0, 0],
[0, 0, 0, 0, 96, 11, 0, 0],
[0, 0, 0, 0, 0, 88, 27, 0],
[0, 0, 0, 0, 0, 0, 2, 38]]

exponents = [23, 118, 38, 76, 92, 45, 24, 23]

plaintexts = open("plaintexts.txt", "r")
ciphers = open("refined_outputs.txt", "r")

inputs = []
outputs = []

for _ in range(8):
    inputs.append(plaintexts.readline().split())
    outputs.append(ciphers.readline().split())

plaintexts.close()
ciphers.close()

for off_d in range(2,8):
    for c in range(8-off_d):
        i = c + off_d
        ins = [16*(ord(inputs[c][j][2*c]) - ord('f')) + (ord(inputs[c][j][2*c+1]) - ord('f')) for j in range(128)]
        outs = [16*(ord(outputs[c][j][2*(i)]) - ord('f')) + (ord(outputs[c][j][2*(i)+1]) - ord('f')) for j in range(128)]
        for k in range(1,128):
            A[i][c] = k
            f = 1
            for index, (x, y) in enumerate(zip(ins, outs)):
                p = [0,0,0,0,0,0,0,0]
                p[c] = x
                cipher = EAEAE(A,exponents,p)
                if y != cipher[i]:
                    f = 0
                    A[i][c] = 0
                    break 
            if f:
                A[i][c] = k
                break

print(A)