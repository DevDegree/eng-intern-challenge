/* 
Requirements -> Braille Alphabet: Letters a through z/ The ability to capitalize letters/ Numbers 0 through 9/ The ability to include spaces ie: multiple words

Function 1. check if the input is either English or Braille (if it's English then translate it to Braille, if it's Braille then translate it to English)
Function 2. translate English to Braille 
    - a. loop through each characters in the content
    - b. check if the first letter is capital or not (if yes, then ADD prefix Capital) AND next letter should be lowercase
    - c. number = false

Print the output
*/

const brailleDictionary = {
	"alphabets": {
		"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
		"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
		"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
		"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
		"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
		"z": "O..OOO"
	},
	"numbers": {
		"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
		"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
	},
	"indicators": {
		"capital": ".....O", "number": ".O.OOO", "decimal": ".O...O", " ": "......"
	}
};

// Check if the input is Braille or not
function isBraille(input) {
	return input.length >= 6 && /^[0\.]+$/.test(input);
}

// Function to translate the input, English to Braille

