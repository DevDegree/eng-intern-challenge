#!/bin/bash

#How to call the program properly
TRANSLATOR="ruby translator.rb"

#Testing function
test_translation() {
	local input="$1"
	local expected_output="$2"

	local output="$($TRANSLATOR "$input")"

	if [[ "$output" == "$expected_output" ]]; then
		echo "PASS"
	else
		echo -e "FAIL:\nExpected: '$expected_output'\nActual: '$output'\n"
	fi
}

#Given test cases
test_translation "Hello world" .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
test_translation .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.. "Hello world"
test_translation .O.OOOOO.O..O.O... 42
test_translation 42 .O.OOOOO.O..O.O...
test_translation .....OO.....O.O...OO...........O.OOOO.....O.O...OO.... "Abc 123"
test_translation "Abc 123" .....OO.....O.O...OO...........O.OOOO.....O.O...OO....

#Testing for every possible letter
test_translation "abcdefghijklmnopqrstuvwxyz" "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"
test_translation "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO" "abcdefghijklmnopqrstuvwxyz"

#Testing for every possible number
test_translation "1234567890" ".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO.."
test_translation ".O.OOOO.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO.." "1234567890"

#Testing for every possible special character
test_translation ".,?!:;-/<() " "..OO.O..O.....O.OO..OOO...OO....O.O.....OO.O..O..OO..OO.O..O.O.OO......."
test_translation "..OO.O..O.....O.OO..OOO...OO....O.O.....OO.O..O..OO..OO.O..O.O.OO......." ".,?!:;-/<() "

#Random string with number, capitals and special characters
test_translation "ACLs4  34 52  aad--66" ".....OO..........OOO.........OO.O.O..OO.O..O.OOOOO.O...............O.OOOOO....OO.O.........O.OOOO..O..O.O...............O.....O.....OO.O......OO....OO.O.OOOOOO...OOO..."
test_translation ".....OO..........OOO.........OO.O.O..OO.O..O.OOOOO.O...............O.OOOOO....OO.O.........O.OOOO..O..O.O...............O.....O.....OO.O......OO....OO.O.OOOOOO...OOO..." "ACLs4  34 52  aad--66"

echo "All tests complete"
