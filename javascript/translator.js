// Mappings for English to Braille Translation
const englishToBraille = {
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
	CAPITAL: ".....O",
	NUMBER: ".O.OOO",
};

const numberToBraille = {
	0: ".OOO..",
	1: "O.....",
	2: "O.O...",
	3: "OO....",
	4: "OO.O..",
	5: "O..O..",
	6: "OOO...",
	7: "OOOO..",
	8: "O.OO..",
	9: ".OO...",
};

// Reverse mappings
const brailleToEnglish = {};
for (const [key, value] of Object.entries(englishToBraille)) {
	if (key !== "CAPITAL" && key !== "NUMBER") {
		brailleToEnglish[value] = key;
	}
}

const brailleToNumber = {};
for (const [key, value] of Object.entries(numberToBraille)) {
	brailleToNumber[value] = key;
}

// Check if the input is Braille (or English)
const isBraille = (text) => {
	if (text.length % 6 !== 0) {
		return false;
	}

	for (let char of text) {
		// only '0' and '.' are valid Braille characters
		if (char !== "O" && char !== ".") {
			return false;
		}
	}

	return true;
};

// Function to translate English to Braille
const translateToBraille = (text) => {
	// store the translation as an array, and join at the end
	let result = [];
	let isNumber = false;

	for (let char of text) {
		// check for special inputs first
		if (char === " ") {
			result.push(englishToBraille[" "]);
			continue;
		}

		if (char.toUpperCase() === char && isNaN(parseInt(char))) {
			result.push(englishToBraille["CAPITAL"]);
			char = char.toLowerCase();
			isNumber = false;
		}

		if (!isNaN(parseInt(char))) {
			if (!isNumber) {
				result.push(englishToBraille["NUMBER"]);
				isNumber = true;
			}
			result.push(numberToBraille[char]);
		} else {
			isNumber = false;
			result.push(englishToBraille[char] || "");
		}
	}

	return result.join("");
};

// Function to translate Braille to English
const translateToEnglish = (braille) => {
	// store the translation as an array, and join at the end
	let result = [];
	let isCapital = false;
	let isNumber = false;
	const brailleSymbolLength = 6;

	for (let i = 0; i < braille.length; i += brailleSymbolLength) {
		const symbol = braille.slice(i, i + brailleSymbolLength);

		// check for special inputs first
		if (symbol === englishToBraille["CAPITAL"]) {
			isCapital = true;
		} else if (symbol === englishToBraille["NUMBER"]) {
			isNumber = true;
		} else if (symbol === englishToBraille[" "]) {
			result.push(" ");
			isNumber = false;
		} else {
			if (isNumber) {
				result.push(brailleToNumber[symbol] || "");
			} else {
				let letter = brailleToEnglish[symbol] || "";
				if (isCapital) {
					letter = letter.toUpperCase();
					isCapital = false;
				}
				result.push(letter);
			}
		}
	}

	return result.join("");
};

// CLI
const main = () => {
	const args = process.argv.slice(2);
	const inputText = args.join(" ");

	if (isBraille(inputText)) {
		console.log(translateToEnglish(inputText));
	} else {
		console.log(translateToBraille(inputText));
	}
};

if (require.main === module) {
	main();
}
