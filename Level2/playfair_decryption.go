package main

import (
	"fmt"
	"strings"
)

type loc struct {
	x int
	y int 
}

func main() {
	playfair_matrix := [5][5]string{{"S","E","C","U","R"}, 
										{"I","T","Y","A","B"},
										{"D","F","G","H","K"},
										{"L","M","N","O","P"},
										{"Q","V","W","X","Z"}}
	cipher_text := "B MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH LMRLCCETOT FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC."
	//key := "SECURITY"
	bigrams := []string{}
	cipher_text = strings.ReplaceAll(cipher_text, " ", "")
	cipher_text = strings.ReplaceAll(cipher_text, ".", "")
	
	// Bigram Generation
	for i := 0; i < len(cipher_text); i += 2 {
		temp := ""
		if (i < len(cipher_text)-1) {
			temp = string(cipher_text[i]) + string(cipher_text[i+1])
		} else {
			temp = string(cipher_text[i]) + "z"
		}
		bigrams = append(bigrams, temp)
	}

	// Location Mapping
	m := make(map[string]loc)
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			m[playfair_matrix[i][j]] = loc {i, j}
		}
	}
	
	fmt.Println(cipher_text)
	fmt.Println(bigrams)
	fmt.Println(m["A"].x)
}