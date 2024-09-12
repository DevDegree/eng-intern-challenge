const letterArray = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    [".", ",", "?",  "!", ":", ";", "-", "/", "<", ">", "(", ")", " "],
    ["caps", "deci", "num"]
];

const brailleArray = [
    ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
    "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
    "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"],

    ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."],

    ["..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.", "....OO", ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO.", "......"],
    [".....O", ".O...O", ".O.OOO"]
];

const numberBraille = brailleArray[3][2];
const capitalBraille = brailleArray[3][0];

function isDigit(char) {
    return /[0-9]/.test(char);
}

function isUpperCase(char) {
    return /[A-Z]/.test(char);
}

function isLetter(char) {
    return /[a-z]/i.test(char);
}

function isLetterAToJ(char) {
    return /[a-j]/.test(char);
}

function charToBraille(char) {
    for (let i = 0; i < letterArray.length; i++) {
        let index = letterArray[i].indexOf(char);

        if (index !== -1) {
            return brailleArray[i][index];
        }
    }
    return char;
}

function brailleToChar(braille) {
    for (let i = 0; i < brailleArray.length; i++) {
        let index = brailleArray[i].indexOf(braille);

        if (index !== -1) {
            return letterArray[i][index];
        }
    }
    return braille;
}

function letterToNumber(char) {
    return String(letterArray[1][letterArray[0].indexOf(char.toLowerCase())]);
}

function toBraille(text) {
    let braille = "";
    let isNumber = false;

    for (let char of text) {
        if (isDigit(char) && !isNumber) {
            braille += numberBraille;
            isNumber = true;
        } else if (!isDigit(char)) {
            isNumber = false;
        }

        if (isUpperCase(char)) {
            braille += capitalBraille;
            char = char.toLowerCase();
        }

        braille += charToBraille(char);
    }

    return braille;
}

function toText(braille) {
    let text = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const pattern = braille.slice(i, i + 6);

        if (pattern === capitalBraille) {
            isCapital = true;
            continue;
        }

        if (pattern === numberBraille) {
            isNumber = true;
            continue;
        }

        let char = brailleToChar(pattern);

        if (isCapital && isLetter(char)) {
            char = char.toUpperCase();
            isCapital = false;
        }

        if (isNumber && isLetterAToJ(char)) {
            char = letterToNumber(char);
        } else {
            isNumber = false;
        }

        text += char;
    }

    return text;
}

function main() {
    const args = process.argv.slice(2);
    const input = args.join(" ");

    if (/^[O\.]+$/.test(input)) {
        console.log(toText(input));
    } else {
        console.log(toBraille(input));
    }
}

main();