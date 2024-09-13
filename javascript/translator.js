#!/usr/bin/env node

const charToBraile = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".O.O..",
    "j": ".OO...",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".O.OO.",
    "t": ".OO.O.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "number": ".O.OOO",
    "capital": ".....O",
    ' ': '......',
    '0': '.....O',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.O.O..',

};
//O.....O.O...OO.... lowercase abc
// .....OO.....O.O...OO.... uppercase ABC


const braileToChar = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".O.O..": "i",
    ".OO...": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".O.OO.": "s",
    ".OO.O.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".O.OOO": "number",
    ".....O": "capital",
    '......': ' ',
    '.....O': '0',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.O.O..': '9',
};


function toBraile(input) {
    let result = "";
    let isNum = false;
    //check if the character is uppercase, if so add the capital letter to the result
    for (let i = 0; i < input.length; i++) {
        let char = input[i];
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            result += charToBraile["capital"];
            char = char.toLowerCase();
        }
        if (char >= '0' && char <= '9') {
            if (!isNum) {
                result += charToBraile["number"];
                isNum = true;
            }
            result += charToBraile[char];
        } else {
            isNum = false;
            console.log(char);
            result += charToBraile[char] || charToBraille[' '];;
        }
    }
    return result;
}

function toChar(input) {
    return input
        .match(/.{6}/g)
        .map(braile => braileToChar[braile] || "?")
        .join("");
}

function main() {
    const args = process.argv.slice(2); // Skip the first two arguments (node and script path)
    console.log(args);
    const input = args.join(' '); // Join all arguments into a single string
    
    // Check if the input is a sequence of O and . characters
    if (input.match(/^[O.]+$/)) {
        console.log(toChar(input));
    }
    else {
        console.log(toBraile(input));
    }
}

main();