import { argv } from 'process';

// Collect arguments
const args = argv.slice(2);

if (args.length === 0) {
	console.log('Minimum: One argument required.');
} else {
	const text = args.join(' '); // Combine args into one string to account for English with spaces.

	// Initialize conversions between braille and characters
	const CAPITAL = '.....O';
	const DECIMAL = '.O...O';
	const NUMBER = '.O.OOO';
	const SPACE = '......';

	const brailleToLettersMap: { [key: string]: string } = {
		'O.....': 'a',
		'O.O...': 'b',
		'OO....': 'c',
		'OO.O..': 'd',
		'O..O..': 'e',
		'OOO...': 'f',
		'OOOO..': 'g',
		'O.OO..': 'h',
		'.OO...': 'i',
		'.OOO..': 'j',
		'O...O.': 'k',
		'O.O.O.': 'l',
		'OO..O.': 'm',
		'OO.OO.': 'n',
		'O..OO.': 'o',
		'OOO.O.': 'p',
		'OOOOO.': 'q',
		'O.OOO.': 'r',
		'.OO.O.': 's',
		'.OOOO.': 't',
		'O...OO': 'u',
		'O.O.OO': 'v',
		'.OOO.O': 'w',
		'OO..OO': 'x',
		'OO.OOO': 'y',
		'O..OOO': 'z',
		'..OO.O': '.',
		'..O...': ',',
		'..O.OO': '?',
		'..OOO.': '!',
		'..OO..': ':',
		'..O.O.': ';',
		'....OO': '-',
		'.O..O.': '/',
		'.OO..O': '<',
		// 'O..OO.': '>', // Duplicate symbol with 'o', not sure how to handle
		'O.O..O': '(',
		'.O.OO.': ')',
	};

	const lettersToBrailleMap: { [key: string]: string } = {};
	for (const [key, value] of Object.entries(brailleToLettersMap)) {
		lettersToBrailleMap[value] = key;
	}

	const brailleToNumbersMap: { [key: string]: string } = {
		'O.....': '1',
		'O.O...': '2',
		'OO....': '3',
		'OO.O..': '4',
		'O..O..': '5',
		'OOO...': '6',
		'OOOO..': '7',
		'O.OO..': '8',
		'.OO...': '9',
		'.OOO..': '0',
	};

	const numbersToBrailleMap: { [key: string]: string } = {};
	for (const [key, value] of Object.entries(brailleToNumbersMap)) {
		numbersToBrailleMap[value] = key;
	}

	// If the text only contains .'s and O's, and is divisible by 6, then assume it is braille
	const braillePattern = /^[O\.]+$/;
	let isBraille = text.length % 6 === 0 && braillePattern.test(text);

	if (isBraille) {
		let outputText = '';

		let capitalNext = false;
		let numberNext = false;

		for (let i = 0; i < text.length; i += 6) {
			// Take 6 characters at a time
			const brailleChar = text.slice(i, i + 6);

			if (brailleChar === CAPITAL) {
				// Capitalize the next character
				capitalNext = true;
			} else if (brailleChar === DECIMAL) {
				// Insert a decimal point
				outputText += '.';
			} else if (brailleChar === NUMBER) {
				// Use numbers for the next character
				numberNext = true;
			} else if (brailleChar === SPACE) {
				// Insert a space and use letters for the next character
				numberNext = false;
				outputText += ' ';
			} else {
				// Select the character based on whether the next character is a number or not
				let englishChar = numberNext
					? brailleToNumbersMap[brailleChar]
					: brailleToLettersMap[brailleChar];

				// Capitalize the character and set the next character to be un-capitalized
				if (capitalNext) {
					englishChar = englishChar.toUpperCase();
					capitalNext = false;
				}

				// Add the english character to the output text
				outputText += englishChar;
			}
		}

		// Print the english translation
		console.log(outputText);
	} else {
		let outputText = '';

		// Use this variable to know when we need to add the number follows braille symbol
		let prevCharIsNumber = false;

		for (let i = 0; i < text.length; i++) {
			// Take 1 character at a time
			const englishChar = text[i];

			if (englishChar >= '0' && englishChar <= '9') {
				// If previous character was not a number, and the current character is,
				// add the number follows braille symbol.
				if (!prevCharIsNumber) {
					outputText += NUMBER;
				}

				// Insert braille number
				outputText += numbersToBrailleMap[englishChar];

				prevCharIsNumber = true;
			} else if (englishChar === '.') {
				// Check if the '.' is a period of a decimal point
				// If the '.' is preceded and suceeded by numbers, then it is a decimal point, otherwise
				// it is a period
				if (prevCharIsNumber && i < text.length - 1) {
					const nextEnglishChar = text[i + 1];

					if (nextEnglishChar >= '0' && nextEnglishChar <= '9') {
						outputText += DECIMAL;
					}
				} else {
					outputText += lettersToBrailleMap['.'];
				}
			} else if (englishChar === ' ') {
				// Insert braille space and make note that the last character is not a number
				prevCharIsNumber = false;
				outputText += SPACE;
			} else {
				// Select the braille char
				const brailleChar = lettersToBrailleMap[englishChar.toLowerCase()];

				// Add the capital braille symbol if the character is capitalized
				if (englishChar >= 'A' && englishChar <= 'Z') {
					outputText += CAPITAL;
				}

				// Insert braille letter
				outputText += brailleChar;
			}
		}

		// Print the braille translation
		console.log(outputText);
	}
}
