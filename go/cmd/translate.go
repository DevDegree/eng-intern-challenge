package cmd

import (
	"fmt"
	"os"
	"regexp"

	"github.com/spf13/cobra"
	"solution/pkg/translator"
)

var rootCmd = &cobra.Command{
	Use:   "translator",
	Short: "Translator is a tool to translate between text and braille",
	Run: func(cmd *cobra.Command, args []string) {
		translator := translator.NewTranslator(isBraille(args))

		output, err := translator.Translate(args)
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}

		fmt.Println(output)
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func isBraille(args []string) bool {
	exp := regexp.MustCompile(`^[.O]+$`)
	return len(args) == 1 && exp.MatchString(args[0])
}
