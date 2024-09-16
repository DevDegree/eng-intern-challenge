const brailleToEnglish: { [key: string]: string } = {
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
    "......": " ", 
    ".....O": "CAPITAL", 
    ".O...O": "DECIMAL", 
    ".O.OOO": "NUMBER"
};

const digitToBraille: { [key: string]: string } = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
};

const englishToBraille: { [key: string]: string } = {};
for (const braille in brailleToEnglish) {
    if (brailleToEnglish.hasOwnProperty(braille)) {
        const english = brailleToEnglish[braille];
        englishToBraille[english] = braille;
    }
}

const brailleToDigit: { [key: string]: string } = {};
for (const digit in digitToBraille) {
    if (digitToBraille.hasOwnProperty(digit)) {
        brailleToDigit[digitToBraille[digit]] = digit;
    }
}

function translateEnglishToBraille(input: string): string {
    let isNumber = false;

    const brailleOutput = input.split('').map(char => {        
        if (char === ' ') {
            isNumber = false;  
            return englishToBraille[" "]; 
        }

        if (char >= '0' && char <= '9') {
            const brailleChar = digitToBraille[char];
            if (!isNumber) {
                isNumber = true;
                return englishToBraille["NUMBER"] + brailleChar;
            } else {
                return brailleChar;
            }
        } else {
            isNumber = false;  

            if (char === char.toUpperCase()) {
                return englishToBraille["CAPITAL"] + englishToBraille[char.toLowerCase()];
            } else {
                return englishToBraille[char.toLowerCase()] ;  
            }
        }
    }).join('');

    return brailleOutput + (input.endsWith(' ') ? englishToBraille[" "] : '');
}

function splitBrailleString(braille: string): string[] {
    const brailleChars: string[] = [];
    
    for (let i = 0; i < braille.length; i += 6) {
        brailleChars.push(braille.substring(i, i + 6));
    }
    
    return brailleChars;
}


function translateBrailleToEnglish(braille: string): string {
    const brailleChars = splitBrailleString(braille);

    let isCapital = false;
    let isNumber = false;
    let result = '';

    brailleChars.forEach(symbol => {
        if (symbol === englishToBraille["CAPITAL"]) {
            isCapital = true;
        } else if (symbol === englishToBraille["NUMBER"]) {
            isNumber = true;
        } else if (symbol === brailleToEnglish["......"]) {  
            isNumber = false; 
            result += ' ';
        } else {
            let char;
            if (isNumber) {
                char = brailleToDigit[symbol] ;
            } else {
                char = brailleToEnglish[symbol] ;
            }

            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }

            result += char;
        }
    });

    return result;
}

const args = process.argv.slice(2);  

const input = args.join(' ');
let output: string;

if (input.match(/^[0-9a-zA-Z ]+$/)) {
    output = translateEnglishToBraille(input);
} else {
    output = translateBrailleToEnglish(input);
}

console.log(output);