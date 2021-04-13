e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693

def find_roots(pol, modulus, m, k):

    deg = pol.degree()
    n = deg*m 
    pol_in_Z = pol.change_ring(ZZ)
    x = pol_in_Z.parent().gen()

    new_pols = []
    for i in range(m):
        for j in range(deg):
            new_pols.append((x*k)**j * modulus**(m-i) * pol_in_Z(x*k)**(i))

    B = Matrix(ZZ, n)

    for i in range(n):
        for j in range(i+1):
            B[i,j] = new_pols[i][j]

    reduced_B = B.LLL()

    g = 0
    for i in range(n):
        g += x**i * reduced_B[0,i]/(k**i)

    candidates = g.roots()

    final = []
    for y in candidates:
        if y[0].is_integer():
            val = pol_in_Z(ZZ(y[0]))
            if val%modulus == 0:
                final.append(ZZ(y[0]))

    return final

def find_message(padding, max_bits):
    padding_bin = ''.join([format(ord(c), '0>8b') for c in padding])
    
    for l in range(0, max_bits+1, 8):
        
        P.<x> = PolynomialRing(Zmod(N))
        pol = ((int(padding_bin, 2)<<l) + x)^e - C 

        ## Coppersmith attack parameters
        eps = 1/7
        m = ceil(1/(5*eps))
        k = ceil(N**((1/5) - eps))

        roots = find_roots(pol, N, m, k)

        if roots:
            print ("Root found: ", format(roots[0], 'b'))
            return
        
    print("No root found")
    
find_message("You see a Gold-Bug in one corner. It is the key to a treasure found by ", 300)

