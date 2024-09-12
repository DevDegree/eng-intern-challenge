/**
 * @author Sebastian Castro Obando
 * 05/09/2024
 */

/**
 *	@param {string} str - to be tested if it is braille
 *	@returns {boolean} False if str is English; True if str is Braille. As defined below.
 */
 function isBraille(str) {
	/**
	 * We assume that a string is braille if and only if it contains at least 6 characters
	 * and it only contains characters "0" and ".". 
	 */

	// Braille letters are composed of 6 letter "chunks"
	if (str.length < 6) {
		return false;
	}
	// Braille text only contains "." or "O". Regex test : 
	let isValidBraille = /^[.O]+$/.test(str);
	
	// Braille test. See above iff condition. 
	return isValidBraille;
}

/**
 *	@param {string} str - String in english to be translated to braille
 *	@returns {string} englishToBrailleTranslation the translated string
 */
function englishToBraille(str) {
	englishToBrailleTranslation = ""; // String to be returned
	let numberMode = false; // Used when tranlasting numbers

	str.forEach( (subStr, index) => {
		for (const currentChar of subStr) {
			// Check if character is a number
			if ( '0' <= currentChar && currentChar <= '9') {
				// Check if number mode was set
				if (!numberMode) {
					// Number mode not set, send special number braille character
					englishToBrailleTranslation += englishToBrailleDict['number'];
					// Set number mode
					numberMode = true;
				}
				englishToBrailleTranslation += englishToBrailleDict[currentChar];
			} else {
				// Not a number
				numberMode = false;
				if (currentChar === currentChar.toUpperCase()) {
					// Find the code for the capitalization
					englishToBrailleTranslation += englishToBrailleDict['capitalization'] + englishToBrailleDict[currentChar.toLowerCase()];
				} else {
					englishToBrailleTranslation += englishToBrailleDict[currentChar];
				}
			}
		}
		// If it's not the last string, add a space character between strings
		if (index < str.length - 1) {
			englishToBrailleTranslation += englishToBrailleDict['space'];
		}
	});
	return englishToBrailleTranslation;
}

/**
 *	@param {string} str - String in braille to be translated to english
 *	@returns {string} the translated string
 */
function brailleToEnglish(str) {
	let englighStr = "";
	let numberMode = false;
    let brailleChunkSize = 6; // Maybe add as an global constant?
	for (let i = 0; i < str.length; i += brailleChunkSize) {
		let chunk = str.slice(i, i + brailleChunkSize);

		let chunkToEnglish = brailleToEnglishDict[chunk];

		if (chunkToEnglish === "capitalization") {
			// Grab the next chunk
			i += brailleChunkSize;
			chunk = str.slice(i, i + brailleChunkSize);
			englighStr += brailleToEnglishDict[chunk].toUpperCase();
		} else if (chunkToEnglish === "space") {
			englighStr += " ";
			numberMode = false;
		} else if (chunkToEnglish === "number") {
			numberMode = true;
		} else if (chunkToEnglish) {
			if (!numberMode) {
				englighStr += brailleToEnglishDict[chunk];
			} else {
				englighStr += Object.keys(brailleToEnglishDict).indexOf(chunk) + 1;
			}
		} else {
			// undefined braille
			console.log("Error parsing : Braille character not found : " + chunk);
		}
	}
	return englighStr;
}

function translator() {
	// Get arguments passed from command line
	const providedArgs = process.argv.slice(2);
	// We want at least one argument
	if (providedArgs.length === 0) {
		console.log("You need to provide at least one argument to translate.");
		return;
	}

	let translation = "";
	// From the problem description, it seems that braille text will not contain spaces. This can
	// save us some time.
	if (providedArgs.length === 1 && isBraille(providedArgs[0])) {
		// is braille
		translation = brailleToEnglish(providedArgs[0]);
		console.log(translation);
		return;
	} else {
		// is english
		translation = englishToBraille(providedArgs);
		console.log(translation);
		return;
	}
}

// Definitions -----------------------------
const brailleToEnglishDict = {
	"O....." : "a", "O.O..." : "b", "OO...." : "c", 
	"OO.O.." : "d", "O..O.." : "e", "OOO..." : "f", 
	"OOOO.." : "g", "O.OO.." : "h", ".OO..." : "i",
	".OOO.." : "j", "O...O." : "k", "O.O.O." : "l",
	"OO..O." : "m", "OO.OO." : "n", "O..OO." : "o", 
	"OOO.O." : "p", "OOOOO." : "q", "O.OOO." : "r",
	".OO.O." : "s", ".OOOO." : "t", "O...OO" : "u",
	"O.O.OO" : "v", ".OOO.O" : "w", "OO..OO" : "x",
	"OO.OOO" : "y", "O..OOO" : "z",  "......" : " ",
	".....O" : "capitalization", 
	".O.OOO" : "number", 
	"......" : "space"
}

const englishToBrailleDict = {
	"a" : "O.....", "b" : "O.O...", "c" : "OO....",
	"d" : "OO.O..", "e" : "O..O..", "f" : "OOO...",
	"g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...",
	"j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.",
	"m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.",
	"p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.",
	"s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO",
	"v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
	"y" : "OO.OOO", "z" : "O..OOO",
	"1" : "O.....", "2" : "O.O...", "3" : "OO....", 
	"4" : "OO.O..", "5" : "O..O..", "6" : "OOO...", 
	"7" : "OOOO..", "8" : "O.OO..", "9" : ".OO...",
	"0" : ".OOO..", 
	"capitalization" : ".....O",
	"number" : ".O.OOO",
	"space" : "......"
}
// -----------------------------------------

// Call "main" function
translator();