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

func TestSolutionOutputTwo(t *testing.T) {
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

func TestTranslateToBrailleAlphabet(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", "Hello world")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}

func TestTranslateToEnglish(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace("Abc 123 xYz")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}

func TestTranslateToBrailleNumber(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", "42")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace(".O.OOOOO.O..O.O...")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}

func TestTranslateToEnglishTwo(t *testing.T) {
	cmd := exec.Command("go", "run", "translator.go", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace("Abc 123")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}
