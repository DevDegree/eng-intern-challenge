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

func TestEnglishToBraille(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", "Hello", "Man!")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace(".....OO.OO..O..O..O.O.O.O.O.O.O..OO............OOO..O.O.....OO.OO...OOO.")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}

func TestBrailleToEnglish(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", "....OO....OOO..OO.")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace("-->")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}
