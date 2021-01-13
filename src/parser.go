package main

import (
	"fmt"
	"bufio"
	"os"
)
var index int = 0
var tokens = [] Token { }


type Variable struct {
	var_name string
	var_value string
	var_type string
}

var vars = [] Variable { }
func parse (toks []Token){
	tokens = toks

	for index < len(tokens) {
		switch(tokens[index].token_type){
			case "VAR":
				index++
				Var_Declare()
				index++
				break
			case "PRINT":
				index++
				Print_stmt()
				index++
				break
			case "PRINTLN":
				index++
				Print_stmt()
				index++
				break
			case "READSTR":
				index++
				Read_str()
				index++
				break
			case "READINT":
				index++
				Read_Int()
				index++
				break
			/*case "IF":
				index++
				if_stmt()
				index++
				break*/
			default :
				fmt.Println("Parse Error")
				
		}
		//index++
	}
}

func Var_Declare(){
	if tokens[index].token_type == "NAME" {
		name := tokens[index].token_value
		index++
		if tokens[index].token_type == "EQUAL" {
			index++
			if tokens[index].token_type == "NUMBER" {
				value := tokens[index].token_value
				index++
				if tokens[index].token_type == "SEMI" {
					vars = append(vars,Variable {name,value,"INT_VARIABLE"})
				}
				
			}else if tokens[index].token_type == "STRING" {
				value := tokens[index].token_value
				index++
				if tokens[index].token_type == "SEMI" {
					vars = append(vars,Variable {name,value,"STRING_VARIABLE"})
				}
			}
		}
	}else {
		fmt.Println("var declare error")
	}
}
func Print_stmt(){
	
	if tokens[index].token_type == "STRING" {
		value := string(tokens[index].token_value)
		index++

		if tokens[index].token_type == "SEMI" {
			fmt.Print(value)
		}
		

	}else if tokens[index].token_type == "NUMBER" {
		value := tokens[index].token_value
		index++

		if tokens[index].token_type == "SEMI" {
			fmt.Print(value)
		}
	}else if tokens[index].token_type == "NAME" {
		name := tokens[index].token_value
		index++
		if tokens[index].token_type == "SEMI" {
			a:=0
			for a < len(vars){
				if vars[a].var_name == name {
					fmt.Print(vars[a].var_value)
				}
				a++
			} 
			
		}
	}
	
}
/*func if_stmt(){
	var block_tokens = [] Token { }
	
	for tokens[index].token_type != "END" {
		block_tokens = append(block_tokens,tokens[index])
		index++
	}
	var cond string
	if GenCondition() != nil {
		cond = GenCondition()
		index++
		if tokens[index].token_type == "THEN" {
			if cond == "true" {
				parse()
			}else if cond == "Error" {
				ShowError("Error in if statement")
			}
		}else {
			ShowError("then expected.")
		}
		
	}
}*/
func Println_stmt(){
	
	if tokens[index].token_type == "STRING" {
		value := string(tokens[index].token_value)
		index++

		if tokens[index].token_type == "SEMI" {
			fmt.Println(value)
		}
		

	}else if tokens[index].token_type == "NUMBER" {
		value := tokens[index].token_value
		index++

		if tokens[index].token_type == "SEMI" {
			fmt.Println(value)
		}
	}else if tokens[index].token_type == "NAME" {
		name := tokens[index].token_value
		index++
		if tokens[index].token_type == "SEMI" {
			a:=0
			for a < len(vars){
				if vars[a].var_name == name {
					fmt.Println(vars[a].var_value)
				}
				a++
			} 
			
		}
	}
	
}

func Read_str(){
	if tokens[index].token_type == "NAME" {	
		name := tokens[index].token_value
		index++
		if tokens[index].token_type == "SEMI" {
			a:=0
			for a < len(vars){
				if vars[a].var_name == name  {
					if vars[a].var_type == "STRING_VARIABLE" {
						reader := bufio.NewReader(os.Stdin)
						temp_read, _ := reader.ReadString('\n')
						vars[a].var_value = temp_read
					}else {
						ShowError("ReadStr : Invalid arguemnt")
					}
					
				}
				a++
			} 
			
		}else {
			ShowError("Semicolon Error")
		}

	}else {
		ShowError("ReadStr : Invalid arguements")
	}
}

func Read_Int(){
	if tokens[index].token_type == "NAME" {	
		name := tokens[index].token_value
		index++
		if tokens[index].token_type == "SEMI" {
			a:=0
			for a < len(vars){
				if vars[a].var_name == name  {
					if vars[a].var_type == "INT_VARIABLE" {
						reader := bufio.NewReader(os.Stdin)
						temp_read, _ := reader.ReadString('\n')
						vars[a].var_value = temp_read
					}else {
						ShowError("ReadInt : Invalid arguemnt")
					}
					
				}
				a++
			} 
			
		}else {
			ShowError("Semicolon Error")
		}

	}else {
		ShowError("ReadInt : Invalid arguements")
	}
}
func GenExpr(){
	if tokens[index].token_type == "NAME" {

	}
}

/*func GenCondition() string {
	if tokens[index].token_type == "NAME" {
		name := tokens[index]
		index++
		if tokens[index].token_type == "EQUAL" {
			index++
			if tokens[index].token_type == "NAME" {
				name2 := tokens[index]
				if name.token_value == name2.token_value {
					return "true"
				}else {
					return "false"
				}

			}else if tokens[index].token_type == "NUMBER" {
				if name.token_value == tokens[index].token_value {
					return "true"
				}else {
					return "false"
				}
			}else if tokens[index].token_type == "STIRNG" {
				if name.token_value == tokens[index].token_value {
					return "true"
				}else {
					return "false"
				}
			}	
		}
	}

	return "Error"
}*/
func ShowError(s1 string){
	fmt.Println(s1)
}