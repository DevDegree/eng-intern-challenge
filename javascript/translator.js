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
	"specialChars": {
		".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
		";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
		"(": "O.O..O", ")": ".O.OO."
	},
};

// Check if the input is Braille
function isBraille(input) {
	return input.length >= 6 && /^[O\.]+$/.test(input);
}


// Function to translate Braille to English
function brailleToEnglish(input) {
  const brailleChars = input.match(/.{1,6}/g); // Split Braille string into chunks of 6 characters
  let result = ''; // output is a string
  let isCapital = false;
  let isNumber = false;

  brailleChars.forEach(brailleChar => { // loop through each Braille Character in the brailleChars array
    if(brailleChar === brailleDictionary.indicators.capital) { // checks the current char matches the capital indicator
      isCapital = true;
    } else if (brailleChar === brailleDictionary.indicators.number) { // checks the current char matches the number indicator
      isNumber = true;
    } else if (brailleChar === brailleDictionary.indicators.decimal) { // checks the current char matches the decimal indicator
			result += '.';
		} else if(brailleChar === brailleDictionary.indicators.space) { // checks the current char matches the space indicator
      result += ' ';
      isCapital = false;
      isNumber = false; // space resets the number mode to false
    } else { // if none of the conditions(indicator) above are met 
      if (isNumber) { // if the current brailleChar is a number, look for the maching Braille charactor in the numbers object
        const num = Object.keys(brailleDictionary.numbers).find(key => brailleDictionary.numbers[key] === brailleChar);
        if (num) { // if a match is found then add it to the result string
          result += num;
        }
      } else { // if the current brailleChar is an alphabet, look for the matching Braille char in the alphabets object
        let isExist = false;
        const alphabet = Object.keys(brailleDictionary.alphabets).find(key => brailleDictionary.alphabets[key] === brailleChar);
        if (alphabet) { // if a match is found then add it to the result string
          result += isCapital ? alphabet.toUpperCase() : alphabet; // checks if the matching char is capitalized or not
          isExist = true;
        }

        if (!isExist) { // if no alphabet was found then check for a match in the specialChars object.
          const specialChar = Object.keys(brailleDictionary.specialChars).find(key => brailleDictionary.specialChars[key] === brailleChar);
          if (specialChar) {
            result += specialChar;
          }
        }
        isCapital = false; // reset the capital indicator to false for the next Braille Character
      }
   
    }

  });
  
  return result;
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
			result += isNumber ? brailleDictionary.indicators.decimal : brailleDictionary.specialChars[char]; // checks if the period is period or decimal
		} else if (char === ' ') { // checks spacing
			result += brailleDictionary.indicators["space"];
			isNumber = false;
		} else if (brailleDictionary.specialChars[char]) { // checks special charactoers
			result += brailleDictionary.specialChars[char];
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

// Read input from command line arguments
const input = process.argv.slice(2).join(' ');

// Output the translation
console.log(translate(input));