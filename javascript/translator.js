// map english characters to braille characters
const braille_english = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", 
    h: "O.OO..", i: ".OO...", j: ".OOO..", k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", 
    o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.", u: "O...OO", 
    v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO"
}

// map numbers to braille characters
const braille_number = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

// map special character to braille characters
const braille_special = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
    "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......"
}

// define the special case for capitalized character and when switched to a number
const capital = ".....O";
const decimal = ".O...O";
const number = ".O.OOO";

// translate the braille character input into english text
function brailleToEnglish (input) {
    let isCap = false;
    let isNum = false;
    let ans = "";

    // iterate through the whole input, incrementing by 6 for each character
    for (let i = 0; i < input.length; i+=6) {

        // get the braille representative of a character
        let character = input.substring(i, i+6);

        // handle the case when the next character should be a capitalized character
        if (character == capital){
            isCap = true;
            continue;
        }

        // handle the case when the next character is a number
        if (character == number){
            isNum = true;
            continue;
        }

        // find the letter or number or special character represented by the braille characters
        let letter = Object.keys(braille_english).find(key => braille_english[key] === character);
        let num = Object.keys(braille_number).find(key => braille_number[key] === character);
        let special_char = Object.keys(braille_special).find(key => braille_special[key] === character);

        // handle case when the current character is a letter
        if (letter && !isNum){
            //case when it's a capital letter
            if (isCap) {
                ans += letter.toUpperCase();
                isCap = false;
            }
            else {
                ans += letter;
            }
        }
        // handle case when the current character is a number
        else if (num) {
            ans += num;
        }
        // handle case when the current character is a special character
        else if (special_char) {
            ans += special_char;
        }
        // handle case when the current character does not fit on the braille alphabet
        else {
            return "Invalid Braille character " + character;
        }
    }

    return ans;
}

// translate english input into braille character
function englishToBraille (input) {
    let ans = "";
    let isNum = false;

    // iterate through each character in the input
    for (let char of input) {
        // case when the character is a space
        if (char == " "){
            ans += braille_special[" "];
            isNum = false;
        }
        // case when the character is a capital letter
        else if (/[A-Z]/.test(char)){
            ans += capital;
            ans += braille_english[char.toLowerCase()];
        }
        // case when the character is a lower case letter
        else if (/[a-z]/.test(char)){
            ans += braille_english[char];
        }
        // case when the character is a number
        else if (/[0-9]/.test(char)){
            // not the first time a number appear before a space
            if (isNum) {
                ans += braille_number[char];
            }
            // the first time a number appear after a space
            else {
                ans += number;
                ans += braille_number[char];
                isNum = true;
            }
        }
        // case when the character is a special character
        else if (braille_special[char]){
            ans += braille_special[char];
        }
        else {
            return "Invalid character " + char;
        }
    }

    return ans;
}

// determine if the input is in the form of braille
function isBraille (input) {
    //regular expression that contains only O and .
    const valid = /^[O.]+$/;
    return valid.test(input) && (input.length % 6 == 0);
}

// main function to handle which translation direction it is
function translator () {

    if (process.argv.length > 2){
        // join all the word into a string to store the input exluding node and translator.js
        const input = process.argv.slice(2).join(' ');

        // check if input is in english or braille
        if (isBraille(input)) {
            console.log(brailleToEnglish(input));
        }
        else {
            console.log(englishToBraille(input));
        }
    }
    else {
        console.log("Usage: node translator.js <input>")
    }
}

// call for the main function
translator();