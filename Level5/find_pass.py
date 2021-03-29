from utils import *

A = [[84, 0, 0, 0, 0, 0, 0, 0], [119, 70, 0, 0, 0, 0, 0, 0], [14, 30, 43, 0, 0, 0, 0, 0], [97, 16, 1, 12, 0, 0, 0, 0], [99, 35, 1, 104, 112, 0, 0, 0], [24, 46, 18, 52, 96, 11, 0, 0], [9, 124, 20, 103, 30, 88, 27, 0], [65, 15, 87, 27, 10, 67, 2, 38]]

exponents = [23, 118, 38, 76, 92, 45, 24, 23]

cipher = "msjjkrlmhimumuilloghgikgfllqkjgi"

cipher1 = cipher[:16]
cipher2 = cipher[16:]

out1 = make_vector(cipher1)
out2 = make_vector(cipher2)

p = [0 for _ in range(8)]
q = [0 for _ in range(8)]

for i in range(8):
    for j in range(1,128):
        p[i] = j
        x = EAEAE(A, exponents, p)
        if x[i] == out1[i]:
            p[i] = j
            break
        else:
            p[i] = 0

for i in range(8):
    for j in range(1,128):
        q[i] = j
        x = EAEAE(A, exponents, q)
        if x[i] == out2[i]:
            q[i] = j
            break
        else:
            q[i] = 0

# print(to_encoding(p) + to_encoding(q))
print(to_ascii(p) + to_ascii(q))