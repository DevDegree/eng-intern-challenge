//braille to english mapping
const brailleToEnglishAlphabets = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "number"
};

//braille digits
const brailleToEnglishDigits = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
};

//english to braille mapping
const englishAlphabetsToBraille = Object.fromEntries(
    Object.entries(brailleToEnglishAlphabets).map(([k, v]) => [v, k])
);  

//english digits
const englishDigitsToBraille = Object.fromEntries(
    Object.entries(brailleToEnglishDigits).map(([k, v]) => [v, k])
);

//function to determine if input is braille or english
function isBraille(input) {
    return /^[O.]+$/.test(input.replace(/\s/g, ''));
}

//function to convert braille to english
function translateBrailleToEnglish(input) {
    const brailleSymbols = input.match(/.{6}/g);
    let translation = '';
    let isCapital = false;
    let isNumber = false;

    brailleSymbols.forEach(symbol => {
        if (symbol === ".....O") {
            //capitalize next letter
            isCapital = true;
        } else if (symbol === ".O.OOO") {
            //start number mode
            isNumber = true;
        } else if (symbol in brailleToEnglishAlphabets) {
            if (isNumber) {
                //handle numbers
                translation += brailleToEnglishDigits[symbol] || '';
            } else {
                let letter = brailleToEnglishAlphabets[symbol];
                if (isCapital && letter !== ' ') {
                    letter = letter.toUpperCase();
                    isCapital = false;
                }
                translation += letter;
            }
        } else if (symbol === "......") {
            //space will reset number mode
            translation += ' ';
            isNumber = false;
        }
    });
    return translation;
}

//function to convert english to braille
function translateEnglishToBraille(input) {
    let translation = '';
    let isNumber = false;

    for (let char of input) {
        if (/[A-Z]/.test(char)) {
            //add capital symbol for uppercase letters
            translation += englishAlphabetsToBraille['capital'];
            //add the lowercase equivalent in Braille
            translation += englishAlphabetsToBraille[char.toLowerCase()];
        } else if (/[a-z]/.test(char)) {
            //lowercase letters are directly mapped
            translation += englishAlphabetsToBraille[char];
        } else if (/\d/.test(char)) {
            if (!isNumber) {
                //add number symbol once
                translation += englishAlphabetsToBraille['number'];
                isNumber = true;
            }
            translation += englishDigitsToBraille[char];
        } else {
            if (isNumber && /\D/.test(char)) {
                //exit number mode on non-number
                isNumber = false;
            }
            //handle spaces and punctuation
            translation += englishAlphabetsToBraille[char.toLowerCase()] || '';
        }
    }
    return translation;
}

//main function
function main() {
    const input = process.argv.slice(2).join(' ');

    //if no input is given
    if (!input) {
      console.error('Please provide input to translate.');
      process.exit(1);
    }

    //check if input is braille or english
    const output = isBraille(input) ? translateBrailleToEnglish(input) : translateEnglishToBraille(input);
    console.log(output);
}

//execute main function
main();