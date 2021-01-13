package main

import (
	"unicode"
)
type Scanner struct {
	src string
}

func (s *Scanner) scan(src []rune) []Token {
	result := []Token{}
	pos := 0
	for pos < len(src) {
		temp := ""
		for pos < len(src) && unicode.IsSpace(src[pos]) { pos++ }
		/*if  string(src[pos]) == "#" { 
			pos++ 
			for pos < len(src) && string(src[pos]) != "\n"{pos++}
		}*/
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
			case "else":
				result = append(result, Token{ "THEN", temp })
			case "end":
				result = append(result, Token{ "END", temp })
			case "for":
				result = append(result, Token{ "FOR", temp })
			case "do":
				result = append(result, Token{ "DO", temp })
			case "function":
				result = append(result, Token{ "FUNCTION", temp })
			case "use":
				result = append(result, Token{ "USE", temp })		
			case "int":
				result = append(result, Token{ "INTVAR", temp })
			case "string":
				result = append(result, Token{ "STRVAR", temp })
			case "bool":
				result = append(result, Token{ "BOOLVAR", temp })	
			case "float":
				result = append(result, Token{ "FLOATVAR", temp })
			case "char":
				result = append(result, Token{ "CHARVAR", temp })
			case "double":
				result = append(result, Token{ "DOUBLEVAR", temp })
			case "long":
				result = append(result, Token{ "LONGVAR", temp })
			case "array":
				result = append(result, Token{ "ARRAYVAR", temp })
			case "as":
				result = append(result, Token{ "AS", temp })
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
