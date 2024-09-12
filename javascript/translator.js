function reverseBraille(brailleAlphabet) {
    let reversed = Object.entries(brailleAlphabet).map(([key, value]) => [value, key]);
    reversed = Object.fromEntries(reversed);
    return reversed;
}

const brailleToEnglish = {
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
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",

    ".....O": "caps",
    ".O.OOO": "number",

    "......": " "
};

const brailleNumbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
};

const englishToBraille = reverseBraille(brailleToEnglish);
const englishToBrailleNumbers = reverseBraille(brailleNumbers);

function determineInputtedLanguage(userInput) {
    const regex = /^[O.]+$/;

    // If input contains only 'O' and '.', then the inputted language is braille
    if (regex.test(userInput)) {
        if (userInput.length % 6 == 0) {
            translateBrailleToEnglish(userInput);
        }
        else {
            console.log("There is an issue with the inputted Braille string. Please make sure each character has a length of 6.");
            return;
        }
    }
    else {
        translateEnlishToBraille(userInput);
    }
}

const brailleStringSize = 6;

function translateBrailleToEnglish(userInput) {
    let output = "";
    let isNumber = false;
    let capsNext = false;

    for (let i = 0; i < userInput.length; i += brailleStringSize) {
        let letter = userInput.substring(i, i + brailleStringSize);

        if (brailleToEnglish[letter] === undefined) {
            console.log("There is an issue with the inputted Braille string. Please make sure your input is a valid Braille character.");
            return;
        }

        if (brailleToEnglish[letter] == " ") {
            isNumber = false;
        }

        // Check for special cases of capital, and number

        if (brailleToEnglish[letter] == "caps") {
            capsNext = true;
        }

        else if (brailleToEnglish[letter] == "number") {
            isNumber = true;
        }

        else {
            if (isNumber) {
                output += brailleNumbers[letter];
                capsNext = false;
            }
            else if (capsNext) {
                output += brailleToEnglish[letter].toUpperCase();
                capsNext = false;
            }
            else {
                output += brailleToEnglish[letter];
            }
        }
    }

    // Log the translated string
    console.log(output);
}

function translateEnlishToBraille(userInput) {
    let output = "";
    let isNumber = false;

    for (let i = 0; i < userInput.length; i++) {
        let letter = userInput.substring(i, i + 1);

        // Check if space (to reset number)
        if (letter == " ") {
            isNumber = false;
            output += englishToBraille[letter];
        }

        // Check if number
        else if (!isNaN(parseFloat(letter))) {
            if (isNumber) {
                output += englishToBrailleNumbers[letter];
            }
            else {
                isNumber = true;
                output += englishToBraille["number"] + englishToBrailleNumbers[letter];
            }
        }

        // Check if character exists in object (at this point in if else, only letters (upper and lower case) as well as invalid characters are left to check for)
        else if (englishToBraille[letter.toLowerCase()] === undefined) {
            console.log("There is an issue with the inputted English string. Please make sure your input has all valid English characters.");
            return;
        }

        // Check if capital letter
        else if (letter == letter.toUpperCase()) {
            output += (englishToBraille["caps"] + englishToBraille[letter.toLowerCase()]);
        }

        else {
            output += englishToBraille[letter.toLowerCase()];
        }
    }

    // Log the translated string
    console.log(output);
}

// If a string is given when running the program, use that string. Otherwise, prompt the user to enter
const inputArgument = process.argv.slice(2).join(' ');

if (inputArgument) {
    determineInputtedLanguage(inputArgument);
}
else {
    const readline = require('readline');

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter your string: ', (input) => {
        determineInputtedLanguage(input);
        rl.close();
    });
}
