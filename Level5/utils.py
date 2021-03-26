from pyfinite import ffield
F = ffield.FField(7)

mapping = {}
inverse_mapping = {}

for i in range(16):
    enc = format(i, '0>4b')
    mapping[enc] = chr(ord('f') + i)
    inverse_mapping[chr(ord('f') + i)] = enc

def Expo(a,n):
    if(n==0):
        return 1
    elif(n==1):
        return a
    elif(n%2==0):
        ans = F.Multiply(Expo(a,n/2),Expo(a,n/2))
        return ans 
    else:
        ans = F.Multiply(a, F.Multiply(Expo(a,n//2),Expo(a,n//2)))
        return ans

def Add(a,b):
    return a ^ b

def Multiply(a,b):
    return F.Multiply(a,b)

def MatrixMultiplication(A,v):
    rows, cols = A.shape
    # v will have the same number of rows and only single column
    ans = [0,0,0,0,0,0,0,0]
    for i in range(rows):
        for j in range(cols):
            ans[i] = Add(ans[i], Multiply(v[j], A[i][j]))
    return ans

def E(p,e):
    for i in range(8): 
        p[i] = Exponentiation(p[i], e[i])
    return p

def EAEAE(A,e,p):
    c = []
    for i in range(8):
        c.append(int(inverse_mapping[p[2*i]] + inverse_mapping[p[2*i+1]], 2))
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    return c

def make_vector(p):
    vec = []
    for i in range(8):
        vec.append(int(inverse_mapping[p[2*i]] + inverse_mapping[p[2*i+1]], 2))
    return vec

def refine_outputs(f, n):
    read_file = open(f, "r");
    write_file = open(n, "w+");
    for i in range(8):
        for j in range(128):
            line = read_file.readline().split()
            write_file.write(line[0])
            write_file.write(" ")
        write_file.write("\n")
    read_file.close()
    write_file.close()
