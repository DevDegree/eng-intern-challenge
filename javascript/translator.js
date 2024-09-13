const ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", " ": "......",
};

const BRAILLE_TO_ENG = {};
Object.keys(ENG_TO_BRAILLE).forEach((key) => {
    BRAILLE_TO_ENG[ENG_TO_BRAILLE[key]] = key;
});

const NUM_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
}

const BRAILLE_TO_NUM = {};
Object.keys(NUM_TO_BRAILLE).forEach((key) => {
    BRAILLE_TO_NUM[NUM_TO_BRAILLE[key]] = key;
});

const CAP = ".....O";
const NUM = ".O.OOO";

// returns true if input is braille otherwise returns false
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// translate english input to braille
function englishToBraille(input) {
    let output = "";
    let numberFollows = false;

    for (let char of input) {
        if (/[A-Z]/.test(char)) {
            output += CAP + ENG_TO_BRAILLE[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!numberFollows) {
                output += NUM;
                numberFollows = true;
            }
            output += NUM_TO_BRAILLE[char];
        } else if (char === " ") {
            numberFollows = false;
            output += ENG_TO_BRAILLE[" "];
        } else {
            numberFollows = false;
            output += ENG_TO_BRAILLE[char];
        }
    }

    return output;
}

// translate braille input to english
function brailleToEnglish(input) {
    let output = "";
    let numberFollows = false;
    let capitalFollows = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i+6);
    
        if (brailleChar === CAP) {
            capitalFollows = true;
            continue;
        } else if (brailleChar === NUM) {
            numberFollows = true;
            continue;
        } else if (brailleChar === ENG_TO_BRAILLE[" "]) {
            numberFollows = false;
            output += " ";
            continue;
        }

        if (capitalFollows) {
            output += BRAILLE_TO_ENG[brailleChar].toUpperCase();
            capitalFollows = false;
        } else if (numberFollows) {
            output += BRAILLE_TO_NUM[brailleChar];
        } else {
            output += BRAILLE_TO_ENG[brailleChar];
        }
    }

    return output;
}

function main() {
    const input = process.argv.slice(2).join(" ");

    if (isBraille(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
}

main();