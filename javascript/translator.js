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
    ".O.OOO": "number", //could get rid of?
    "..OO.O": "."
};

const numberTranslattionObject = {
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
const stringToTranslate = process.argv.slice(2).join(' ');
if (!stringToTranslate) {
    console.log("Please provide string to translate");
    return;
}


// First translate from braile to english
const stringSample = stringToTranslate.slice(0, 6);
const isBraille = brailleTranslationObject[stringSample];

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
        if (currentLetter === " ") {
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
    // Check if it is a valid Braille input
    if(string % 6 !== 0){
        return "\n.....OOOO.O.O.O.O.O..O..O......OO.O.O..O........O..O..OO.OO..OOOO.O..O..O.OOO.......O...........O.O.OOO.....O.O.O..OO...OO.O.............OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.........OO.O..OOOO.O.OOO..OO...OO.OO.OOOO..\nPlease enter a valid Braille string"
    }
    let translatedString = "";
    let singleBrailleLetter = "";
    let toggleCapitalLetter = false;
    let toggleNumberMode = false;
    for (let i = 0; i < string.length; i++) {
        // could count per six to make it faster
        
        singleBrailleLetter = singleBrailleLetter + string.charAt(i);
        if (singleBrailleLetter.length === 6) {
            if (singleBrailleLetter === englishTranslationObject[" "]) {
                toggleNumberMode = false;
            }
            if (singleBrailleLetter === englishTranslationObject["number"]) {
                toggleNumberMode = true;
                singleBrailleLetter = ""
                continue;
            }
            if (singleBrailleLetter === englishTranslationObject["capital"]) {
                toggleCapitalLetter = true;
                singleBrailleLetter = "";
                continue;
            }
            let englishEquivalent = brailleTranslationObject[singleBrailleLetter];
            toggleCapitalLetter && (englishEquivalent = englishEquivalent.toUpperCase());
            toggleNumberMode && (englishEquivalent = numberTranslattionObject[singleBrailleLetter]);
            translatedString = translatedString + englishEquivalent;
            singleBrailleLetter = "";
            toggleCapitalLetter = false;
        }
        continue;
    }
    return translatedString;
}


const finalTranslation = isBraille ? convertBrailleToEnglish(stringToTranslate) : convertEnglishToBraille(stringToTranslate);
console.log(finalTranslation);