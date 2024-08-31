const ENGLISH_TO_BRAILLE_DICTIONARY = {
	'a': 'O.....',
	'b': 'O.O...',
	'c': 'OO....',
	'd': 'OO.O..',
	'e': 'O..O..',
	'f': 'OOO...',
	'g': 'OOOO..',
	'h': 'O.OO..',
	'i': '.OO...',
	'j': '.OOO..',
	'k': 'O...O.',
	'l': 'O.O.O.',
	'm': 'OO..O.',
	'n': 'OO.OO.',
	'o': 'O..OO.',
	'p': 'OOO.O.',
	'q': 'OOOOO.',
	'r': 'O.OOO.',
	's': '.OO.O.',
	't': '.OOOO.',
	'u': 'O...OO',
	'v': 'O.O.OO',
	'w': '.OOO.O',
	'x': 'OO..OO',
	'y': 'OO.OOO',
	'z': 'O..OOO',
	'capital': '.....O',
	'number': '.O.OOO',
	' ': '......',
};

const ENGLISH_TO_BRAILLE_NUM = {
	'0': '.OOO..',
	'1': 'O.....',
	'2': 'O.O...',
	'3': 'OO....',
	'4': 'OO.O..',
	'5': 'O..O..',
	'6': 'OOO...',
	'7': 'OOOO..',
	'8': 'O.OO..',
	'9': '.OO...',
};

const BRAILLE_TO_ENGLISH_DICTIONARY = {
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
	'.....O': 'capital',
	'.O.OOO': 'number',
	'......': ' ',
};

const BRAILLE_TO_ENGLISH_NUM = {
	'.OOO..': '0',
	'O.....': '1',
	'O.O...': '2',
	'OO....': '3',
	'OO.O..': '4',
	'O..O..': '5',
	'OOO...': '6',
	'OOOO..': '7',
	'O.OO..': '8',
	'.OO...': '9',
};

function main(inputString) {
	const translatedString = inputString.includes('.')
		? translateBrailleToEnglish(inputString)
		: translateEnglishToBraille(inputString);
	return translatedString;
}

function translateBrailleToEnglish(brailleString) {
	let englishString = '';
	let isNumber = false;
	for (let i = 0; i < brailleString.length; i += 6) {
		let currentBrailleCell = brailleString.slice(i, i + 6);

		if (currentBrailleCell === ENGLISH_TO_BRAILLE_DICTIONARY['capital']) {
			i += 6;
			currentBrailleCell = brailleString.slice(i, i + 6);
			englishString +=
				BRAILLE_TO_ENGLISH_DICTIONARY[currentBrailleCell].toUpperCase();
		} else if (
			currentBrailleCell === ENGLISH_TO_BRAILLE_DICTIONARY['number']
		) {
			isNumber = true;
			i += 6;
			currentBrailleCell = brailleString.slice(i, i + 6);

			while (isNumber && i < brailleString.length) {
				if (!(currentBrailleCell === ENGLISH_TO_BRAILLE_DICTIONARY[' '])) {
					englishString += BRAILLE_TO_ENGLISH_NUM[currentBrailleCell];
					i += 6;
					currentBrailleCell = brailleString.slice(i, i + 6);
				} else {
					isNumber = false;
					englishString += BRAILLE_TO_ENGLISH_DICTIONARY[currentBrailleCell];
				}
			}
		} else {
			englishString += BRAILLE_TO_ENGLISH_DICTIONARY[currentBrailleCell];
		}
	}

	return englishString;
}

function translateEnglishToBraille(englishString) {
	let brailleString = '';

	for (let i = 0; i < englishString.length; i++) {
		if (englishString[i] === englishString[i].toUpperCase() && !(/\d/.test(englishString[i])) && englishString[i] != ' ') {
			brailleString += ENGLISH_TO_BRAILLE_DICTIONARY['capital'];
			brailleString += ENGLISH_TO_BRAILLE_DICTIONARY[englishString[i].toLowerCase()];
		} else if (/\d/.test(englishString[i])) {
			brailleString += ENGLISH_TO_BRAILLE_DICTIONARY['number'];
			while (englishString[i] !== ' ' && i < englishString.length) {
				brailleString += ENGLISH_TO_BRAILLE_NUM[englishString[i]];
				i++;
			}
            if(englishString[i]===" "){
                brailleString+=ENGLISH_TO_BRAILLE_DICTIONARY[englishString[i]];
            }
		} else {
			brailleString += ENGLISH_TO_BRAILLE_DICTIONARY[englishString[i]];
		}
	}
	return brailleString;
}

const commandLineInput = process.argv.splice(2);
console.log(main(commandLineInput.join(' ')));
