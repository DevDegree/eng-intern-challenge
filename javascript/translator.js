// Braille to English mapping
const brailleToEnglish = {
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
	".....O": "capital",
	"....OO": "number",
	"......": " ",
	".O.OOO": "0",
	".O..OO": "1",
	".OO.OO": "2",
	".O.O.O": "3",
	".O.O..": "4",
	".OO..O": "5",
	".OO.O.": "6",
	"OOO..O": "7",
	"OOO...": "8",
	"OOO.OO": "9",
};

// English to Braille mapping
// Initialize an empty object to store English to Braille mappings
const englishToBraille = {};

// Loop over each entry in the brailleToEnglish object
Object.entries(brailleToEnglish).forEach(([braille, char]) => {
    // Handle for uppercase and lowercase letters
    if (char.length === 1 && char !== ' ') {
        englishToBraille[char.toLowerCase()] = braille; 

        // Mapping for uppercase
        if (char.toUpperCase() === char) {
            englishToBraille[char] = ".....O" + braille; 
        }
    }
    
    // Handle numbers
    if (!isNaN(char)) {
        englishToBraille[char] = "....OO" + braille; 
    }
});

// Space character mapping
englishToBraille[' '] = "......"; 

// Check if input is Braille (if input contains only 'O' or '.' characters)
function isBraille(input) {
    return /^[O.]+$/.test(input);
}