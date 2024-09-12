// Braille to English mapping
const brailleToEnglishAlph = {
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
};

const capital = ".....O";
const number = ".O.OOO";
const space = "......";

const brailleToEnglishNum = {
	".OOO..": "0",
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
};

// English to Braille mapping
// Initialize an empty object to store English to Braille mappings
const englishToBraille = {};

// Loop over each entry in the brailleToEnglish object
Object.entries(brailleToEnglishAlph).forEach(([braille, char]) => {
	// Handle for uppercase and lowercase letters
	if (char.length === 1 && char !== " ") {
		englishToBraille[char.toLowerCase()] = braille;

		// Mapping for uppercase
		if (char.toUpperCase() === char) {
			//Check
			englishToBraille[char] = capital + braille;
		} else {
			console.log("error: unrecognizable character");
		}
	}
});

// Handle numbers
Object.entries(brailleToEnglishNum).forEach(([braille, char]) => {
	if (!isNaN(char)) {
		englishToBraille[char] = number + braille;
	}
});

// Space character mapping

englishToBraille[" "] = space;

console.log(englishToBraille);

// Check if input is Braille (if input contains only 'O' or '.' characters)
function isBraille(input) {
	return /^[O.]+$/.test(input);
}

// Translate English to Braille
function translateEnglishToBraille(input) {
	let output = "";
	for (let i = 0; i < input.length; i++) {
		const char = input[i];
		if (englishToBraille[char]) {
			output += englishToBraille[char];
		} else {
			console.log("Error: Character does not have a Braille equivalent");
		}
	}
	return output;
}
//console.log(englishToBraille());

// Translate Braille to English
function translateBrailleToEnglish(input) {
	let output = "";
	let i = 0;
	let isCapital = false;
	let isNumber = false;

	while (i < input.length) {
		const currentSymbol = input.slice(i, i + 6); // to account for 6 braille symbols
		console.log(currentSymbol);
		if (currentSymbol === capital) {
			isCapital = true;
		} else if (currentSymbol === number) {
			isNumber = true;
			console.log("Number detected");
		} else if (currentSymbol === space) {
			output += " "; // to account for space
			isNumber = false;
		} else if (brailleToEnglishAlph[currentSymbol]) {
			let char = brailleToEnglishAlph[currentSymbol];
			if (isCapital) {
				output += char.toUpperCase();
				isCapital = false;
			} else if (isNumber) {
				let num = brailleToEnglishNum[currentSymbol];
				output += num;
			} else if (!isNumber) {
				output += char;
			}
		}
		i += 6;
	}
	return output;
}
//console.log(brailleToEnglish());

// Main traslator function

function mainTranslator() {
	const commandInput = process.argv.slice(2); //  slicing the first two arguments to command line argument
	const input = commandInput.join(" ");
	let output = "";

	if (isBraille(input)) {
		if (input.length % 6 === 0) {
			output = translateBrailleToEnglish(input);
		} else {
			output = "Error: incorrect Braille patterns";
		}
	} else {
		output = translateEnglishToBraille(input);
	}

	console.log(output);
}

//mainTranslator();

input = "O.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
// input = "hello world";

console.log(translateBrailleToEnglish(input));
