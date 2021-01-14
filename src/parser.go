package main

import (
	"fmt"
	"log"
	"strconv"
)

type Parser struct {
	S *Scanner
}

var pc int
var pt []Token

func (p *Parser) parse(toks []Token) ast {
	pt = toks
	ast := ast{
		kind : "program",
		body: []node{},
	}

	for pc <len(pt) {
		ast.body = append(ast.body,walk())
	}
	
	return ast
}


func walk() node {
	token := pt[pc]

	// var <name> = <expr> ;
	if token.token_type == "VAR" {
		pc++
		token = pt[pc]

		if token.token_type == "NAME" {
			temp_name := token.token_value

			pc++
			token = pt[pc]

			if token.token_type == "EQUAL" {
				pc++
				token = pt[pc]

				if token.token_type == "NUMBER" {
					num := token.token_value
					pc++
					token = pt[pc]

					if CheckSemiColon(token) {
						return node{
							kind:  "Declare_IntVariable",
							name: temp_name,
							value : num,
						}
					}
					
				}

			}
			
		}
		
	}

	// print <expr> ;
	if token.token_type == "PRINT" {
		pc++
		token = pt[pc]

		if token.token_type == "NAME" {
			temp_name := token.token_value

			pc++
			token = pt[pc]

			if CheckSemiColon(token) {
				return node{
					kind: "PrintStmt_Name",
					name : temp_name,
				}
			} 
			
		}else if token.token_type == "NUMBER" {
			num := token.token_value
			pc++
			token = pt[pc]
			
			if CheckSemiColon(token) {
				pc++
				return node{
					kind: "PrintStmt_Number",
					value : num,
				}
			}
		}
	}

	log.Fatal(token.token_type," : ",token.token_value)
	return node {}
}

func CheckSemiColon(t Token)bool{
	if t.token_type == "SEMI" {
		pc++
		return true
	}else {
		ShowError("Error : semicolon(;) excepted.")
		return false
	}
}

/*func GenExprInt(t Token) int{
	resault := 0

	
	if t.token_type == "NUMBER" {
		nums := [] int { }
		pc++
		t = pt[pc]

		for (t.token_type == "NUMBER" || t.token_type == "PLUS" || t.token_type == "MINUS") && pc < len(pt){
			if t.token_type == "NUMBER" {
				tmp := t.token_value

				num1,err := strconv.Atoi(tmp) 
				check(err)

				pc++
				t = pt[pc]

				if t.token_type == "PLUS" {
					pc++
					t = pt[pc]

					if t.token_type == "NUMBER"{

					}else {
						ShowError("Parser Error ")
					}
				}else if t.token_type == "MINUS" {
					pc++
					t = pt[pc]
				}
			}
		}
		
	}
	return resault
}*/
func ShowError(s1 string){
	fmt.Println(s1)
}