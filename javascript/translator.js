const alphabetToBraille = {
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
    " ": "......",
    capital: ".....O",
    number: ".O.OOO"
};

const brailleToAlphabet = {
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
    "......": " ",
    ".....O": "capital",
    ".O.OOO": "number",
};

const brailleToNumbers = {
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
};

const braille = /[O.]/gm;

function translator(argArray) {
    argArray.shift();
    argArray.shift();
    let translation = "";
    if (braille.test(argArray)) {
        translation = translateToAplhabet(argArray).join("");
    } else {
        translation = translateToBraille(argArray).join("");
    }
    console.log(translation);
}

const translateToBraille = (argArray) => {
    let lettersToTranslate = argArray.map((arr) => {
        return [...arr.split(""), " "];
    });
    lettersToTranslate = lettersToTranslate.flat();
    lettersToTranslate.pop();

    let isANumber = false;
    return lettersToTranslate.map((e) => {
        if (e === " ") {
            isANumber = false;
            return alphabetToBraille[e];
        }
        if (!isNaN(e * 1)) {
            if (!isANumber) {
                isANumber = true;
                return alphabetToBraille["number"] + alphabetToBraille[e];
            } else {
                return alphabetToBraille[e];
            }
        } else {
            if (e === e.toUpperCase() && e !== " ") {
                return (
                    alphabetToBraille["capital"] + alphabetToBraille[e.toLowerCase()]
                );
            }
        }
        return alphabetToBraille[e];
    });
};

const translateToAplhabet = (argArray) => {
    const brailleArray = argArray.toString().match(/.{1,6}/g);

    let isANumber = false;
    let isCapital = false;

    return brailleArray.map((e) => {
        if (e === "......") {
            isANumber = false;
            return brailleToAlphabet[e];
        }
        if (e === ".O.OOO") {
            isANumber = true;
            return "";
        }

        if (isANumber) return brailleToNumbers[e];

        if (e === ".....O") {
            isCapital = true;
            return "";
        } else {
            if (isCapital) {
                isCapital = false;
                return brailleToAlphabet[e].toUpperCase();
            }
        }
        return brailleToAlphabet[e];
    });
};

translator(process.argv);