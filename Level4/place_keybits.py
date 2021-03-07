mapping = [
    [24, 27, 21, 6, 11, 15],
    [13, 10, 25, 16, 3, 20],
    [5, 1, 22, 14, 8, 18],
    [26, 17, 9, 2, 23, 12],
    [51, 34, 41, 47, 29, 37],
    [40, 50, 33, 55, 43, 30],
    [54, 31, 49, 38, 44, 35],
    [56, 52, 32, 46, 39, 42],
]

# S_box_number : key_value
known_bits = {
    1:61,
    2:51, 
    5:11,
    6:23,
    7:23,
    8:54, 
}

key = ['X' for _ in range(56)]

for (i, num) in known_bits.items():
    for (j, bit) in enumerate(format(num, '0>6b')):
        if bit == '1':
            key[mapping[i-1][j]-1] = '1'
        else:
            key[mapping[i-1][j]-1] = '0'

print (''.join(key))
