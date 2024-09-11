let words = process.argv.slice(2);

const brailleCharacters = {
    alphabet: {
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
    },
    numbers: {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
    },
    punctuation: {
        "..OO.O": ".",
        "..O...": ",",
        "..O.OO": "?",
        "..OOO.": "!",
        "..OO..": ":",
        "..O.O.": ";",
        "....OO": "-",
        ".O..O.": "/",
        ".OO..O": "<",
        "O..OO.": ">",
        "O.O..O": "(",
        ".O.OO.": ")",
        "......": " ",
    },
    follows: {
        ".....O": "capital",
        ".O...O": "decimal",
        ".O.OOO": "number",
    },
};

const checkIsBraille = (str) => {
    if (str.length % 6 !== 0) {
        return false;
    }
    if (!/^[O.]+$/.test(str)) {
        return false;
    }
    return true;
};

const main = (words) => {
    let output = "";
    let isNum = false;
    let isCapital = false;
    if (checkIsBraille(words[0])) {
        for (let i = 0; i < words[0].length; i += 6) {
            const brailleChar = words[0].substring(i, i + 6);
            if (brailleCharacters.follows[brailleChar] === "number") {
                isNum = true;
            } else if (brailleCharacters.follows[brailleChar] === "capital") {
                isCapital = true;
            } else {
                if (isNum) {
                    if (brailleCharacters.numbers[brailleChar]) {
                        output += brailleCharacters.numbers[brailleChar]; // Add the number
                    }
                } else if (brailleCharacters.punctuation[brailleChar]) {
                    output += brailleCharacters.punctuation[brailleChar];
                    if (brailleCharacters.punctuation[brailleChar] === " ") {
                        isNum = false;
                    }
                } else if (brailleCharacters.alphabet[brailleChar]) {
                    let alphabet = brailleCharacters.alphabet[brailleChar];
                    if (isCapital) {
                        alphabet = alphabet.toUpperCase();
                        isCapital = false;
                    }
                    output += alphabet;
                } else {
                }
            }
        }
    } else {
        // convert words to braille
        console.log("is not braille");
    }

    console.log(output);
};
main(words);
