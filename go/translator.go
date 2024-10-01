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

func main() {
	// assuming an argument will always be provided
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
