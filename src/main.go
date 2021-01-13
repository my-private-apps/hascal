/*
	Hascal Programming Language  --- v1.2
	Copyiright (c) 2019-2020 Hascal Development Team, all rights reserved.
*/
package main

import (
	"os"
	"io/ioutil"
	"fmt"
)

var source string 
func main() {
	if len(os.Args) == 1 || len(os.Args) > 2 {
		fmt.Println("Hascal : No such file or directory.\nusage : hascal <input_file>")
		os.Exit(0)
	}else {
		input_file_name := os.Args[1]

		// Open File
		file, err := ioutil.ReadFile(input_file_name)
    	check(err)
		source = string(file)

		Hascal(source)
		os.Exit(0)
	}
}
func Hascal(src string){
	var s Scanner
	var p Parser

	// Tokenize source
	tokens := s.scan([]rune(source))

	// Parse source and create AST
	tree := p.parse(tokens)
	
	// run source
	interpreter(node(tree))
}
func check(e error) {
    if e != nil {
        panic(e)
    }
}
