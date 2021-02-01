package main

import (
	"fmt"
	"strings"
)

type loc struct {
	x int
	y int
}

func decryption(b string, m map[string]loc, playfair_square [5][5]string) string {
	loc1 := m[string(b[0])]
	loc2 := m[string(b[1])]

	decrypted_bigram := ""

	if loc1.y == loc2.y {
		x1 := (loc1.x - 1 + 5) % 5
		x2 := (loc2.x - 1 + 5) % 5
		y1 := loc1.y
		y2 := loc2.y
		decrypted_bigram += string(playfair_square[x1][y1]) + string(playfair_square[x2][y2])
	} else if loc1.x == loc2.x {
		y1 := (loc1.y - 1 + 5) % 5
		y2 := (loc2.y - 1 + 5) % 5
		x1 := loc1.x
		x2 := loc2.x
		decrypted_bigram += string(playfair_square[x1][y1]) + string(playfair_square[x2][y2])
	} else {
		x1 := loc1.x
		x2 := loc2.x
		y1 := loc1.y
		y2 := loc2.y
		decrypted_bigram += string(playfair_square[x1][y2]) + string(playfair_square[x2][y1])
	}
	return decrypted_bigram
}

func main() {
	playfair_matrix := [5][5]string{{"S", "E", "C", "U", "R"},
		{"I", "T", "Y", "A", "B"},
		{"D", "F", "G", "H", "K"},
		{"L", "M", "N", "O", "P"},
		{"Q", "V", "W", "X", "Z"}}
	cipher_text := "B MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH LMRLCCETOT FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC."
	//key := "SECURITY"
	bigrams := []string{}
	cipher_text = strings.ReplaceAll(cipher_text, " ", "")
	cipher_text = strings.ReplaceAll(cipher_text, ".", "")
	cipher_text = strings.ReplaceAll(cipher_text, ",", "")

	// Bigram Generation
	for i := 0; i < len(cipher_text); i += 2 {
		temp := ""
		if i < len(cipher_text)-1 {
			if cipher_text[i] == cipher_text[i+1] {
				temp = string(cipher_text[i]) + "X"
				i -= 1
			} else {
				temp = string(cipher_text[i]) + string(cipher_text[i+1])
			}
		} else {
			temp = string(cipher_text[i]) + "X"
		}
		bigrams = append(bigrams, temp)
	}

	// Location Mapping
	m := make(map[string]loc)
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			m[playfair_matrix[i][j]] = loc{i, j}
		}
	}

	plaintext := ""
	for i := 0; i < len(bigrams); i += 1 {
		plaintext += decryption(bigrams[i], m, playfair_matrix)
	}

	fmt.Println(plaintext)
	//fmt.Println(cipher_text)
}
