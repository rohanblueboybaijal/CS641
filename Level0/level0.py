cipher = "wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt"
plaintext = 'wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt'
count = {} 
double_count = {}

for char in cipher:
    if (char.isalpha()):
        if chr(ord(char.lower()) - ord('a') + 97) in count :
            count[chr(ord(char.lower()) - ord('a') + 97)] += 1
        else:
            count[chr(ord(char.lower()) - ord('a') + 97)] = 1

for i in range(len(cipher)-1):
    if  cipher[i] == cipher[i+1]:
        doub = cipher[i:i+2]
        if doub in double_count:
            double_count[doub] += 1
        else :
            double_count[doub] = 1

print (count)
print (double_count)

plaintext = plaintext.replace("y", "e")
plaintext = plaintext.replace("m", "t")

print (plaintext)
