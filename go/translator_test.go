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
