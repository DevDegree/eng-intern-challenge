//Mapping

//braille to english mapping
const brailleToEnglishMapping = {
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
    ".....0": "capital",
    ".0...0": "decimal",
    ".0.000": "number",
    "..00.0": ".",
    "..0...": ",",
    "..0.00": "?",
    "..000.": "!",
    "..00..": ":",
    "..0.0.": ";",
    "....00": "-",
    ".0..0.": "/",
    ".00..0": "<",
    "0..00.": ">",
    "0.0..0": "(",
    ".0.00.": ")",
    "......": " "
};
//braille to english mapping for numbers
const numberBrailleToEnglish = {
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

//english to braille mapping
const englishToBrailleMapping = {
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
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
};

const resultList = [];

//function to translate Braille to English
const brailleToEnglish = (args) => {
    let isNumMode = false;
    let isUpperMode = false;

    for (let i = 0; i < args.length; i += 6) {
        const chunk = args.slice(i, i + 6);
        if(chunk === ".O.OOO") {
            isNumMode = true;
            continue;
        }
        if(chunk === ".....O") {
            isUpperMode = true;
        }
        if (chunk === "......") {
            isNumMode = false;
        }
        if(isNumMode === false) {
            if(chunk in brailleToEnglishMapping) {
                if(isUpperMode === true) {
                    resultList.push(brailleToEnglishMapping[chunk].toUpperCase());
                    isUpperMode = false;
                }
                else {
                    resultList.push(brailleToEnglishMapping[chunk]);
                }
            }
        }
        else {
            if(chunk in numberBrailleToEnglish) {
                resultList.push(numberBrailleToEnglish[chunk]);
            }
        }
        
    }
    const englishResult = resultList.join('');
    return englishResult;
};

//function to translate English to Braille
const englishToBraille = (args) => {
    let isNum = false;
    //loop through all elements in args string array
    for (const char of args) {
        let charSearch = char.toLowerCase();
        if(charSearch in englishToBrailleMapping) {
            if(char === char.toUpperCase() && /^[a-zA-Z]$/.test(char) && isNaN(char)) {
                resultList.push(englishToBrailleMapping["capital"]);
            }
            if(!isNaN(char) && char !== ' ' && isNum !== true) {
                isNum = true;
                resultList.push(englishToBrailleMapping["number"]);
            }
            if(char === "." && char !== ' ') {
                resultList.push(englishToBrailleMapping["decimal"]);
            }
            resultList.push(englishToBrailleMapping[charSearch]);
        }
    }
    const resultString = resultList.join('');
    return resultString;
};

//take arguments from input
const args = process.argv.slice(2).join(' ');

//detect if string input is English or Braille
const isBraille = (str) => /^[.O]+$/.test(str);
const response = isBraille(args);

//output correct translation to console
if(response == true) {
    const resultEnglish = brailleToEnglish(args);
    console.log(resultEnglish);
}
else {
    const resultBraille = englishToBraille(args);
    console.log(resultBraille);
}
