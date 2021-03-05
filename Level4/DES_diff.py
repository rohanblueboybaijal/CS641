import numpy as np 

map = {
    'f' : '0000',
    'g' : '0001',
    'h' : '0010',
    'i' : '0011',
    'j' : '0100',
    'k' : '0101',
    'l' : '0110',
    'm' : '0111',
    'n' : '1000',
    'o' : '1001',
    'p' : '1010',
    'q' : '1011',
    'r' : '1100',
    's' : '1101',
    't' : '1110',
    'u' : '1111'
}

def char_to_bits(x):
    inputs = []
    for i in range(len(x)):
        temp = ""
        for j in range(16):
            temp +=  map[x[i][j]]
        inputs.append(temp)
    return inputs

file = open("output_random.txt", "r")
outputs = file.read().split("\n")
output_bits = char_to_bits(outputs)
# print (output_bits)

reverse_final_perm = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8]

final_outputs = [", ".join([output_bits[j][reverse_final_perm[i]-1] for i in range(64)]).replace(', ', '') for j in range(len(output_bits))]
# print(final_outputs)

Xor_outputs = [", ".join([str(int(final_outputs[2*i+1][j]) ^ int(final_outputs[2*i][j])) for j in range(64)]).replace(', ', '') for i in range(len(final_outputs) // 2)]

# print(Xor_outputs)
Exp_box = [32, 1, 2, 3, 4, 5, 4, 5,6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

Expanded_out = [", ".join([final_outputs[i][Exp_box[j]-1] for j in range(48)]).replace(", ", "") for i in range(len(final_outputs))]

# print (Expanded_out)
S_box_in = [", ".join([str(int(Expanded_out[2*i+1][j]) ^ int(Expanded_out[2*i][j])) for j in range(48)]).replace(', ', '') for i in range(len(Expanded_out) // 2)]

# print(S_box_in)

L5 = '00000100' + '0'*24
Permut_Xor = [", ".join([str(int(Xor_outputs[i][32+j]) ^ int(L5[j])) for j in range(32)]).replace(", ", "") for i in range(len(Xor_outputs))]

# print(Permut_Xor)

Inv_permutation = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]

S_box_out = [", ".join([Permut_Xor[j][Inv_permutation[i]-1] for i in range(32)]).replace(', ', '') for j in range(len(Permut_Xor))]

# print (S_box_out)

file = open("S_box_inputs.txt", "w")
for i in S_box_in:
    file.write(i)
    file.write("\n")

file.close()

file = open("S_box_outputs.txt", "w")
for i in S_box_out:
    file.write(i)
    file.write("\n")

file.close()

file = open("Expansion_output.txt", "w")
for i in Expanded_out:
    file.write(i)
    file.write('\n')
file.close()
