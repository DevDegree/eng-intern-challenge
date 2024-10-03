const letterToBraille = {
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
    "CAPITAL": ".....O",
    "NUMBER": ".O.OOO",
    " ": "......"
};

const numberToBraille = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    " ": "......",
    "NUMBER": ".O.OOO"
};

const brailleToLetter = Object.fromEntries(
    Object.entries(letterToBraille).map(([key, value]) => [value, key])
);

const brailleToNumber = Object.fromEntries(
    Object.entries(numberToBraille).map(([key, value]) => [value, key])
);

// convert braille to english
function convertBraille(input) {
    let nextCapital = false;
    let nextNumber = false;
    let result = "";
    let letter;

    for (let i = 0; i < input.length; i+= 6) {
        let braille = input.slice(i, i+ 6); // get next 6 characters

        if (nextNumber == true) {
            letter = brailleToNumber[braille];
            if (letter == " ") {
                nextNumber = false; 
            }
            result += letter;  
        } else {
            letter = brailleToLetter[braille];

            if (letter == "NUMBER") {
                nextNumber = true;
                continue;
            }
            if (letter == "CAPITAL") {
                nextCapital = true;
                continue;
            }
            if (nextCapital == false && nextNumber == false) {
                result += letter;
            }
            if (nextCapital == true) {
                result += letter.toUpperCase();
                nextCapital = false;
            }
        }
    }
    return result;
};

// convert english to braille
function convertLetter(input) {
    let nextNumber = false;
    let result = "";
    let braille = ""; 

    for (let i = 0; i < input.length; i++) {
        let letter = input.slice(i, i+1);

        if (/^[0-9 ]$/.test(letter)) {
            braille = numberToBraille[letter];
            
            if (braille == numberToBraille[" "]) {
                nextNumber = false;
                result += numberToBraille[" "];
                continue; 
            }
            if (nextNumber == false) {
                nextNumber = true;
                result += numberToBraille["NUMBER"];
            }
        } else if (/^[A-Z]$/.test(letter) && letter != null) {
                result += letterToBraille["CAPITAL"];
                braille = letterToBraille[letter.toLowerCase()];
        } else {
            braille = letterToBraille[letter];  
        }
        result += braille;
    }    
    return result;
};

const args = process.argv.slice(2);
const input = args.join(' ');

function isBraille(input) {
    return /^[O.]+$/.test(input);
};

let translated;
if (isBraille(input)) {
    translated = convertBraille(input);
} else {
    translated = convertLetter(input);
}
console.log(translated);