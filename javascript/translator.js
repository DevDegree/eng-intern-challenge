const DIC_BRAILLE = {
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
	"punctuations": {
		".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
		";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
		"(": "O.O..O", ")": ".O.OO.", " ": "......"
	},
	"prefixes": {
		"capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"
	}
};

function isBraille(input) {
	return input.length >= 6 && /^[O\.]+$/.test(input);
}

function englishToBraille(text) {
	let result = '';
	let isNumberMode = false;

	for (let i = 0; i < text.length; i++) {
		let char = text[i];

		if (char >= 'A' && char <= 'Z') {
			result += DIC_BRAILLE.prefixes.capital;
			result += DIC_BRAILLE.alphabets[char.toLowerCase()];
			isNumberMode = false;
		} else if (char >= 'a' && char <= 'z') {
			result += DIC_BRAILLE.alphabets[char];
			isNumberMode = false;
		} else if (char >= '0' && char <= '9') {
			if (!isNumberMode) {
				result += DIC_BRAILLE.prefixes.number;
				isNumberMode = true;
			}
			result += DIC_BRAILLE.numbers[char];
		} else if (char === '.') {
			// If it's a decimal point and in number mode, add the decimal prefix
			if (isNumberMode) {
				result += DIC_BRAILLE.prefixes.decimal;
			} else {
				// Otherwise, use the punctuation for a period
				result += DIC_BRAILLE.punctuations[char];
			}
		} else if (DIC_BRAILLE.punctuations[char]) {
			result += DIC_BRAILLE.punctuations[char];
			isNumberMode = false;
		} else if (char === ' ') {
			result += DIC_BRAILLE.punctuations[" "];
			isNumberMode = false;
		}
	}

	return result;
}

function brailleToEnglish(input) {
	const words = input.match(/.{1,6}/g); // Split Braille string every 6 characters
	let result = '';
	let isCapital = false;
	let isNumber = false;

	for (let word of words) {
		if (word === DIC_BRAILLE.prefixes.capital) {
			isCapital = true;
		} else if (word === DIC_BRAILLE.prefixes.number) {
			isNumber = true;
		} else if (word === DIC_BRAILLE.prefixes.decimal) {
			result += '.';
		} else {
			if (isNumber) {
				for (let [digit, brailleCode] of Object.entries(DIC_BRAILLE.numbers)) {
					if (brailleCode === word) {
						result += digit;
						break;
					}
				}
			} else {
				let found = false;
				for (let [letter, brailleCode] of Object.entries(DIC_BRAILLE.alphabets)) {
					if (brailleCode === word) {
						result += isCapital ? letter.toUpperCase() : letter;
						found = true;
						break;
					}
				}
				if (!found) {
					for (let [punctuation, brailleCode] of Object.entries(DIC_BRAILLE.punctuations)) {
						if (brailleCode === word) {
							result += punctuation;
							break;
						}
					}
				}
				isCapital = false;
			}
		}

		// Continue number mode unless a space or other termination is encountered
		if (word === DIC_BRAILLE.punctuations[" "]) {
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