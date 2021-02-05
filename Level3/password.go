package main

import (
	"fmt"
	"math/big"
)

// 159733, -204768, 45036
func main() {
	//var f big.Int
    // f.MulRange(1, 50)
	// fmt.Println(&f)

	n1 := new(big.Int)
	n1, _ = n1.SetString("13820704073802119244527501963",10)
	//fmt.Println(n1)
	//fmt.Println(ok)

	n2 := new(big.Int)
	n2, _ = n2.SetString("13250703864738017529092081924",10)
	//fmt.Println(n2)

	n3 := new(big.Int)
	n3, _ = n3.SetString("12855368516529211269848301050",10)
	//fmt.Println(n3)

	alpha := new(big.Int)
	alpha, _ = alpha.SetString("159733",10)
	//fmt.Println(alpha)

	beta := new(big.Int)
	beta, _ = beta.SetString("204768",10)
	//fmt.Println(beta)

	gamma := new(big.Int)
	gamma, _ = gamma.SetString("45036",10)
	//fmt.Println(gamma)

	P := new(big.Int)
	P, _ = P.SetString("19807040628566084398385987581",10)
	//fmt.Println(P)

	// n1^(alpha) * n2^(beta) * n3^(gamma)
	n2_inverse := new(big.Int)
	n2_inverse.ModInverse(n2, P)
	//fmt.Println(n2_inverse)

	// x := new(big.Int)
	// x.Sub(P, big.NewInt(2))
	// a := new(big.Int)
	// a.Exp(n2, x , P)
	// fmt.Println(a)

	x1 := new(big.Int)
	x2 := new(big.Int)
	x3 := new(big.Int)
	x1.Exp(n1, alpha, P)
	x2.Exp(n2_inverse, beta, P)
	x3.Exp(n3, gamma, P)

	// n2.Mul(n2, n2_inverse)
	// n2.Mod(n2, P)
	//fmt.Println(n2)

	x := new(big.Int)
	x.Mul(x1,x2)
	//x.Mod(x, P)
	x.Mul(x,x3)
	x.Mod(x, P)

	fmt.Println(x)

	beta.Neg(beta)
	fmt.Println(beta)
	sum := new(big.Int)
	sum.Add(alpha, beta)
	sum.Add(sum, gamma)
	fmt.Println(sum)
}