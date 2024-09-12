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
	
    //Add lowercase letter
    englishToBraille[char] = braille;
    englishToBraille[char.toUpperCase()] = capital + braille;
    
});


// Handle numbers
Object.entries(brailleToEnglishNum).forEach(([braille, char]) => {
		englishToBraille[char] = braille;
	
});

// Space character mapping
englishToBraille[" "] = space;

console.log(englishToBraille);

// Check if input is Braille (if input contains only 'O' or '.' characters)
function isBraille(input) {
	return /^[O.]+$/.test(input);
}

function isNumber(char) {
    return /\d/.test(char);
}

// Translate English to Braille
function translateEnglishToBraille(input) {
	let output = "";
    let numMode = false;

	for (let i = 0; i < input.length; i++) {
		const char = input[i];
        if (isNumber(char) && !numMode) {
            output += number + englishToBraille[char]
            numMode = true
        } else if  (isNumber(char) && numMode) {
            output += englishToBraille[char]
        } else {
            numMode = false
            output += englishToBraille[char]
        }
	}
	return output;
}

input = "Abc 123"
console.log("English to braille")
console.log(translateEnglishToBraille(input));

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
		} else if (brailleToEnglishAlph[currentSymbol]) { //check
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

input = ".O.OOOOO.O..O.O...";
// input = "hello world";

console.log(translateBrailleToEnglish(input));
