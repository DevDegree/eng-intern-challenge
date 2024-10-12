#!/bin/bash

# Test Script for Braille Translator

# Path to the translator program
TRANSLATOR="python3 translator.py"

# Function to run a test case
run_test() {
    input="$1"
    expected_output="$2"
    description="$3"

    echo "Test: $description"
    echo "Input: $input"

    # Run the translator program and capture the output
    output=$($TRANSLATOR "$input")

    echo "Output: $output"
    echo "Expected Output: $expected_output"

    if [ "$output" = "$expected_output" ]; then
        echo "Result: PASS"
    else
        echo "Result: FAIL"
    fi

    echo "-------------------------------"
}

# Start of Test Cases

echo "Starting Tests for Braille Translator"
echo "======================================"

# Simple Test Cases

# Test 1: Empty Input
run_test "" "" "Empty Input"

# Test 2: Single Lowercase Letter
run_test "a" "O....." "Single lowercase letter"

# Test 3: Single Uppercase Letter
run_test "A" ".....OO" "Single uppercase letter"

# Test 4: Single Digit Number
run_test "5" ".O.OOOO.." "Single digit number"

# Test 5: Space Character
run_test " " "......" "Space character"

# Test 6: Simple Word
run_test "cat" "OO....O.....OO...." "Simple word 'cat'"

# Test 7: Braille to English (Single Letter)
run_test "O....." "a" "Braille 'O.....' to English"

# Intermediate Test Cases

# Test 8: Word with Mixed Case
run_test "HeLLo" ".....OO.OO..O..O..O.O." "Word with mixed case 'HeLLo'"

# Test 9: Number Sequence
run_test "123" ".O.OOOO.....O.O...OO...." "Number sequence '123'"

# Test 10: Sentence with Space
run_test "hi there" "O.OO...OO.... ......O..O..O.OO..O..O.O..." "Sentence 'hi there'"

# Complex Test Cases

# Test 11: Full Sentence with Capitals and Numbers
input11="Hello World 42"
expected_output11=".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O...O.OOO...O......O.OOOOO.O..O.O..."
run_test "$input11" "$expected_output11" "Sentence with capitals and numbers"

# Test 12: Braille to English (Complex)
input12=".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O...O.OOO...O......O.OOOOO.O..O.O..."
expected_output12="Hello World 42"
run_test "$input12" "$expected_output12" "Braille to English (complex input)"

# Test 13: Complex Braille Input with Capital and Number Indicators
input13=".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
expected_output13="Abc 123"
run_test "$input13" "$expected_output13" "Braille input 'Abc 123'"

# Test 14: Unsupported Characters (Should be Ignored)
run_test "Hello, World!" ".....OO.OO..O..O..O.O.O......OOOOO.O.OO..O...OOO.O..." "Input with unsupported characters"

# Test 15: Long Text Input
input15="The quick brown fox jumps over the lazy dog 9876543210"
expected_output15=".....O.O...OOOO...O.OO...O..OOO......OOO...OO....OOOOO...OO....O.OO...OO.OO......OO....OO.OO.O.OO..O......O..OOO.OO.O...OOO...O.OO...OO......O.O.OO.O..OO...O.OOOO.O......O..OOO...O.OO..OO.OO..O.OO...OO....O.OOO......O.OO...O...OO....O..O..OO.OOOO.....O.O...OO....OOO...OOO...OOO...OOOOO...OOOOO...OOOOO..."
run_test "$input15" "$expected_output15" "Long text input"

echo "All tests completed."