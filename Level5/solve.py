from utils import *

refine_outputs("outputs.txt", "refined_outputs.txt")

plaintexts = open("plaintexts.txt", "r")
ciphers = open("refined_outputs.txt", "r")

exponents = [[] for i in range(8)]
possible_aii = [[[] for i in range (8)] for j in range(8)]

for i in range(8):
    inputs = plaintexts.readline().split()
    outputs = ciphers.readline().split()

    ins = [16*(ord(inputs[j][2*i]) - ord('f')) + (ord(inputs[j][2*i+1]) - ord('f')) for j in range(128)]
    outs = [16*(ord(outputs[j][2*i]) - ord('f')) + (ord(outputs[j][2*i+1]) - ord('f')) for j in range(128)]

    for j in range(1, 127):
        # print (j)
        for k in range(1, 128):
            f = 1
            for x, y in zip(ins, outs):
                # print(x, y)
                if y != Expo(Multiply(Expo(Multiply(Expo(x, j), k), j), k), j):
                    f = 0
                    break 
            if f:
                exponents[i].append(j)
                possible_aii[i][i].append(k)

print(exponents)
print(possible_aii)
