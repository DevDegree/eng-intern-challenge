const redirectToFunction = (input) => {
    let isBraille = true;
    for (let i = 0; i < input.length; i++) {
        const char = input[i];
        if (char !== 'O' && char !== '.') {
            isBraille = false;
            break;
        }
    }
    if (isBraille) {
        translateBrailleToEnglish(input);
    } else {
        translateEnglishToBraille(input);
    }
}

const translateEnglishToBraille = (english) => {
    let numberFlag = false;
    let res = "";
    let currentCharacter = "";
    const numberLookUpTable = {
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
    };
    const lookUpTable = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOO...",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
        "capital": ".....O",
        "number": ".O.OOO",
        " ": "......"
    }
    for(let i = 0; i < english.length; i++){
        currentCharacter = english.substring(i,i+1);
        if(!isNaN(currentCharacter) && currentCharacter !== ' '){
            if(!numberFlag){
                res += lookUpTable["number"];
                numberFlag = true;
            }
            res += numberLookUpTable[currentCharacter];
        } else if(currentCharacter === currentCharacter.toUpperCase() && currentCharacter !== currentCharacter.toLowerCase() ){
            res += lookUpTable["capital"];
            res += lookUpTable[currentCharacter.toLowerCase()];
        } else if(currentCharacter === " "){
            numberFlag = false;
            res += lookUpTable[" "];
        } else{
            numberFlag = false;
            res += lookUpTable[currentCharacter];
        }
    }
    console.log(res);
}


const translateBrailleToEnglish = (braille) => {
    let numberFlag = false;
    let decimalFlag = false;
    let capitalFlag = false;
    let res = "";
    let currentCharacter = "";
    const numberLookUpTable = {
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
    }
    const lookUpTable = {
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
        "OOOO.":  "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
        ".....O": "capital",
        ".O.OOO": "number",
        "......": " "
    }
    for (let i = 0; i < braille.length; i += 6) {
        currentCharacter = braille.substring(i, i + 6);

        if (lookUpTable[currentCharacter] === "capital") {
            capitalFlag = true;
        } else if (lookUpTable[currentCharacter] === "decimal") {
            decimalFlag = true;
        } else if (lookUpTable[currentCharacter] === "number") {
            numberFlag = true;
        } else if (lookUpTable[currentCharacter] === " ") {
            res += " ";
            numberFlag = false;
        } else {
            if (capitalFlag) {
                res += lookUpTable[currentCharacter].toUpperCase();
                capitalFlag = false;
            } else if (decimalFlag) {
                res += numberLookUpTable[currentCharacter];
                decimalFlag = false;
            } else if (numberFlag) {
                res += numberLookUpTable[currentCharacter];
            } else {
                res += lookUpTable[currentCharacter];
            }
        }
    }
    console.log(res);
}

const input = process.argv.slice(2).join(' ');
redirectToFunction(input);