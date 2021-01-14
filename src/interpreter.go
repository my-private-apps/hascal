package main

import (
	"fmt"
	// "bufio"
	// "math"
)

type Variable struct {
	name string
	value string
	type_t string
}

var vars = [] Variable { }
func interpreter(n node){
	switch n.kind {

	case "program":
		for _, no := range n.body {
			interpreter(no)
		}
	case "PrintStmt_Number":
		fmt.Print(n.value)
		break
	case "PrintStmt_Name":
		a:= 0
		for a < len(vars) {
			if vars[a].name == n.name {
				fmt.Print(vars[a].value)
			}
			a++
		}
		fmt.Print(n.value)
		break
	case "Declare_IntVariable":
		AddVariable(n.name,n.value,"int")
		break
	default :
		fmt.Println("Interpreter Error")
	}
}

func AddVariable(var_name string,var_value string,var_type string){
	vars = append(vars,Variable {var_name,var_value,var_type})
}