// Written by Mostafa Bander

const brailleMap = {
	// Letters
	a: '0.....',
	b: '00....',
	c: '0..0..',
	d: '00.0..',
	e: '0..0..',
	f: '000...',
	g: '0000..',
	h: '0.00..',
	i: '.00...',
	j: '.000..',
	k: '0...0.',
	l: '0.0.0.',
	m: '00..0.',
	n: '00.00.',
	o: '0..00.',
	p: '000.0.',
	q: '00000.',
	r: '0.000.',
	s: '.00.0.',
	t: '.0000.',
	u: '0...00',
	v: '0.0.00',
	w: '.000.0',
	x: '00..00',
	y: '00.000',
	z: '0..000',

	// Numbers
	1: '0.....',
	2: '0.0...',
	3: '00....',
	4: '00.0..',
	5: '0..0..',
	6: '000...',
	7: '0000..',
	8: '0.00..',
	9: '.00...',
	0: '.000..',

	// ...Follows
	CAPITAL: '.....0',
	DECIMAL: '.0...0',
	NUMBER: '.0.000',

	// Special Characters
	'.': '..00.0',
	',': '..0...',
	'?': '..0.00',
	'!': '..000.',
	':': '..00..',
	';': '..0.0.',
	'-': '....00',
	'/': '.0..0.',
	'<': '.00..0',
	'>': '0..00.',
	'(': '0.0..0',
	')': '.0.00.',
	space: '......',
};

// Reverse mapping for Braille to English
const reverseBrailleMap = Object.fromEntries(
	Object.entries(brailleMap).map(([k, v]) => [v, k])
);

function englishToBraille(englishInput) {
	let result = '';
	for (let char of englishInput) {
		if (char === char.toUpperCase() && char !== ' ') {
			result += brailleMap.CAPITAL;
		}
		if (!isNaN(char)) {
			result += brailleMap.NUMBER;
		}
		result += brailleMap[char.toLowerCase()] || ''; // Convert to lowercase for mapping
	}
	return result;
}

function brailleToEnglish(brailleInput) {
	let result = '';
	const brailleChars = brailleInput.match(/.{1,6}/g); // Splits input into chunks of 6
	let isCapital = false;
	let isNumber = false;

	for (let brailleChar of brailleChars) {
		if (brailleChar === brailleMap.CAPITAL) {
			isCapital = true;
			continue;
		}
		if (brailleChar === brailleMap.NUMBER) {
			isNumber = true;
			continue;
		}

		let englishChar = reverseBrailleMap[brailleChar];
		if (isCapital) {
			englishChar = englishChar.toUpperCase();
			isCapital = false;
		}
		if (isNumber) {
			isNumber = false; // Reset after using the number follows symbol
		}

		result += englishChar || ''; // Fallback in case of unmatched Braille pattern
	}
	return result;
}
