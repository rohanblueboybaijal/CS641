import binascii
import random

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


inv_map = {
    '0000' : 'f',
    '0001' : 'g',
    '0010' : 'h',
    '0011' : 'i',
    '0100' : 'j',
    '0101' : 'k',
    '0110' : 'l',
    '0111' : 'm',
    '1000' : 'n',
    '1001' : 'o',
    '1010' : 'p',
    '1011' : 'q',
    '1100' : 'r',
    '1101' : 's',
    '1110' : 't',
    '1111' : 'u'
}

reverse_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
39,	7, 47, 15, 55, 23, 63, 31,
38,	6, 46, 14, 54, 22, 62, 30,
37,	5, 45, 13, 53, 21, 61, 29,
36,	4, 44, 12, 52, 20, 60, 28,
35,	3, 43, 11, 51, 19, 59, 27,
34,	2, 42, 10, 50, 18, 58, 26,
33,	1, 41, 9,  49, 17, 57, 25,]

def bits_to_char(x):
    i = 0
    plaintext = ''
    while i < 64:
        block = x[i:i+4]
        i += 4
        plaintext += inv_map[block]
    return plaintext

def inverse_IP(x):
    inverse = ""
    x = format(int(x, 16), '0>64b')
    for i in range(64):
        inverse += x[reverse_permutation[i]-1]
    inverse = hex(int(inverse, 2))[2:]
    return inverse 

required_xor = inverse_IP('405c000004000000')
number = int(required_xor, 16)
X = format(number, '0>64b')

plaintext_bits = open('./plaintext_bits.txt', 'a')
plaintext_pairs = open('./plaintext_pairs.txt', 'a')

for i in range(2**20):
    n1 = random.randint(0, 2**64 - 1)
    x1 = format(n1, '0>64b')
    x2 = ''
    for j in range(64):
        bit = str(int(x1[j]) ^ int(X[j]))
        x2 += bit
    p1 = bits_to_char(x1)
    p2 = bits_to_char(x2)

    plaintext_bits.write(x1)
    plaintext_bits.write('\n')
    plaintext_bits.write(x2)
    plaintext_bits.write('\n')

    plaintext_pairs.write(p1)
    plaintext_pairs.write('\n')
    plaintext_pairs.write(p2)
    plaintext_pairs.write('\n')

plaintext_pairs.close()
plaintext_bits.close()