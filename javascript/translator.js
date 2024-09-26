/* 
Requirements -> Braille Alphabet: Letters a through z/ The ability to capitalize letters/ Numbers 0 through 9/ The ability to include spaces ie: multiple words

Function 1. check if the input is either English or Braille (if it's English then translate it to Braille, if it's Braille then translate it to English)
Function 2. translate Braille to English
Function 3. translate English to Braille 
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
		"capital": ".....O", "number": ".O.OOO", "decimal": ".O...O", "space": "......"
	},
	"specialChar": {
		".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
		";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
		"(": "O.O..O", ")": ".O.OO."
	},
};

// Check if the input is Braille
function isBraille(input) {
	return input.length >= 6 && /^[0\.]+$/.test(input);
}


// Function to translate the input, Braille to English
function brailleToEnglish(input) {
	let result = ''; // result is string
	let isNumber = false; // indicator for number setting
	let isCapital = false;  // indicator for capitalization

  const brailleChars = text.match(/.{1,6}/g); // Split the input into groups of 6 characters 

	for (let char of input) {
		if (char === brailleDictionary.indicators.capital) {
			isCapital = true;
		}	else if (char === brailleDictionary.indicators.number) {
			isCapital = true;
		}	else if (char === brailleDictionary.indicators.decimal) {
			result += ".";
		} else {}
	}

}






// Function to translate the input, English to Braille
function englishToBraille(input) {
	let result = ''; // result is string
	let isNumber = false;

	for (let char of input) { // iterates over characters of the input
		if (char >= 'A' && char <= 'Z') { // checks if the first letter is capital
		  result += brailleDictionary.indicators.capital;
			result += brailleDictionary.alphabets[char.toLowerCase()]; 
			isNumber = false;
		} else if (char >= 'a' && char <= 'z') { // lower case
			result += brailleDictionary.alphabets[char];
			isNumber = false;
		} else if (char >= '0' && char <= '9') { 
			if (!isNumber) {
				result += brailleDictionary.indicators.number; // indicate number mode
				isNumber = true;
			}
			result += brailleDictionary.numbers[char]; 
		} else if (char === '.') {
			result += isNumber ? brailleDictionary.indicators.decimal : brailleDictionary.specialChar[char]; // checks if the period is period or decimal
		} else if (char === ' ') { // checks spacing
			result += brailleDictionary.indicators["space"];
			isNumber = false;
		} else if (brailleDictionary.specialChar[char]) { // checks special charactoers
			result += brailleDictionary.specialChar[char];
			isNumber = false;
		}
	}
	return result;
}
function translate(input) {
	if (isBraille(input)) {
		return brailleToEnglish(input);
	} else {
		return englishToBraille(input);
	}
}

// Reading input from command line arguments
const input = process.argv.slice(2).join(' ');

// Output the translation
console.log(translate(input));