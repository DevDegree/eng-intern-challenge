#!/usr/bin/env node

/* 
1. Create a translator that will translate Braille to English or vice-versa
    - Translator will determine which direction to translate depending on the argument passed
        - E.g., if the argument is Braille, it will return the English equivalent

2. Input: Braille, output: English OR input: English, output: Braille

3. Each Braille character is stored as a series of 'O" (letter) or "."
    - 0 = raised dot

4. Braille alphabet will include:
    - Letters "a" to "z"
    - Ability to capitalize letters
    - Numbers "0" to "9"
    - Ability to include "spaces" to make multiple words

5. Keywords:
    - Terminal/command line (CL) application
    - Translate/convert to the appropriate opposite
    - Argument = string to be translated
        - Therefore this terminal/CL application will have one parameter, string?

6. Notes:
    - Braille is read from left to right
    - Braille letters A to J are used to identify numbers in Braille

Steps:
    - Create a dictionary where each character corresponds with its letter equivalent
        - Include marker for capitalization and for numbers
        - Remember Braille numbers have the same raised dots as the first 10 Braille letters
    - Create dynamic object to reverse map alphabet and numbers
    - Function A will translate English to Braille by:
        - Taking a string (in English) as an argument
        - Checking if a character in the string is capitalized, a number, or has a space
            - If capitalized, a number, or has a space: append marker then append associated character
                - Note: If capitalized, make sure to return it to lowercase before appending
                        since Braille by default is lower case. Marker will indicate if the character
                        immediately following it is capitalized
        - Appending regular (lowercase) characters
            - These are characters that do not pass the checks
    - Function B will translate Braille to English by:
        - Taking a string (in Braille) as an argument
        - Iterating over the string by 6 increments and extracting 6 characters at a time
            - A single Braille character = 6 dots
        - Checking for capital and number markers
            - If present, set associated state to true
        - Checking for spaces
            - If present, append space
        - Append characters based on checks
    - Function C will determine if string input is Braille or not
    = Function D will determine which translator to use based on the output of Function C
*/

const englishAlphabet = {
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
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO"
};

const numbers = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j"
};

// initializes empty objects
const reversedCharacters = {};
const reversedNumbers = {};

Object.keys(englishAlphabet).forEach(key => {
    reversedCharacters[englishAlphabet[key]] = key;
});

Object.keys(numbers).forEach(key => {
    reversedNumbers[numbers[key]] = key;
});

// translates English to Braille
const translateEnglishToBraille = (text) => {
    let translatedText = ""; 
    let isNumber = false;

    for (let i = 0; i < text.length; i++) {
        let brailleChar = "";
        let englishChar = text[i];

        // resets number marker
        if (englishChar === " ") {
            translatedText += englishAlphabet[" "];
            isNumber = false;
            continue;
        };

        // checks if a character is a number
        if (!isNaN(englishChar) && englishChar !== " ") {
            if (!isNumber) {
                translatedText += englishAlphabet["number"]; // adds number marker
                isNumber = true;
            };
            brailleChar = englishAlphabet[numbers[englishChar]];
        } else {
            // checks if a character is capitalized
            if (englishChar === englishChar.toUpperCase()) {
                translatedText += englishAlphabet["capital"]; // adds capitalization marker
                englishChar = englishChar.toLowerCase();
            };
            brailleChar = englishAlphabet[englishChar];
            isNumber = false;
        };
        translatedText += brailleChar;
    };
    return translatedText;
};

const translateBrailleToEnglish = (text) => {
    let translatedText = "";
    let isNumber = false;
    let isCapital = false;

    for (let i = 0; i < text.length; i += 6) {
        let brailleChar = text.slice(i, i + 6); // extracts Braille characters (6)
        let englishChar = reversedCharacters[brailleChar];

        // checks for number marker
        if (brailleChar === englishAlphabet["number"]) {
            isNumber = true;
            continue;
        };

        // checks for capitalization marker
        if (brailleChar === englishAlphabet["capital"]) {
            isCapital = true;
            continue;
        };

        // checks for space
        if (brailleChar === englishAlphabet[" "]) {
            translatedText += " ";
            isNumber = false;
            continue;
        };

        if (isNumber) {
            if (englishChar in reversedNumbers) {
                translatedText += reversedNumbers[englishChar];
            }
        } else {
            if (isCapital) {
                translatedText += englishChar.toUpperCase();
                isCapital = false;
            } else {
                translatedText += englishChar;
            };
        };
    };
    return translatedText;
};

// checks if input is Braille
const isBraille = (text) => {
    const brailleCheck = /^[O.]*$/;
    return brailleCheck.test(text);
};

// main translate function - the Braille check will determine which function to run
function translate(text) {
    if (isBraille(text)) {
        return translateBrailleToEnglish(text);
    } else {
        return translateEnglishToBraille(text);
    };
};

// retrieves input from command-line arguments --> this was a learning curve! So cool!
const inputText = process.argv[2]; // retrieves command-line argument from input
const outputText = translate(inputText); // passes command-line argument into main translate function
console.log("The translation is:", outputText); // logs result