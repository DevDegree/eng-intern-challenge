package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

var braillePattern = regexp.MustCompile("(?m)^[O.]*$")

func main() {
	if len(os.Args) < 2 {
		return
	}
	if isBraille(os.Args[1]) {
		english, err := decode(strings.Join(os.Args[1:], ""))
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(english)
	} else { // Input is English.
		braille, err := encode(strings.Join(os.Args[1:], " "))
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(braille)
	}
}

// isBraille returns true if str is a valid Braille string. A valid Braille string
// contains only 'O' (uppercase letter O), and '.' (period) characters.
func isBraille(str string) bool {
	return braillePattern.MatchString(str)
}

// decode converts a Braille string to English. braille must contain only 'O' (uppercase
// letter O), and '.' (period) characters.
func decode(braille string) (string, error) {
	// TODO
	return "", nil
}

// encode converts an English string to Braille. english must contain only a-z, A-Z, 0-9,
// and ' ' (space) characters. If english contains any other characters, encode returns
// ErrInvalidChar.
func encode(english string) (string, error) {
	// TODO
	return "", nil
}
