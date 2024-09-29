const englishTranslationObject = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO",
    ".": "..OO.O"
};

const brailleTranslationObject = {
    ".OOO..": "j",
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
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
    "......": " ",
    ".....O": "capital",
    ".O.OOO": "number",
    "..OO.O": "."
};

const numberTranslationObject = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

// Edge cases what happens if user inputs english and braille?

// This will convert the letter to uppercase if needed
const checkUpperCase = (letter) => {
    if (letter !== letter.toLowerCase()) {
        return ".....O" + englishTranslationObject[letter.toLowerCase()];
    }
    return englishTranslationObject[letter]
}

const convertEnglishToBraille = (string) => {
    let translatedString = "";
    let toggleNumberMode = false;
    for (let i = 0; i < string.length; i++) {
        const currentLetter = string.charAt(i);
        if (currentLetter === brailleTranslationObject["......"]) {
            toggleNumberMode = false;
            translatedString = translatedString + englishTranslationObject[currentLetter];
            continue;
        }
        if (!isNaN(currentLetter) && toggleNumberMode === false) {
            translatedString = translatedString + englishTranslationObject["number"] + englishTranslationObject[currentLetter];
            toggleNumberMode = true;
            continue;
        }
        const brailleEquivalent = toggleNumberMode ? englishTranslationObject[currentLetter] : checkUpperCase(currentLetter);
        translatedString = translatedString + brailleEquivalent;
    }
    return translatedString;
}
const convertBrailleToEnglish = (string) => {
    // Check string is a valid Braille input, if not return error message in Braille and English
    if (string.length % 6 !== 0) {
        return "\n.....OOOO.O.O.O.O.O..O..O......OO.O.O..O........O..O..OO.OO..OOOO.O..O..O.OOO.......O...........O.O.OOO.....O.O.O..OO...OO.O.............OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.........OO.O..OOOO.O.OOO..OO...OO.OO.OOOO..\nPlease enter a valid Braille string"
    }
    let translatedString = "";
    let toggleCapitalLetter = false;
    let toggleNumberMode = false;

    for (let i = 0; i < string.length; i += 6) {
        // Counting by 6 make the itteration faster since Braille strings are longer
        let singleBrailleLetter = string.slice(i, i + 6);
        if (singleBrailleLetter === englishTranslationObject[" "]) {
            toggleNumberMode = false;
        }
        if (singleBrailleLetter === englishTranslationObject["number"]) {
            toggleNumberMode = true;
            continue;
        }
        if (singleBrailleLetter === englishTranslationObject["capital"]) {
            toggleCapitalLetter = true;
            continue;
        }
        let englishEquivalent = brailleTranslationObject[singleBrailleLetter];
        toggleCapitalLetter && (englishEquivalent = englishEquivalent.toUpperCase());
        toggleNumberMode && (englishEquivalent = numberTranslationObject[singleBrailleLetter]);
        translatedString = translatedString + englishEquivalent;
        toggleCapitalLetter = false;
    }
    return translatedString;
}

// Capture every input after file name in terminal
const stringToTranslate = process.argv.slice(2).join(' ');
// If no string is found, return an error message in Braille and English
// Braille will come first in order to clarify users who are visually impaired
if (!stringToTranslate) {
    console.log(".....OOOO.O.O.O.O.O..O..O......OO.O.O..O........OOO.O.O.OOO.O..OO.O.O.OO.OO...OO.O..O..O........O............OO.O..OOOO.O.OOO..OO...OO.OO.OOOO.........OOOO.O..OO........OOOO.O.OOO.O.....OO.OO..OO.O.O.O.O.O......OOOO.O..O..\nPlease provide a string to translate");
    return;
}

const stringSample = stringToTranslate.slice(0, 6);
const isBraille = brailleTranslationObject[stringSample];

const finalTranslation = isBraille ? convertBrailleToEnglish(stringToTranslate) : convertEnglishToBraille(stringToTranslate);
console.log(finalTranslation);