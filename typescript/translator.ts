
function isBraille(input: string): boolean {
    const len: number = input.length;
    const regex: RegExp = /[\da-zA-NP-Z,!?:;<>()\/\-\s]/;

    // any Braille input will always need to be at least 6 chars long, or a multiple of 6
    if (len < 6 || (len % 6) !== 0) {
        return false;
    }
    // any input containing letters (except O), numbers, symbols (except .), and spaces " " is English
    if (regex.test(input) === true) {
        return false;
    }
    return true;
}

const engObj: { [key: string] : string } = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....",
    "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...",
    "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...",
    "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.",
    "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.",
    "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.",
    "s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO",
    "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
    "y" : "OO.OOO", "z" : "O..OOO", "0" : ".OOO..",
    "1" : "O.....", "2" : "O.O...", "3" : "OO....",
    "4" : "OO.O..", "5" : "O..O..", "6" : "OOO...",
    "7" : "OOOO..", "8" : "O.OO..", "9" : ".OO...",
    " " : "......", "capital" : ".....O", "num" : ".O.OOO"
};

const brObj: { [key: string] : string } = {};
for (let key in engObj) {
    brObj[engObj[key]] = key;
}

// we know whether the input is in Braille or English by this point, string is separated
function englishToBraille(englishArr: string[]): string {
    let translatedStr: string = "";
    const isUpperCase = (str: string): boolean => /^[A-Z]$/.test(str);
    const isNum = (str: string): boolean => /^[0-9]$/.test(str);

    for (let i = 0; i < englishArr.length; i++) {
        if (isUpperCase(englishArr[i])) {
            translatedStr += (engObj["capital"] + engObj[englishArr[i].toLowerCase()]);
            continue;
        }
        // if the char is a number and if it is the first char or not adjacent to another number, we need
        // the 'number follows' braille symbol as well
        if (isNum(englishArr[i]) && (i === 0 || (i > 0 && !isNum(englishArr[i - 1])))) {
            translatedStr += (engObj["num"] + engObj[englishArr[i]]);
            continue;
        }
        // console.log(englishArr[i]);
        translatedStr += engObj[englishArr[i]];
    }
    return translatedStr;
}

function brailleToEnglish(brailleArr: string[]): string {
    let translatedStr: string = "";
    let capital: boolean = false;

    for (let i = 0; i < brailleArr.length; i++) {
        if (brObj[brailleArr[i]] === "capital") {
            capital = true;
        }
        if (capital) {
            translatedStr += (brObj[brailleArr[i]].toUpperCase());
            capital = false;
        }
        if (brObj[brailleArr[i]] !== "num") {
            translatedStr += (brObj[brailleArr[i]]);
        }
    }
    return translatedStr;
}

function translate(input: string): string {
    if (isBraille(input)) {
        const splitRegex: RegExp = /.{6}/g;
        const brailleMatch = input.match(splitRegex)
        const brailleArr = brailleMatch ? brailleMatch : [];
        // console.log(brailleToEnglish(brailleArr));
        return brailleToEnglish(brailleArr);
    }
    const englishArr: string[] = input.split("");
    // console.log(englishToBraille(englishArr));
    return englishToBraille(englishArr);
}

console.log(translate((process.argv.slice(2)).join(" ")));