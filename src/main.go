/*
	Hascal Programming Language  --- v1.2
	Copyiright (c) 2019-2020 Hascal Development Team, all rights reserved.
*/
package main

import (
	"os"
	"io/ioutil"
)

var source string 
func main() {
	input_file_name := os.Args[1]

	// Open File
	file, err := ioutil.ReadFile(input_file_name)
    check(err)
	source = string(file)

	// Tokenize source
	tokens := scan([]rune(source))

	// Parse and run source
	parse(tokens)
	os.Exit(0)
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}
