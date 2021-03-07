file='keys.txt'
cand_keys=[]
for i in range(0,8):
    cand_keys.append([])
    
for i in range(0,8):
    for j in range(0,64):
        cand_keys[i].append(0)

with open(file) as f:
    content=f.read().splitlines()
    for k in range(len(content)//8):
        for i in range(8):
            # print(k)
            for j in list(content[8*k+i].split(' ')):
                
                if j!='':
                    a=int(j,2)

                    cand_keys[i][a]+=1

file = open("keys_frequency.txt", "w")

for i in range(8):
    s=sum(cand_keys[i])/64
    m=max(cand_keys[i])
    f=-1
    for j in range(64):
        if cand_keys[i][j]==m:
            f=j
            break
    if f>0:
        file.write(str(f) + " " + str(m) + " " + str(s))
        file.write('\n')

