const brailleToEnglishMapping = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
};

const alphabetToNumberMapping = {
    "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
};

const englishToBrailleMapping = Object.fromEntries(
    Object.entries(brailleToEnglishMapping).filter(([_, value]) => value !== 'capital' && value !== 'number').map(([key, value]) => [value, key])
);

const numberToAlphabetMapping = Object.fromEntries(
    Object.entries(alphabetToNumberMapping).map(([key, value]) => [value, key])
);

function isBrailleInput(input) {
    return [...input].every(char => char === 'O' || char === '.');
}

function brailleToTextConverter(brailleInput) {
    const textOutput = [];
    const brailleCharacters = [];
    
    for (let i = 0; i < brailleInput.length; i += 6) {
        brailleCharacters.push(brailleInput.slice(i, i + 6));
    }

    let capitalizeNext = false;
    let numberMode = false;

    for (const brailleChar of brailleCharacters) {
        if (brailleChar === '.....O') {
            capitalizeNext = true;
        } else if (brailleChar === '.O.OOO') {
            numberMode = true;
        } else {
            let englishChar = brailleToEnglishMapping[brailleChar] || '?';
            if (capitalizeNext) {
                englishChar = englishChar.toUpperCase();
                capitalizeNext = false;
            }
            if (englishChar === ' ') {
                numberMode = false;
            }
            if (numberMode) {
                englishChar = alphabetToNumberMapping[englishChar] || englishChar;
            }
            textOutput.push(englishChar);
        }
    }

    return textOutput.join('');
}

function textToBrailleConverter(textInput) {
    const brailleOutput = [];
    let isNumberMode = false;

    for (const char of textInput) {
        if (char.toUpperCase() === char && char.toLowerCase() !== char) {
            brailleOutput.push('.....O'); // Capital follows
            brailleOutput.push(englishToBrailleMapping[char.toLowerCase()]);
        } else if (/\d/.test(char)) {
            if (!isNumberMode) {
                isNumberMode = true;
                brailleOutput.push('.O.OOO'); // Number follows
            }
            brailleOutput.push(englishToBrailleMapping[numberToAlphabetMapping[char]]);
        } else {
            if (char === " ") {
                isNumberMode = false;
            }
            brailleOutput.push(englishToBrailleMapping[char] || '......'); // Default to space if not found
        }
    }

    return brailleOutput.join('');
}

function mainFunction() {
    const inputArgs = process.argv.slice(2);

    if (inputArgs.length === 0) {
        console.log("Usage: Rerun with English or Braille input.");
        return;
    }

    let finalResult = "";
    for (let i = 0; i < inputArgs.length - 1; i++) {
        if (isBrailleInput(inputArgs[i])) {
            finalResult += brailleToTextConverter(inputArgs[i]) + " ";
        } else {
            finalResult += textToBrailleConverter(inputArgs[i]) + "......";
        }
    }

    if (isBrailleInput(inputArgs[inputArgs.length - 1])) {
        finalResult += brailleToTextConverter(inputArgs[inputArgs.length - 1]);
    } else {
        finalResult += textToBrailleConverter(inputArgs[inputArgs.length - 1]);
    }

    console.log(finalResult);
}

mainFunction();
