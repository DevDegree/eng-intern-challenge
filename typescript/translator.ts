/**
* Dictionary mapping English characters to their Braille representation.
*
* @type { [key: string]: string }
*/
const englishToBrailleMapping: { [key: string]: string } = {
    "a": "O.....", "b": "O.O...", "c": "OO....",
    "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
    "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", 
    
    "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..",
    
    " ": "......"
  };

const brailleCapitalIndicator = ".....O";
const brailleNumberIndicator = ".O.OOO";

/**
 * Verifies if the input string is in Braille format.
 *
 * @param {string} input - The string to verify.
 * @returns {boolean} - True if the input is in Braille format, false otherwise.
 */
function isBrailleFormat(input: string): boolean {
    return /^[O.]+$/g.test(input);
}

/**
 * Converts an English string to its Braille representation.
 *
 * @param {string} input - The English string to convert.
 * @returns {string} - The Braille representation of the input.
 */
function convertEnglishToBraille(input: string): string {
    let brailleOutput = "";
    let inNumberMode = false;

    for (const char of input) {
        if (char.match(/[A-Z]/)) {
            brailleOutput += brailleCapitalIndicator;
            brailleOutput += englishToBrailleMapping[char.toLowerCase()] || "";
        } else if (char.match(/[0-9]/)) {
            if (!inNumberMode) {
                brailleOutput += brailleNumberIndicator;
                inNumberMode = true;
            }
            brailleOutput += englishToBrailleMapping[char] || "";
        } else {
            brailleOutput += englishToBrailleMapping[char] || "";
            inNumberMode = false;
        }
    }

    return brailleOutput;
}

/**
 * Translates a Braille string to English.
 *
 * @param {string} input - The Braille string to translate.
 * @returns {string} - The English representation of the input.
 */
function translateBrailleToEnglish(input: string): string {
    const brailleToEnglishMapping: { [key: string]: string } = Object.fromEntries(
        Object.entries(englishToBrailleMapping).map(([key, value]) => [value, key])
    );

    let englishOutput = "";
    let capitalizeNext = false;
    let inNumberMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleSymbol = input.slice(i, i + 6);

        if (brailleSymbol === brailleCapitalIndicator) {
            capitalizeNext = true;
            continue;
        }

        if (brailleSymbol === brailleNumberIndicator) {
            inNumberMode = true;
            continue;
        }

        const englishChar = brailleToEnglishMapping[brailleSymbol];
        if (englishChar) {
            if (inNumberMode && englishChar.match(/[a-j]/)) {
                englishOutput += String.fromCharCode(englishChar.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
            } else {
                englishOutput += capitalizeNext ? englishChar.toUpperCase() : englishChar;
            }
            capitalizeNext = false;
            inNumberMode = false;
        }
    }

    return englishOutput;
}

function main() {
    const inputArgs = process.argv.slice(2);
    if (inputArgs.length === 0) {
        console.error("Error: No Input Provided.");
        process.exit(1);
    }

    const inputString = inputArgs.join(" ");
    const result = isBrailleFormat(inputString) ? translateBrailleToEnglish(inputString) : convertEnglishToBraille(inputString);
    console.log(result);
}

main();
