package main

import (
	"os/exec"
	"strings"
	"testing"
)

func TestSolutionOutput(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", "Abc", "123", "xYz")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}

func TestTranslator(t *testing.T) {
	tests := []struct {
		input    string
		expected string
	}{
		{input: "Hello world", expected: ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."},
		{input: ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", expected: "Hello world"},

		{input: "42", expected: ".O.OOOOO.O..O.O..."},
		{input: ".O.OOOOO.O..O.O...", expected: "42"},

		{input: "Abc 123", expected: ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."},
		{input: ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", expected: "Abc 123"},

		{input: "1", expected: ".O...OO....."},
		{input: ".O...OO.....", expected: "1"},
		{input: ".O.OOOO.....", expected: "1"},

		{input: "x5", expected: "OO..OO.O...OO..O.."},
		{input: "OO..OO.O...OO..O..", expected: "x5"},

		{input: "6f", expected: ".O...OOOO...OOO..."},
		{input: ".O...OOOO...OOO...", expected: "6f"},

		{input: "78g", expected: ".O...OOOOO...O...OO.OO..OOOO.."},
		{input: ".O...OOOOO...O...OO.OO..OOOO..", expected: "78g"},

		{input: "90g456", expected: ".O...O.OO....O...O.OOO..OOOO...O.OOOOO.O..O..O..OOO..."},
		{input: ".O...O.OO....O...O.OOO..OOOO...O.OOOOO.O..O..O..OOO...", expected: "90g456"},
	}

	for _, test := range tests {
		cmd := exec.Command("go", append([]string{"run", "translator.go"}, strings.Split(test.input, " ")...)...)
		outputBytes, err := cmd.CombinedOutput()
		if err != nil {
			t.Fatalf("Failed to run the command: %v", err)
		}

		// Trim space from output and expected value
		actual := strings.TrimSpace(string(outputBytes))

		if actual != test.expected {
			t.Errorf("Unexpected output for input %s, got: %q, want: %q", test.input, actual, test.expected)
		}
	}
}
