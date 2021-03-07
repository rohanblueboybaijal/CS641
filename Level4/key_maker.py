key = 'XX1XX1XXX10X1X10XXX11XX10X1X1110001X11101011X10X0101X011'

file = open("Final_keys.txt", "w")
temp = ""

for i in range(2**20):
    bits = format(i, '0>20b')
    curr = 0
    for char in key:
        if char == 'X':
            temp += bits[curr]
            curr += 1
        else:
            temp += char
    file.write(temp)
    file.write('\n')
    temp = ""

file.close()