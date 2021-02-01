package main

import "fmt"

func main() {
	var playfair_matrix = [5][5]string{{"S","E","C","U","R"}, 
										{"I","T","Y","A","B"},
										{"D","F","G","H","K"},
										{"L","M","N","O","P"},
										{"Q","V","W","X","Z"}}
	fmt.Println(playfair_matrix[3][4])
}