// mapping for braille alphabet & number
var brailleLetters = {
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
    ".....O": "capatilized",
    "......": " ",
};
var brailleNumbers = {
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
var englishToBraille = {
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
    capatilized: ".....O",
    number: ".O.OOO",
    " ": "......",
};
// Check if input is correct i.e. braille
function isBraille(input) {
    return /^[O.]+$/.test(input) && input.length % 6 === 0;
}
// check if input is english
function isValidEnglish(input) {
    return /^[a-zA-Z0-9 ]+$/.test(input);
}
// Func for braille to English conversion
function translateBrailleToEnglish(braille) {
    var result = "";
    var brailleChars = braille.match(/.{1,6}/g) || []; // diving braille into 6 characters
    var capatilizedNext = false;
    var isNumber = false;
    for (var _i = 0, brailleChars_1 = brailleChars; _i < brailleChars_1.length; _i++) {
        var char = brailleChars_1[_i];
        if (char === ".....O") {
            capatilizedNext = true;
            continue;
        }
        else if (char === ".O.OOO") {
            isNumber = true;
            continue;
        }
        var englishChar = isNumber ? brailleNumbers[char] : brailleLetters[char];
        if (capatilizedNext && englishChar) {
            englishChar = englishChar.toUpperCase();
            capatilizedNext = false;
        }
        // check if number
        if (isNumber && !/[0-9]/.test(englishChar)) {
            isNumber = false;
        }
        result += englishChar || "";
    }
    return result;
}
// Func for English to Braille Conversion
function translateEnglishToBraille(english) {
    var result = "";
    var isNumber = false;
    for (var _i = 0, _a = english.split(""); _i < _a.length; _i++) {
        var char = _a[_i];
        if (/[A-Z]/.test(char)) {
            result += englishToBraille["capatilized"];
            char = char.toLowerCase();
        }
        if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result += englishToBraille["number"];
                isNumber = true;
            }
        }
        else {
            isNumber = false;
        }
        result += englishToBraille[char] || "";
    }
    return result;
}
function main() {
    var input = process.argv.slice(2).join(" ");
    if (!input) {
        console.error("Your input is empty ");
        return;
    }
    if (isBraille(input)) {
        // output : Braille to English
        console.log(translateBrailleToEnglish(input));
    }
    else if (isValidEnglish(input)) {
        //Output : English to Braille
        console.log(translateEnglishToBraille(input));
    }
    else {
        console.error("Please provide valid input");
    }
}
// func trigger point, from where fun begins
main();
