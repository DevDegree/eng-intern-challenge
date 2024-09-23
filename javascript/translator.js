const brailleAlphabet = {
  a: 'O.....',
  b: 'O.O...',
  c: 'OO....',
  d: 'OO.O..',
  e: 'O..O..',
  f: 'OOO...',
  g: 'OOOO..',
  h: 'O.OO..',
  i: '.OO...',
  j: '.OOO..',
  k: 'O...O.',
  l: 'O.O.O.',
  m: 'OO..O.',
  n: 'OO.OO.',
  o: 'O..OO.',
  p: 'OOO.O.',
  q: 'OOOOO.',
  r: 'O.OOO.',
  s: '.OO.O.',
  t: '.OOOO.',
  u: 'O...OO',
  v: 'O.O.OO',
  w: '.OOO.O',
  x: 'OO..OO',
  y: 'OO.OOO',
  z: 'O..OOO',

	//number
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
 
	//condition
	' ': '......',
  capital: '.....O',
  number: '.O.OOO',

	//punctuation
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  '!': '..OOO.',
  ':': '..OO..',
  ';': '..O.O.',
  '-': '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.'
};

	//check if Braille contains only 'O' and '.'
function isBraille(input) {
	for (let i = 0; i < input.length; i++) {
		const char = input[i];
		if (char !=='O' && char !== '.') {
			return false;
		}
	}

	//check if its divisible by 6
	if (input.length % 6 !== 0) {
		return false;
	}
	return true;
}

function translate(input) {
	if (isBraille(input)) {
		return brailleToText(input);
	} else {
		return textToBraille(input);
	}
}

function brailleToText(braille) {
	let result = '';
	let isNumber = false;
	let isCapital = false;
	
	for (let i = 0; i < braille.length; i += 6) {
		const chunk = braille.slice(i, i + 6);

		// check for number indicator
		if (chunk === brailleAlphabet.number) {
			isNumber = true;
			continue;
		}

		// check for capital alphabet indicator
		if (chunk === brailleAlphabet.capital) {
			isCapital = true;
			continue;
		}

		for (let key in brailleAlphabet) {
			if (brailleAlphabet[key] === chunk) {
				if (!isNumber && key >= 'a' && key <= 'z') {
					if (isCapital) {
						result += key.toUpperCase();
						isCapital = false;
					} else {
						result += key; // add letter if not in number mode TODO not working
					}
				}	else if (isNumber && key >= '1' && key <= '9' || key === '0') {
					result += key; // add number if in number mode
				}  else if (key === ' ') {
					result += ' '; // add space
					isNumber = false; // reset number mode after space
				}
				// break;
			}
		}
	}
	return result;
}

function textToBraille(text) {

	let result = '';
	let isNumber = false;

	for (let i = 0; i < text.length; i++) {
		const char = text[i];

		//check if char is a number
		if (char >= '0' && char <= '9') {
			if (!isNumber) {
				result += brailleAlphabet.number; //add number indicator
				isNumber = true;
			}
			result += brailleAlphabet[char];
		} else {
			if (isNumber) {
				isNumber = false; // reset number mode
			}

			//check if char is uppercase
			if (char >= 'A' && char <= 'Z') {
				result += brailleAlphabet.capital;
				result += brailleAlphabet[char.toLowerCase()];
			} else {
				result += brailleAlphabet[char];
			}
		}
	}
	return result;
}