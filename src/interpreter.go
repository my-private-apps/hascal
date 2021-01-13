package main

import (
	"fmt"
)
func interpreter(n node){
	switch n.kind {

	case "program":
		for _, no := range n.body {
			interpreter(no)
		}
	case "PrintStmt_Number":
		fmt.Print(n.value)
	}
}