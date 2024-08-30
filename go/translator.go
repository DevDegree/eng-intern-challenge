package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
)

var ErrMissingArguments = errors.New("missing required cli arguments")

// processes arguments, joins them together, and removes leading/trailing whitespace
func handleArguments() (string, error) {
	if len(os.Args) < 2 {
		return "", ErrMissingArguments
	}
	args := os.Args[1:]
	return strings.TrimSpace(strings.Join(args, " ")), nil
}

func main() {
	text, err := handleArguments()

	if err != nil {
		log.Fatalf("invalid args: %s\n", err)
	}

	fmt.Println(text)
}
