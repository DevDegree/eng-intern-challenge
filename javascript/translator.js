const brailleAlphabet = {
	"O.....": "a",
	"O.O...": "b",
	"OO....": "c",
	"OO.O..": "d",
	"O..O..": "e",
	"OOO...": "f",
	"OOOO..": "g",
	"O.OO..": "h",
	".OO...": "i",
	".OOO..": "j",
	"O...O.": "k",
	"O.O.O.": "l",
	"OO..O.": "m",
	"OO.OO.": "n",
	"O..OO.": "o",
	"OOO.O.": "p",
	"OOOOO.": "q",
	"O.OOO.": "r",
	".OO.O.": "s",
	".OOOO.": "t",
	"O...OO": "u",
	"O.O.OO": "v",
	".OOO.O": "w",
	"OO..OO": "x",
	"OO.OOO": "y",
	"O..OOO": "z",
	".....O": "^",
	".O.OOO": "#",
	"......": " ",
};

const englishAlphabet = {
	a: "O.....",
	b: "O.O...",
	c: "OO....",
	d: "OO.O..",
	e: "O..O..",
	f: "OOO...",
	g: "OOOO..",
	h: "O.OO..",
	i: ".OO...",
	j: ".OOO..",
	k: "O...O.",
	l: "O.O.O.",
	m: "OO..O.",
	n: "OO.OO.",
	o: "O..OO.",
	p: "OOO.O.",
	q: "OOOOO.",
	r: "O.OOO.",
	s: ".OO.O.",
	t: ".OOOO.",
	u: "O...OO",
	v: "O.O.OO",
	w: ".OOO.O",
	x: "OO..OO",
	y: "OO.OOO",
	z: "O..OOO",
	" ": "......",
};

const brailleDigits = {
	"O.....": 1,
	"O.O...": 2,
	"OO....": 3,
	"OO.O..": 4,
	"O..O..": 5,
	"OOO...": 6,
	"OOOO..": 7,
	"O.OO..": 8,
	".OO...": 9,
	".OOO..": 0,
};

const englishDigits = {
	1: "O.....",
	2: "O.O...",
	3: "OO....",
	4: "OO.O..",
	5: "O..O..",
	6: "OOO...",
	7: "OOOO..",
	8: "O.OO..",
	9: ".OO...",
	0: ".OOO..",
};

function detectStringType(inputStr) {
	for (let char of inputStr) {
		if (/[a-np-zA-NP-Z0-9]/.test(char)) {
			return "string";
		}
	}
	return "braille";
}

console.log(detectStringType("help"), detectStringType("O.OO.."));

function splitStringEverySixChars(inputStr) {
	let result = [];
	// Loop through the string and take 6 characters at a time
	for (let i = 0; i < inputStr.length; i += 6) {
		// Push a substring of 6 characters into the result array
		result.push(inputStr.slice(i, i + 6));
	}
	return result;
}

function brailleToEnglish(str) {
	let brailleArray = splitStringEverySixChars(str);
	console.log("Braille Array:", brailleArray); // Debugging print
	let isCapitalized = false;
	let isDigitMode = false;
	let result = [];

	for (let i = 0; i < brailleArray.length; i++) {
		let braille = brailleArray[i];

		if (braille === ".....O") {
			// Capitalization marker, set the flag to capitalize the next letter
			isCapitalized = true;
			continue; // Skip to the next item
		}

		if (braille === ".O.OOO") {
			// Digit mode marker, switch to interpreting digits
			isDigitMode = true;
			continue; // Skip to the next item
		}

		if (isDigitMode) {
			// If we are in digit mode, look for digits in the brailleDigits object
			if (braille === "......") {
				// End of digit mode if we encounter a space
				isDigitMode = false;
			} else {
				// Push digit or keep the original if not found in the brailleDigits
				let digitChar = brailleDigits[braille] || braille;
				result.push(digitChar);
			}
		} else {
			// Regular conversion mode (letters or symbols)
			let convertedChar = brailleAlphabet[braille] || braille; // Convert to English

			if (isCapitalized) {
				// Capitalize the next character if flag is set
				convertedChar = convertedChar.toUpperCase();
				isCapitalized = false; // Reset capitalization flag
			}

			result.push(convertedChar);
		}
	}

	return result.join(""); // Join result array into a final string
}

console.log(
	brailleToEnglish(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
);
