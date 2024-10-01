var input = "Hello world";

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

function engToBraille(word){
    var translation = "";
    for (let i = 0; i < word.length; i++) {
        currChar = word.charAt(i);
        console.log(currChar);
        console.log(isNumeric(currChar))
        if(currChar == currChar.toUpperCase() && isLetter(currChar)){
            translation = translation.concat(glossary["capFollows"]);
        }
        if(isNumeric(currChar) && (word.charAt(i - 1) === " " || word.charAt(i - 1) === "" )){
            translation = translation.concat(glossary["numFollows"]);
        }
        if(currChar === "." && isNumeric(word.charAt(i + 1)) || isNumeric(word.charAt(i - 1))){
            translation = translation.concat(glossary["decFollows"]);
        }
        translation = translation.concat(glossary[currChar]);
    }
    return translation;
}
console.log(engToBraille(input))

function brailleToEng(){

}