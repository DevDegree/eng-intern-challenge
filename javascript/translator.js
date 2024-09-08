// map from English to Braille
// excludes punctuation and decimal (not in requirements)
const brailleMap = {
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

// map from number to Braille
const numberMap = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
};

// reverse the keys and values of brailleMap and numberMap for Braille to English translation
const reverseBraille = Object.fromEntries(Object.entries(brailleMap).map(([a, b]) => [b, a]));
const reverseNumbers = Object.fromEntries(Object.entries(numberMap).map(([a, b]) => [b, a]));

//check if input string is braille
const isBraille = (str) => {
	return /^[O.]+$/.test(str);
};

// takes braille input and translates to english
const brailleToEnglish = (str) => {
	// split input string into braille characters
	const braille = str.match(/.{1,6}/g);
	var engStr = '';
	var isNumber = false;

	for (let i = 0; i < braille.length; i++) {
		if (braille[i] === brailleMap[' ']) {
			engStr += ' ';
			// invalidate 'number follows' after space symbol
			isNumber = false;
			continue;
		}
		if (braille[i] === brailleMap['number']) {
			isNumber = true;
			continue;
		}
		// use upper case for letter after 'capital follows' symbol
		if (braille[i] === brailleMap['capital']) {
			engStr += reverseBraille[braille[i+1]].toUpperCase() || '';
			i++;
			continue;
		}
		// add current number/letter to output string
		engStr += isNumber ? (reverseNumbers[braille[i]] || '') : (reverseBraille[braille[i]] || '');
	}

	return engStr;
};

// takes english input and translates to braille
const englishToBraille = (str) => {
	var brailleStr = '';
	var isNumber = false;

	for(let char of str) {
		if ((char >= '0') && (char <= '9')) {
			// insert 'number follows' symbol only if current character is first digit of number
			if (!isNumber) {
				brailleStr += brailleMap['number'];
				isNumber = true;
			}
			brailleStr += numberMap[char] || '';
			continue;
        }
		// ignore character if there is no space between number and letter
		if (isNumber) continue;
		if (char === ' ') isNumber = false;

		// insert 'capital follows' symbol for capital letters
		if ((char >= 'A') && (char <= 'Z')) {
            brailleStr += brailleMap['capital'];
        }
		brailleStr += brailleMap[char.toLowerCase()] || '';
	}

	return brailleStr;
};

// handle I/O
const main = () => {
	const input = process.argv.slice(2).join(' ');
	const output = isBraille(input) ? brailleToEnglish(input) : englishToBraille(input);
	console.log(output);
};

main();