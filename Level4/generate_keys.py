S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],
    [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9]],

    [[10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
def generate_keys(alpha_1,alpha_2,gamma, index):
    alpha=alpha_1^alpha_2
    gamma=gamma
    beta_1=0
    beta_2=0
    keys=[]

    for beta_1 in range(64):
        beta_2=alpha^beta_1
        a=format(beta_1,'0>6b')
        b=format(beta_2,'0>6b')
        
        r1 = int(a[0])*2 + int(a[5])
        r2 = int(b[0])*2 + int(b[5])
        c1 = int(a[4]) + 2 *int(a[3]) + int(a[2]) * 4 + int(a[1])*8
        c2 = int(b[4]) + 2 *int(b[3]) + int(b[2]) * 4 + int(b[1])*8

        gamma_1=S[index][r1][c1]
        gamma_2=S[index][r2][c2]
        if gamma_1^gamma_2==gamma:
            k=beta_1^alpha_1
            k=format(k,'0>6b')
            keys.append(k)
    return keys

def main():

    file='S_box_inputs.txt'
    S_box_input=[]
    with open(file) as f:
        content=f.read().splitlines()
        for i in range(len(content)):
            
            S_box_input.append(content[i])

    f.close()
        
    file='S_box_outputs.txt'
    S_box_output=[]
    with open(file) as f:
        content=f.read().splitlines()
        for i in range(len(content)):
            S_box_output.append(content[i])
        
    file='Expansion_output.txt'
    expansion_output=[]
    with open(file) as f:
        content=f.read().splitlines()
        for i in range(0,len(content),2):
            expansion_output.append((content[i],content[i+1]))
    keys=[]

    for i in range(len(expansion_output)):
        for j in range(0,8):
            a=generate_keys(int(expansion_output[i][0][6*j:6*j+6],2), int(expansion_output[i][1][6*j:6*j+6],2), int(S_box_output[i][4*j:4*j+4],2), j)
            keys.append(a)

    with open("keys.txt", "w") as txt_file:
        for line in keys:
            txt_file.write(" ".join(line) + "\n")  
        
main()