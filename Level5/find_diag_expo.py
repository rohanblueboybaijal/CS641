from utils import *

refine_outputs("outputs.txt", "refined_outputs.txt")

plaintexts = open("plaintexts.txt", "r")
ciphers = open("refined_outputs.txt", "r")

exponents = [[] for i in range(8)]
possible_aii = [[[] for i in range (8)] for j in range(8)]

inputs = []
outputs = []

for i in range(8):
    inputs.append(plaintexts.readline().split())
    outputs.append(ciphers.readline().split())

    ins = [16*(ord(inputs[i][j][2*i]) - ord('f')) + (ord(inputs[i][j][2*i+1]) - ord('f')) for j in range(128)]
    outs = [16*(ord(outputs[i][j][2*i]) - ord('f')) + (ord(outputs[i][j][2*i+1]) - ord('f')) for j in range(128)]

    for j in range(1, 127):
        for k in range(1, 128):
            f = 1
            for x, y in zip(ins, outs):
                if y != Expo(Multiply(Expo(Multiply(Expo(x, j), k), j), k), j):
                    f = 0
                    break 
            if f:
                exponents[i].append(j)
                possible_aii[i][i].append(k)

plaintexts.close()
ciphers.close()

for i in range(7):

    ins = [16*(ord(inputs[i][j][2*i]) - ord('f')) + (ord(inputs[i][j][2*i+1]) - ord('f')) for j in range(128)]
    outs = [16*(ord(outputs[i][j][2*(i+1)]) - ord('f')) + (ord(outputs[i][j][2*(i+1)+1]) - ord('f')) for j in range(128)]

    for j in range(1, 128):
        for exp1, diag1 in zip(exponents[i+1], possible_aii[i+1][i+1]):
            for exp2, diag2 in zip(exponents[i], possible_aii[i][i]):
                f = 1
                for x, y in zip(ins, outs):
                    if y != Expo(Add(Multiply(Expo(Multiply(Expo(x, exp2), diag2), exp2), j), Multiply(Expo(Multiply(Expo(x, exp2), j), exp1), diag1)), exp1):
                        f = 0
                        break
                if f:
                    exponents[i+1] = [exp1]
                    exponents[i] = [exp2]
                    possible_aii[i+1][i+1] = [diag1]
                    possible_aii[i][i] = [diag2]
                    possible_aii[i+1][i] = [j]

print(possible_aii)
print(exponents)
