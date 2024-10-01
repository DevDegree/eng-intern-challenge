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

let translationArray = [];
let translatedString;

function translateToEnglish(braille) {
    let [nextCaps, nextNum] = [false, false];

    let brailleArray = braille.match(/[.O]{1,6}/g) || [];

    let englishArray = brailleArray.reduce((acc, brailleChar) => {
        if (brailleChar === englishToBraille.CAP) nextCaps = true;
        else if (brailleChar === englishToBraille.NUM) nextNum = true;
        else {
            let out;
            if (nextNum) {
                out = brailleToNumbers[brailleChar];
            } else {
                out = brailleToEnglish[brailleChar];

                if (nextCaps) {
                    out = out.toUpperCase();
                    nextCaps = false;
                }

                if (out === " ") nextNum = false;
            }
            acc.push(out);
        }

        return acc;
    }, []);

    return englishArray.join("");
}

function translateToBraille(english) {
    let isNum = false;

    let brailleArray = english.split("").reduce((acc, char) => {
        if (char.match(/[0-9]/)) isNum = true;

        if (!isNum) {
            if (char.match(/[A-Z]/)) acc.push(englishToBraille.CAP);

            acc.push(englishToBraille[char.toLowerCase()]);
        } else {
            acc.push(numbersToBraille[char]);
        }

        return acc;
    }, []);

    return brailleArray.join("");
}

// If the first arg isn't purely .s and/or Os, or it is but isn't at least 6 characters (denoting a valid braille character), then it should be english
if (args[0].match(/[^.O]/) || args[0].length % 6 !== 0) {
    args.forEach((arg) => {
        const translatedArg = translateToBraille(arg);
        translationArray.push(translatedArg);
    });
    translatedString = translationArray.join(englishToBraille[' ']);
} else {
    args.forEach((arg) => {
        const translatedArg = translateToEnglish(arg);
        translationArray.push(translatedArg);
    });
    translatedString = translationArray.join('');
}

console.log(translatedString);