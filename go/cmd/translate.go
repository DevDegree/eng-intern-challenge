package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "translator",
	Short: "Translator is a tool to translate between text and braille",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println(args)
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
