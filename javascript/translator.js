const args = process.argv.slice(2);

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
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "CAP", // next character is a capital letter
    ".O.OOO": "NUM", // next character is a number
    "......": " ",
};

const brailleToNumbers = {
    "O.....": 1,
    "O.O...": 2,
    "OO....": 3,
    "OO.O..": 4,
    "O..O..": 5,
    "OOO...": 6,
    "OOOO..": 7,
    "O.OO..": 8,
    ".OO...": 9,
    ".OOO..": 0,
};

const englishToBraille = Object.entries(brailleToEnglish).reduce(
    (acc, [key, value]) => {
        acc[value] = key;
        return acc;
    },
    {}
);
const numbersToBraille = Object.entries(brailleToNumbers).reduce(
    (acc, [key, value]) => {
        acc[value] = key;
        return acc;
    },
    {}
);

let translatedString;

function translateToEnglish(braille) {
    let [nextCaps, nextNum] = [false, false];

    let brailleArray = braille.match(/[.O]{1,6}/g) || [];

    let englishArray = brailleArray.reduce((acc, brailleChar) => {
        if (brailleChar === englishToBraille.CAP) nextCaps = true;
        else if (brailleChar === englishToBraille.NUM) nextNum = true;
        else {
            let out;
            if (brailleChar === englishToBraille[" "]) nextNum = false;

            if (!nextNum) {
                out = brailleToEnglish[brailleChar];

                if (nextCaps) {
                    out = out.toUpperCase();
                    nextCaps = false;
                }
            } else {
                out = brailleToNumbers[brailleChar];
            }

            acc.push(out);
        }
        return acc;
    }, []);

    return englishArray.join("");
}

function translateToBraille(english) {
    let numToggled = false;

    let brailleArray = english.split("").reduce((acc, char) => {
        if (char.match(/[0-9]/)) {
            if (!numToggled) {
                acc.push(englishToBraille.NUM);
                numToggled = true;
            }
            acc.push(numbersToBraille[char]);
        } else {
            if (char.match(/[A-Z]/)) acc.push(englishToBraille.CAP);
            acc.push(englishToBraille[char.toLowerCase()]);
        }

        return acc;
    }, []);

    return brailleArray.join("");
}

if (args[0].match(/[^.O]/) || args[0].length % 6 !== 0 || args[1]) {
    let translationArray = [];
    args.forEach((arg) => {
        const translatedArg = translateToBraille(arg);
        translationArray.push(translatedArg);
    });
    translatedString = translationArray.join(englishToBraille[" "]);
} else {
    translatedString = translateToEnglish(args[0]);
}

console.log(translatedString);
