const process = require('process');

const numberToBraille = {
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

const characterToBraille = {
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

const remainToBraille = {
    "capital": ".....O",
    "number": ".O.OOO",
    " ": "......"
};

const brailleToNumber = Object.fromEntries(Object.entries(numberToBraille).map(([k, v]) => [v, k]));
const brailleToCharacter = Object.fromEntries(Object.entries(characterToBraille).map(([k, v]) => [v, k]));
const brailleToRemain = Object.fromEntries(Object.entries(remainToBraille).map(([k, v]) => [v, k]));

const netBraille = new Set([...Object.keys(brailleToCharacter), ...Object.keys(brailleToNumber), ...Object.keys(brailleToRemain)]);

const inputStr = process.argv.slice(2).join(' ');

function isBraille(s) {
    if (s.length % 6 === 0) {
        const braille = [];

        for (let i = 0; i < s.length; i += 6) {
            braille.push(s.slice(i, i + 6));
        }
        return braille.every(b => netBraille.has(b)) ? braille : false;
    }
    return false;
}

const brailleString = isBraille(inputStr);
let result = "";
let isNumber = false;
let isCapital = false;

if (brailleString) {
    for (const char of brailleString) {
        if (isNumber && brailleToNumber[char]) {
            result += brailleToNumber[char];
        } 
        else {
            if (brailleToRemain[char]) {
                if (isCapital) {
                    throw new Error("Should be followed by an alphabet letter after 'capital follows' braille");
                }
                if (brailleToRemain[char] === "capital") {
                    isCapital = true;
                } 
                else if (brailleToRemain[char] === "number") {
                    isNumber = true;
                } 
                else {
                    result += brailleToRemain[char];
                    isNumber = false;
                }
            } 
            else {
                result += isCapital ? brailleToCharacter[char].toUpperCase() : brailleToCharacter[char];
                isCapital = false;
            }
        }
    }
} 
else {
    for (const char of inputStr) {
        if (isNumber && (!(char == " " || /\d/.test(char)))){
            throw new Error("Invalid character input")
        }
        if (/[a-zA-Z]/.test(char)) {
            if (/[A-Z]/.test(char)) {
                result += remainToBraille["capital"];
            }
            result += characterToBraille[char.toLowerCase()];
        } 
        else if (/\d/.test(char)) {
            if (!isNumber) {
                result += remainToBraille["number"];
                isNumber = true;
            }
            result += numberToBraille[char];
        } 
        else if (char == " ") {
            result += remainToBraille[" "];
            isNumber = false;
        } 
        else {
            throw new Error("Invalid input");
        }
    }
}

console.log(result);