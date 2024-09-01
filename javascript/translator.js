#!/usr/bin/env node

const braille = {
    a: "O.....",
    b: "O.O...",
    c: "OO....",
    d: "OO.O..",
    e: "O..O..",
    f: "OOO...",
    g: "OOOO..",
    h: "O.OO..",
    i: ".OO...",
    j: ".OOO..",
    k: "O...O.",
    l: "O.O.O.",
    m: "OO..O.",
    n: "OO.OO.",
    o: "O..OO.",
    p: "OOO.O.",
    q: "OOOOO.",
    r: "O.OOO.",
    s: ".OO.O.",
    t: ".OOOO.",
    u: "O...OO",
    v: "O.O.OO",
    w: ".OOO.O",
    x: "OO..OO",
    y: "OO.OOO",
    z: "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "O": ".OOO..",
    " ": "......",
};

// Gather user input when running the program

const input = process.argv.slice(2).join(" ");

// Establish whether the string is braille or plain English

const isBraille = (string) => {
    const brailleSyntax = /^[O. ]+$/
    return brailleSyntax.test(string)
}

// Function tha translates from Braille to English

const translateFromBraille = (userInput) => {
    const capitalMarker = ".....O";
    const numericMarker = ".O.OOO";
    let isCapital = false;
    let result = "";
    const chunks = userInput.match(/.{1,6}/g);
    const alphabet = Object.fromEntries(Object.entries(braille).map(([k, v]) => [v, k]));
    chunks.map(chunk => {
        if (chunk === numericMarker) {
            null;
        } else if (chunk === capitalMarker) {
            isCapital = true;
        } else if (isCapital) {
            result+=alphabet[chunk].toUpperCase();
            isCapital = false;
        } else {
            result+=alphabet[chunk];
        }
    })
    console.log(result)
}

// Function tha translates from English to Braille

const translateFromEnglish = (userInput) => {
    const chars = userInput.split("");
    const isCapital = /^[A-Z]$/;
    const isNumber = /^[0-9]$/;

    let isNumberSequence = false;
    let result = "";

    chars.map(char => {
        if (isCapital.test(char)) {
            result+=".....O";
            isNumberSequence = false;
            result+=braille[char.toLowerCase()];
        } else if (isNumber.test(char)) {
            if (!isNumberSequence) {
                result += ".O.OOO"
                isNumberSequence = true;
            }
            result+=braille[char];
        } else {
            result+=braille[char];
            isNumberSequence = false;
        }
    })
    console.log(result);
}

if (isBraille(input)) {
    translateFromBraille(input);
} else {
    translateFromEnglish(input);
}

