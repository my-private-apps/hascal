package main

import (
	"fmt"
	"log"
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

	// var x = 0;
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
					pc++
					token = pt[pc]

					if token.token_type == "SEMI" {
						pc++
						return node{
							kind:  "IntVariable",
							name: temp_name,
							value : token.token_value,
						}
					}else {
						ShowError("Error : semicolon excepted.")
					}
					
				}

			}
			
		}else {
			log.Fatal(token.token_type)
		}
		
	}

	if token.token_type == "PRINT" {
		pc++
		token = pt[pc]

		if token.token_type == "NAME" {
			temp_name := token.token_value
			pc++

			token = pt[pc]

			if token.token_type == "SEMI" {
				pc++
				return node{
					kind: "PrintStmt_Name",
					name : temp_name,
				}
			} 
			
		}else if token.token_type == "NUMBER" {
			num := token.token_value
			pc++
			token = pt[pc]
			
			if token.token_type == "SEMI" {
				pc++
				return node{
					kind: "PrintStmt_Number",
					value : num,
				}
			}
		}
	}

	log.Fatal(token.token_type)
	return node {}
}


func ShowError(s1 string){
	fmt.Println(s1)
}