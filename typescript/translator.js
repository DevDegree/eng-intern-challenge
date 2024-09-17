"use strict";
// collect input, with node and file/path removed
const input = process.argv.slice(2);
// establish a string to return to user
let output = "";
const notBraileExp = /[^\.O]/;
// handle no input
if (!input.length) {
    console.error("Error: Please add a valid input of either Braile or English");
    process.exit(1);
}
// determine if input is braile or English
function isItBraile() {
    // only uses . and O characters
    if (notBraileExp.test(input[0]))
        return false;
    // should only be one string
    if (input.length > 1)
        return false;
    // stretch goal: add notification to user not to use spaces when entering braile
    // should be evenly divisible by 6 (no spaces)
    if (input[0].length % 6 != 0)
        return false;
    // stretch goal: add notification to user to check all their braile characters are complete
    else
        return true;
}
const translationConfig = {
    modifiers: {
        "capital follows": ".....O",
        "number follows": ".O.OOO",
    },
    numbers: {
        // (same as a-j)
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
    },
    letters: {
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
        " ": "......", // space
    }
};
// const numbers: { [key: string]: string } = {
//   // (same as a-j)
//   "1": "O.....",
//   "2": "O.O...",
//   "3": "OO....",
//   "4": "OO.O..",
//   "5": "O..O..",
//   "6": "OOO...",
//   "7": "OOOO..",
//   "8": "O.OO..",
//   "9": ".OO...",
//   "0": ".OOO..",
// }
const letters = {
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
    " ": "......", // space
};
// establish regex to identify letters or numbers
const capitalExp = /[A-Z]/;
const numberExp = /[0-9]/;
// establish variables to hold modifier status
let isCapitalFollows = false;
let isNumberFollows = false;
function translateBraileToEnglish() {
    let english = "";
    // break input into strings of six characters
    let characters = [];
    const braileLetters = input[0].matchAll(/[O\.]{6}/g);
    for (let match of braileLetters)
        characters.push(match[0]);
    // parse each character into english, allowing for "x follows" modifiers
    characters.forEach((char) => {
        // if character is a space, end "number follows" modifier and add space
        if (char == letters[" "]) {
            isNumberFollows = false;
            english += " ";
            return;
        }
        // if it's "number follows", set numLock to true
        if (char == translationConfig.modifiers["number follows"])
            isNumberFollows = true;
        // if it's "capital follows", set capsLock to true (otherwise reset to false)
        if (char == translationConfig.modifiers["capital follows"])
            isCapitalFollows = true;
        // if numLock is true, translate from number definitions
        if (isNumberFollows) {
            for (let n in translationConfig.numbers)
                if (char == translationConfig.numbers[n])
                    english += n;
        }
        else {
            // otherwise, translate from letter definitions
            for (let l in letters) {
                if (char == letters[l]) {
                    if (isCapitalFollows) {
                        english += l.toUpperCase();
                        isCapitalFollows = false;
                    }
                    else
                        english += l;
                }
            }
        }
    });
    return english;
}
function translateEnglishToBraile() {
    // convert input into array of individual characters
    const characters = input.join(" ").split("");
    // create an empty string to return;
    let braile = "";
    // check if next character is a capital or a number, add appropriate braile
    characters.forEach((character) => {
        // if character is a space, turn off numLock
        if (character == " ")
            isNumberFollows = false;
        // if character is a number, and numLock is false add "numbers follows";
        if (numberExp.test(character)) {
            if (!isNumberFollows) {
                braile += translationConfig.modifiers["number follows"];
                isNumberFollows = true;
            }
            // parse the number into braile
            braile += translationConfig.numbers[character];
        }
        else {
            // if character is a capital, add "capital follows";
            if (capitalExp.test(character))
                braile += translationConfig.modifiers["capital follows"];
            // parse the character into braile
            if (letters[character.toLowerCase()] !== undefined)
                braile += letters[character.toLowerCase()];
            // add a flag for undefined characters (e.g. punctuation)
        }
    });
    return braile;
}
if (isItBraile())
    output = translateBraileToEnglish();
else
    output = translateEnglishToBraile();
console.log(output);
process.exit(0);
