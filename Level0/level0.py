cipher = "wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt"
plaintext = 'wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt'
count = {} 
double_count = {}
done = [0]*len(plaintext)

cipher_list = list(cipher)
plaintext_list = list(plaintext)

key = {}
for i in range(26):
    key[chr(97+i)] = '*'

key['y'] = 'e'
key['m'] = 't'
key['e'] = 'h'
key['w'] = 'i'
key['a'] = 's'
key['s'] = 'r'
key['h'] = 'n'

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

for (i, char) in enumerate(plaintext_list):
    if (char.isalpha() and (done[i] == 0) and (key[plaintext_list[i].lower()] != '*')):
        plaintext_list[i] = key[plaintext_list[i].lower()]
        done[i] = 1

plaintext = ''.join(plaintext_list)
print(plaintext)

keys=list("abcdefghijklmnopqrstuvwxyz")
cipher_text=list("poiuytrewzckjhgfdsamnbvlxq")

dict = {}
for i, char in enumerate(keys):
    dict[char] = cipher_text[i]

print(dict)

text1 = "irst *h *** er*ft he***es .* s** ***nse e, the rei snot hin** fi nterest in the*h*** er .S* *e**the* *ter *h *** ers*i ***e**re inte re stin *th*nthis*n e!Th e*** e*se *** rthi s*es sa* eisa si***es ** s tit*ti on*i*herin*h i*h*i* it sh**e *eensh i*te d**8 ****es. Th e **ss**r *is t*R**03* i* **ith**tthe ***tes. Thi sisthef"

text2 = "irst ih pjo ergft heipbes .P sxg nipnse e, the rei snot hinrg ti nterest in theihpjo er .Sg jegtthek pter ih pjo ersvi kkoejgre inte re stin rthpnthisgn e!Th eigu ense utg rthi smes sar eisa sijfkes no s titnti oniifherinvh iihuir it shpbe oeensh ifte dox8 fkpies. Th e fpssvgr uis txRrN03u id dvithgntthe dngtes. Thi sisthef"

list1 = list(text1)
list2 = list(text2)

for (i, char) in enumerate(list1):
    if (char == '*'):
        list2[i] = '(' + list2[i] + ')'

text2 = ''.join(list2)
print (text2)

"""
irst ch amb eroft hecaves .A syo ucanse e, the rei snot hingo fi nterest in the(i)ha(j)b er .So (j)eofthe(k) ater (i)h a(j)(o) ers(v)i (k)(k)(o)e(j)ore inte re stin gthanthis on e!Th e(i)od euse dfo rthi s(j)es sag eisa si(j)(f)(k)es u(o) s tituti on(i)i(f)herin(v)h i(i)hdg it sh(p)(b)e (o)eensh ifte dby8 (f)(k)a(i)es. Th e (f)ass(v)or dis tyRg(N)03d i(d) (d)(v)ithoutthe (d)uotes. Thi sisthef
"""