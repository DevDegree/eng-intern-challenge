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

function splitStringEverySixChars(inputStr) {
	let result = [];
	for (let i = 0; i < inputStr.length; i += 6) {
		result.push(inputStr.slice(i, i + 6));
	}
	return result;
}

function brailleToEnglish(str) {
	let brailleArray = splitStringEverySixChars(str);
	let isCapitalized = false;
	let isDigitMode = false;
	let result = [];

	for (let i = 0; i < brailleArray.length; i++) {
		let braille = brailleArray[i];

		if (braille === ".....O") {
			isCapitalized = true;
			continue;
		}

		if (braille === ".O.OOO") {
			isDigitMode = true;
			continue;
		}

		if (isDigitMode) {
			if (braille === "......") {
				isDigitMode = false;
			} else {
				let digitChar = brailleDigits[braille] || braille;
				result.push(digitChar);
			}
		} else {
			let convertedChar = brailleAlphabet[braille] || braille;

			if (isCapitalized) {
				convertedChar = convertedChar.toUpperCase();
				isCapitalized = false;
			}

			result.push(convertedChar);
		}
	}

	return result.join("");
}

function englishToBraille(str) {
	let englishArray = str.split("");
	let isDigitMode = false;
	let result = [];

	for (let i = 0; i < englishArray.length; i++) {
		let englishChar = englishArray[i];

		if (!isNaN(englishChar) && englishChar !== " ") {
			if (!isDigitMode) {
				result.push(".O.OOO");
				isDigitMode = true;
			}
			result.push(englishDigits[englishChar]);
			continue;
		}

		if (englishChar === " ") {
			result.push("......");
			isDigitMode = false;
			continue;
		}

		if (isDigitMode && isNaN(englishChar)) {
			isDigitMode = false;
		}

		if (englishChar === englishChar.toUpperCase() && isNaN(englishChar)) {
			result.push(".....O");
			englishChar = englishChar.toLowerCase();
		}

		result.push(englishAlphabet[englishChar] || "......");
	}

	return result.join("");
}

function translator(str) {
	let type = detectStringType(str);

	if (type === "string") {
		console.log(englishToBraille(str));
	} else if (type === "braille") {
		console.log(brailleToEnglish(str));
	} else {
		console.log("error occurred: please input a proper string");
	}
}

module.exports = {
	detectStringType,
	englishToBraille,
	brailleToEnglish,
	translator,
};

if (require.main === module) {
	const args = process.argv.slice(2);
	const input = args.join(" ");
	translator(input);
}
