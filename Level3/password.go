package main

import (
	"fmt"
	"math/big"
)

// 159733, -204768, 45036
func main() {

	n1 := new(big.Int)
	n1, _ = n1.SetString("11226815350263531814963336315",10)

	n2 := new(big.Int)
	n2, _ = n2.SetString("9190548667900274300830391220",10)

	n3 := new(big.Int)
	n3, _ = n3.SetString("4138652629655613570819000497",10)

	alpha := new(big.Int)
	alpha, _ = alpha.SetString("159733",10)

	beta := new(big.Int)
	beta, _ = beta.SetString("204768",10)

	gamma := new(big.Int)
	gamma, _ = gamma.SetString("45036",10)

	P := new(big.Int)
	P, _ = P.SetString("19807040628566084398385987581",10)

	// n1^(alpha) * n2^(beta) * n3^(gamma)
	n2_inverse := new(big.Int)
	n2_inverse.ModInverse(n2, P)

	x1 := new(big.Int)
	x2 := new(big.Int)
	x3 := new(big.Int)
	x1.Exp(n1, alpha, P)
	x2.Exp(n2_inverse, beta, P)
	x3.Exp(n3, gamma, P)

	x := new(big.Int)
	x.Mul(x1,x2)
	x.Mul(x,x3)
	x.Mod(x, P)
	// x= (x1*x2*x3)  mod P

	fmt.Println(x)

	// beta.Neg(beta)
	// fmt.Println(beta)
	// sum := new(big.Int)
	// sum.Add(alpha, beta)
	// sum.Add(sum, gamma)
	// fmt.Println(sum)

	alpha, _ = alpha.SetString("6953272", 10)
	beta, _ = beta.SetString("-960712", 10) 

	g := new(big.Int)
	g = g.Exp(n1, alpha, P)
	x1.Exp(n1, alpha, P)
	x2.Exp(n2, beta, P)

	x_alpha := new(big.Int)
	x_alpha.Exp(x, alpha.Neg(alpha), P)

	x_beta := new(big.Int)
	x_beta.Exp(x, beta.Neg(beta), P)

	x_inverse := new(big.Int)
	x_inverse.ModInverse(x, P)

	g.Mul(x1, x2)
	g.Mod(g, P)
	g.Mul(g, n3)
	g.Mod(g, P)
	g.Mul(g, x_alpha)
	g.Mod(g, P)
	g.Mul(g, x_beta)
	g.Mod(g, P)
	g.Mul(g, x_inverse)
	g.Mod(g, P)

	fmt.Println(g)
	check := new(big.Int)
	a := new(big.Int)
	a, _ = a.SetString("324", 10)
	g.Exp(g,a,P)
	check.Mul(g, x)
	check.Mod(check, P)
	fmt.Println(check)
}