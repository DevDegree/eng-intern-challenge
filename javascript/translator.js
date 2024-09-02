// Written by Mostafa Bander

const brailleMap = {
	// Letters
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

	// Numbers
	1: 'O.....',
	2: 'O.O...',
	3: 'OO....',
	4: 'OO.O..',
	5: 'O..O..',
	6: 'OOO...',
	7: 'OOOO..',
	8: 'O.OO..',
	9: '.OO...',
	0: '.OOO..',

	// ...Follows
	CAPITAL: '.....O',
	DECIMAL: '.O...O',
	NUMBER: '.O.OOO',

	// Special Characters
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
	')': '.O.OO.',
	' ': '......',
};

// Reverse mapping for Braille to English
const reverseBrailleMap = Object.fromEntries(
	Object.entries(brailleMap).map(([k, v]) => [v, k])
);

function englishToBraille(englishInput) {
	let result = '';
	let isPreviousCharNumber = false;

	for (let char of englishInput) {
		if (!isNaN(char) && char !== ' ') {
			if (!isPreviousCharNumber) {
				result += brailleMap.NUMBER;
				isPreviousCharNumber = true;
			}
			result += brailleMap[char]; // No need to convert to lowercase for numbers
		} else {
			if (char === char.toUpperCase() && char !== ' ') {
				result += brailleMap.CAPITAL;
			}
			result += brailleMap[char.toLowerCase()] || ''; // Convert to lowercase for letters
			isPreviousCharNumber = false;
		}
	}

	// console.log('English to Braille Result:', result); // Debugging output
	return result;
}

function brailleToEnglish(brailleInput) {
	let result = '';
	const brailleChars = brailleInput.match(/.{6}/g) || []; // Ensures each Braille character is exactly 6 dots long
	let isCapital = false;
	let isNumber = false;
	let isSpace = false;

	for (let brailleChar of brailleChars) {
		// console.log(`Processing Braille Character: ${brailleChar}`); // Debugging output

		if (brailleChar === brailleMap.CAPITAL) {
			isCapital = true;
			continue;
		}
		if (brailleChar === brailleMap.NUMBER) {
			isNumber = true;
			continue;
		}
		if (brailleChar === brailleMap[' ']) {
			result += ' ';
			isNumber = false;
			continue;
		}

		let englishChar = reverseBrailleMap[brailleChar];
		if (isCapital) {
			englishChar = englishChar ? englishChar.toUpperCase() : '';
			isCapital = false;
		}
		if (isNumber) {
			// Convert back to a digit
			englishChar =
				Object.entries(brailleMap).find(
					([key, value]) => value === brailleChar && !isNaN(key)
				)?.[0] || '';
		}

		// console.log(`Detected English Character: ${englishChar}`); // Debugging output
		result += englishChar || ''; // Fallback in case of unmatched Braille pattern
	}

	// console.log('Final Result:', result); // Debugging output
	return result;
}

// Function to check if input is Braille or English
function detectInputType(input) {
	return input.match(/^[.O\s]*$/) ? 'braille' : 'english';
}

// Main function to translate input based on detected type
function translate(input) {
	const inputType = detectInputType(input);
	// console.log('Detected Input Type:', inputType); // Debugging output
	return inputType === 'braille'
		? brailleToEnglish(input)
		: englishToBraille(input);
}

if (require.main === module) {
	const input = process.argv.slice(2).join(' '); // Capture command line arguments as a single string
	// console.log('Input:', input); // Debugging output
	console.log(translate(input)); // Run the translation and print the result
}
