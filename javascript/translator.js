
const readline = require('node:readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.question(``, str => {
    console.log(isBrailleOrEnglish(str));
  rl.close();
});

//var input = ".....O.OOO.O.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";

const glossary = {
    "A": "O.....", // A
    "B": "O.O...", // B
    "C": "OO....", // C
    "D": "OO.O..", // D
    "E": "O..O..", // E
    "F": "OOO...", // F
    "G": "OOOO..", // G
    "H": "O.OO..", // H
    "I": ".OO...", // I
    "J": ".OOO..", // J
    "K": "O...O.", // K
    "L": "O.O.O.", // L
    "M": "OO..O.", // M
    "N": "OO.OO.", // N
    "O": "O..OO.", // O
    "P": "OOO.O.", // P
    "Q": "OOOOO.", // Q
    "R": "O.OOO.", // R
    "S": ".OO.O.", // S
    "T": ".OOOO.", // T
    "U": "O...OO", // U
    "V": "O.O.OO", // V
    "W": ".OOO.O", // W
    "X": "OO..OO", // X
    "Y": "OO.OOO", // Y
    "Z": "O..OOO", // Z
    "a": "O.....", // a
    "b": "O.O...", // b
    "c": "OO....", // c
    "d": "OO.O..", // d
    "e": "O..O..", // e
    "f": "OOO...", // f
    "g": "OOOO..", // g
    "h": "O.OO..", // h
    "i": ".OO...", // i
    "j": ".OOO..", // j
    "k": "O...O.", // k
    "l": "O.O.O.", // l
    "m": "OO..O.", // m
    "n": "OO.OO.", // n
    "o": "O..OO.", // o
    "p": "OOO.O.", // p
    "q": "OOOOO.", // q
    "r": "O.OOO.", // r
    "s": ".OO.O.", // s
    "t": ".OOOO.", // t
    "u": "O...OO", // u
    "v": "O.O.OO", // v
    "w": ".OOO.O", // w
    "x": "OO..OO", // x
    "y": "OO.OOO", // y
    "z": "O..OOO", // z
    "1": "O.....", // 1
    "2": "O.O...", // 2
    "3": "OO....", // 3
    "4": "OO.O..", // 4
    "5": "O..O..", // 5
    "6": "OOO...", // 6
    "7": "OOOO..", // 7
    "8": "O.OO..", // 8
    "9": ".OO...", // 9
    "0": ".OOO..", // 0 
    "capFollows": ".....O",
    "decFollows": ".O...O",
    "numFollows": ".O.OOO",
    ".": "..OO.O", // .
    ",": "..O...", // ,
    "?": "..O.OO", // ?
    "!": "..OOO.", // !
    ":": "..OO..", // :
    ";": "..O.O.", // ;
    "-": "....OO", // -
    "/": ".O..O.", // /
    "<": ".OO..O", // <
    ">": "O..OO.", // >
    "(": "O.O..O", // (
    ")": ".O.OO.", // )
    " ": "......", // space
}

function isNumeric(str){
    return /^\d+$/.test(str);
}

function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
}

function findUppercase(str){
    return str.replace(/[^A-Z]+/g, '');
}

function findLowercase(str){
    return str.replace(/[^a-z]+/g, '');
}

function findSymbol(str){
    return str.replace(/[^.,?!:;\-\/<>()\s]/g, '');
}

function findNumber(str){
    return str.replace(/[^0-9]+/g, '');
}

function isBrailleOrEnglish(str){
    if (/^[.O]+$/.test(str)){
        return brailleToEng(str)
    }
    else {
        return engToBraille(str)

    }
}

function getKeyByValue(object, value) {
    return Object.keys(object).filter(key => object[key] === value);
  }

function engToBraille(word){
    var translation = "";
    for (let i = 0; i < word.length; i++) {
        currChar = word.charAt(i);
        if(currChar == currChar.toUpperCase() && isLetter(currChar)){
            translation = translation.concat(glossary["capFollows"]);
        }
        if(isNumeric(currChar) && (word.charAt(i - 1) === " " || word.charAt(i - 1) === "" )){
            translation = translation.concat(glossary["numFollows"]);
        }
        if(currChar === "." && isNumeric(word.charAt(i + 1))){
            translation = translation.concat(glossary["decFollows"]);
        }
        translation = translation.concat(glossary[currChar]);
    }
    return translation;
}

function brailleToEng(word){
    var translation  = "";

    for (let i = 0; i < word.length; i = i + 6) {
        prevBrailleString = word.substring(i, i - 6)
        currBrailleString = word.substring(i, i + 6)
        nextBrailleString = word.substring(i + 6, i + 12)
        nextNextBrailleString = word.substring(i + 12, i + 18)

        var numflag;

        //console.log(currBrailleString);
        //console.log(getKeyByValue(glossary, currBrailleString));

        if(prevBrailleString === glossary["capFollows"]){
            //console.log("prev: "+ prevBrailleString);
            //console.log("next: "+ nextBrailleString);

            translation = translation.concat(findUppercase(getKeyByValue(glossary, currBrailleString).join('')));
        }
        else if (currBrailleString !== glossary["capFollows"] &&
                    currBrailleString !== glossary["numFollows"] &&
                    currBrailleString !== glossary["decFollows"] &&
                    currBrailleString !== glossary[" "] &&
                    !numflag){
            //console.log("prev: "+ prevBrailleString);
            //console.log("next: "+ nextBrailleString);

            translation = translation.concat(findLowercase(getKeyByValue(glossary, currBrailleString).join('')));
        }

        else if(currBrailleString === glossary[" "]){
            translation = translation.concat(getKeyByValue(glossary, currBrailleString).join(''));
        }

        if(currBrailleString === glossary["numFollows"]){
                numflag = true;
        }
        if(numflag){
            //console.log((getKeyByValue(glossary, nextNextBrailleString).join('')))
            translation = translation.concat(findNumber(getKeyByValue(glossary, nextBrailleString).join('')));
        }

        if(nextBrailleString === glossary[" "] || nextBrailleString === "" ){
            numflag = false;
        }
 
        if(currBrailleString === glossary["decFollows"] && numflag){
            translation = translation.concat(getKeyByValue(glossary, nextBrailleString));
        }
        

    }
    return translation;
}

//console.log(brailleToEng(input))