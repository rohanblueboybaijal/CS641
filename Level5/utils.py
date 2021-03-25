from pyfinite import ffield
F = ffield.FField(7)

mapping = {}
inverse_mapping = {}
for i in range(16):
    enc = format(i, '0>4b')
    mapping[enc] = chr(ord('f') + i)
    inverse_mapping[chr(ord('f') + i)] = enc


def Exponentiation(a,n):
    if(n==0):
        return 1
    if(n==1):
        return a

    if(n%2==0):
        ans = F.Multiply(Exponentiation(a,n/2),Exponentiation(a,n/2))
        return ans
    else:
        ans = F.Multiply(a, F.Multiply(Exponentiation(a,n/2),Exponentiation(a,n/2))
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
        c.append(inverse_mapping[p[2*i:2*i+2]])
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    return c