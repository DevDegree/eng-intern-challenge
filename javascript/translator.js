// Create english object
// Create braille object
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
    ".": ".O...O"
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
    ".O...O": "."
};

// Need to handle numbers and capital letter
// Tackle capital letters first
const stringToTranslate = process.argv.slice(2).join(' ');
if (!stringToTranslate) {
    console.log("Please provide string to translate");
    return;
}
let translatedString = "";
// First translate from braile to english
const stringSample = stringToTranslate.slice(0, 6);
const isBraille = brailleTranslationObject[stringSample];
let singleBrailleLetter = "";

// How to track capital letters first from english to braille
const checkUpperCase = (letter) => {
    if(letter !== letter.toLowerCase()){
        return ".....O" + englishTranslationObject[letter.toLowerCase()];
    }
    return englishTranslationObject[letter]
}
// H -> .....O O.OO..
for (let i = 0; i < stringToTranslate.length; i++) {
    if (isBraille) {
        singleBrailleLetter = singleBrailleLetter + stringToTranslate.charAt(i);
        if (singleBrailleLetter.length === 6) {
            const englishEquivalent = brailleTranslationObject[singleBrailleLetter];
            translatedString = translatedString + englishEquivalent;
            singleBrailleLetter = "";
        }
        continue;
    }
    const currentLetter = stringToTranslate.charAt(i);
    const brailleEquivalent = checkUpperCase(currentLetter);
    translatedString = translatedString + brailleEquivalent;
}

console.log(translatedString);