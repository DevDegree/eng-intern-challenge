const process = require('process');

const chrToBraille = {
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
    "z": "O..OOO"
};

const numToBraille = {
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

const othersToBraille = {
    "capital": ".....O",
    "number": ".O.OOO",
    " ": "......"
};

const brailleToChr = Object.fromEntries(Object.entries(chrToBraille).map(([k, v]) => [v, k]));
const brailleToNum = Object.fromEntries(Object.entries(numToBraille).map(([k, v]) => [v, k]));
const brailleToOthers = Object.fromEntries(Object.entries(othersToBraille).map(([k, v]) => [v, k]));

const allBrailles = new Set([...Object.keys(brailleToChr), ...Object.keys(brailleToNum), ...Object.keys(brailleToOthers)]);

const inputStr = process.argv.slice(2).join(' ');

function isBraille(s) {
    if (s.length % 6 === 0) {
        const brailles = [];
        for (let i = 0; i < s.length; i += 6) {
            brailles.push(s.slice(i, i + 6));
        }
        return brailles.every(b => allBrailles.has(b)) ? brailles : false;
    }
    return false;
}

const brailleStr = isBraille(inputStr);
let output = "", isNum = false, isCapital = false;

if (brailleStr) {  // when the input is braille
    for (const b of brailleStr) {
        if (isNum && brailleToNum[b]) {
            output += brailleToNum[b];
        } else {
            if (brailleToOthers[b]) {
                if (isCapital) {
                    throw new Error("Should be followed by an alphabet letter after 'capital follows' braille");
                }
                if (brailleToOthers[b] === "capital") {
                    isCapital = true;
                } else if (brailleToOthers[b] === "number") {
                    isNum = true;
                } else {
                    output += brailleToOthers[b];
                    isNum = false;
                }
            } else {
                output += isCapital ? brailleToChr[b].toUpperCase() : brailleToChr[b];
                isCapital = false;
            }
        }
    }
} else {  // when input is alphabet, number, or space character.
    for (const c of inputStr) {
        if (isNum && (!(c == " " || /\d/.test(c)))){
            throw new Error("Input character is not valid")
        }
        if (/[a-zA-Z]/.test(c)) {
            if (/[A-Z]/.test(c)) {
                output += othersToBraille["capital"];
            }
            output += chrToBraille[c.toLowerCase()];
        } else if (/\d/.test(c)) {
            if (!isNum) {
                output += othersToBraille["number"];
                isNum = true;
            }
            output += numToBraille[c];
        } else if (c == " ") {
            output += othersToBraille[" "];
            isNum = false;
        } else {
            throw new Error("Input character is not valid. Acceptable inputs: alphabet letters, numbers, and space.");
        }
    }
}

console.log(output);
