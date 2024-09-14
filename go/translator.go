package main

import (
	"fmt"
	"log"
	"os"
	"solution/helpers"
	"solution/lib"
	"solution/mappers"
	"strings"
)

/*
Some questions I had to answer:
Due to the technical requirement:
When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
I am to assume
- numbers will only ever be in the format 123 or 123.123
- no double spaces such as "123 123  123" as one of the spaces would be included in the numbers
- braille and english cannot be mixed
	* input will either be all english or all braille
- I should not assume braille is put in quotes (to stop '.' as being interpreted differently)
*/

func main() {
	// assuming an argument will always be provided
	// as no information was given on what to do in such a case
	// panic is good since this is undefined behavior
	argsWithoutProg := os.Args[1:]
	var translatedWords []string
	for _, word := range argsWithoutProg {
		translation, err := lib.Translate(word)
		if err != nil {
			log.Printf("[ERROR] Could not translate %s, got %v", word, err)
		}
		translatedWords = append(translatedWords, translation)
	}
	space := " "
	if helpers.IsBraille(translatedWords[0]) {
		space = mappers.BRAILLE_SPACE
	}
	finalTranslation := strings.Join(translatedWords, space)
	fmt.Printf("%s", finalTranslation)

}
