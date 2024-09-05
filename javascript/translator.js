/**
 * @author Sebastian Castro Obando
 * 05/09/2024
 */

function translator() {
	// Get arguments passed from command line
	const providedArgs = process.argv.slice(2);
	// We want at least one argument
	if (providedArgs.length === 0) {
		console.log("You need to provide at least one argument to translate.");
		return;
	}

    console.log(providedArgs);
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

// Call "main" function
translator();