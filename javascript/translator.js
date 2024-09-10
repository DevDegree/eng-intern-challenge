const letters = {
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    " ":"......",
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    "(":"O.O..O",
    ")":".O.OO.",
    "cap":".....O",
    "num":".O.OOO", 
}
const brailleToLetters = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    ".....O": "cap",
    ".O.OOO": "num",
};

const numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO.."
}

function toBraille(text) {
    let result = "";
    let inNumberSequence = false;  // Flag to track if we are in a sequence of numbers

    for (let i = 0; i < text.length; i++) {
        let char = text[i];

        if (!isNaN(char) && numbers[char]) {  // Check if the character is a number
            if (!inNumberSequence) {  // Add number indicator only once at the start
                result += letters["num"];
                inNumberSequence = true;  // Set the flag to true
            }
            result += numbers[char];  // Add the Braille representation of the number
        } else {
            // If we're currently in a number sequence, reset the flag
            if (inNumberSequence) {
                inNumberSequence = false; 
            }

            if (char === char.toUpperCase() && letters[char.toLowerCase()] && char !== " ") {
                result += letters["cap"];
                result += letters[char.toLowerCase()];
            } else if (letters[char]) {
                result += letters[char]; 
            }
        }
    }

    return result;
}


function toText(text) {
    let result = "";
    let isCap = false;
    let isNum = false;

    for (let i = 0; i < text.length; i += 6) {
        let char = text.slice(i, i + 6);

        if (char === letters["cap"]) {
            isCap = true; 
            continue; 
        }
        else if(char === letters["num"]) {
            isNum = true;
            continue;
        }

        if(isNum){
            for (let key in numbers) {
                if (numbers[key] === char) {
                    result += key;
                }
                if(char === letters[" "]){
                    isNum = false;
                    result += " ";
                    break;
                }
            }
        }
        else {
            if (isCap) {
                result += brailleToLetters[char].toUpperCase();
                isCap = false;
            } else {
                result += brailleToLetters[char];
            }
        }
    }

    return result;
}

function translate(input) {
    const braillePattern = /^[O.]{6}$/; 
    const chunks = input.match(/.{1,6}/g);  

    
    const isBraille = chunks.every(chunk => braillePattern.test(chunk));

    if (isBraille) {
        return toText(input);
    } else {
        return toBraille(input);
    }
}