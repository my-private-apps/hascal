package main

import (
	"unicode"
)

type Token struct {
	token_type string
	token_value string
}

func scan(src []rune) []Token {
	result := []Token{}
	pos := 0
	for pos < len(src) {
		temp := ""
		for pos < len(src) && unicode.IsSpace(src[pos]) { pos++ }
		for pos < len(src) && unicode.IsNumber(src[pos]) {
			temp += string(src[pos])
			pos++
		}
		if temp != "" {
			result = append(result, Token{ "NUMBER", temp })
			temp = ""
		}
		for pos < len(src) && unicode.IsLetter(src[pos]) {
			temp += string(src[pos])
			pos++
		}
		if temp != "" {
			switch(temp){
			case "var":
				result = append(result, Token{ "VAR", temp })
			case "print":
				result = append(result, Token{ "PRINT", temp })
			case "println":
				result = append(result, Token{ "PRINTLN", temp })
			case "ReadStr":
				result = append(result, Token{ "READSTR", temp })
			case "ReadInt":
				result = append(result, Token{ "READINT", temp })
			case "if":
				result = append(result, Token{ "IF", temp })
			case "then":
				result = append(result, Token{ "THEN", temp })
			case "end":
				result = append(result, Token{ "END", temp })
			default :
				result = append(result, Token{ "NAME", temp })
			}
			//result = append(result, Token{ "NAME", temp })
			temp = ""
		}
		if pos < len(src) && src[pos] == ';'{
			pos++
			result = append(result, Token{ "SEMI", ";" })
		}
		if pos < len(src) && src[pos] == '='{
			pos++
			result = append(result, Token{ "EQUAL", "=" })
		}
		if pos < len(src) && src[pos] == '"' {
			pos++
			for pos < len(src) && (src[pos] != '"' || src[pos-1] == '\\') {
				temp += string(src[pos])
				pos++
			}
			pos++
			result = append(result, Token{ "STRING", temp })
			temp = ""
		}
	}
	return result
}
