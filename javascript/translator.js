var letterMap = {};
var letterMapInversion = new Map();
var numberMap = {};
var numberMapInversion = new Map();
var symbolMap = {};
var symbolMapInversion = new Map();
var capitalFollow = ".....O";
var decimalFollow = ".O...O";
var numberFollow = ".O.OOO";

letterMap["O....."]="A";
letterMap["O.O..."]="B";
letterMap["OO...."]="C";
letterMap["OO.O.."]="D";
letterMap["O..O.."]="E";
letterMap["OOO..."]="F";
letterMap["OOOO.."]="G";
letterMap["O.OO.."]="H";
letterMap[".OO..."]="I";
letterMap[".OOO.."]="J";
letterMap["O...O."]="K";
letterMap["O.O.O."]="L";
letterMap["OO..O."]="M";
letterMap["OO.OO."]="N";
letterMap["O..OO."]="O";
letterMap["OOO.O."]="P";
letterMap["OOOOO."]="Q";
letterMap["O.OOO."]="R";
letterMap[".OO.O."]="S";
letterMap[".OOOO."]="T";
letterMap["O...OO"]="U";
letterMap["O.O.OO"]="V";
letterMap[".OOO.O"]="W";
letterMap["OO..OO"]="X";
letterMap["OO.OOO"]="Y";
letterMap["O..OOO"]="Z";

for (let key in letterMap) {
    if (letterMap.hasOwnProperty(key)) {
        letterMapInversion.set(letterMap[key], key);
    }
}

numberMap["O....."]="1";
numberMap["O.O..."]="2";
numberMap["OO...."]="3";
numberMap["OO.O.."]="4";
numberMap["O..O.."]="5";
numberMap["OOO..."]="6";
numberMap["OOOO.."]="7";
numberMap["O.OO.."]="8";
numberMap[".OO..."]="9";
numberMap[".OOO.."]="O";

for (let key in numberMap) {
    if (numberMap.hasOwnProperty(key)) {
        numberMapInversion.set(numberMap[key], key);
    }
}

symbolMap["..OO.O"]=".";
symbolMap["..O..."]=",";
symbolMap["..O.OO"]="?";
symbolMap["..OOO."]="!";
symbolMap["..OO.."]=":";
symbolMap["..O.O."]=";";
symbolMap["....OO"]="-";
symbolMap[".O..O."]="/";
symbolMap[".OO..O"]="<";
symbolMap["O..OO."]=">";
symbolMap["O.O..O"]="(";
symbolMap[".O.OO."]=")";
symbolMap["......"]=" ";

for (let key in symbolMap) {
    if (symbolMap.hasOwnProperty(key)) {
        symbolMapInversion.set(symbolMap[key], key);
    }
}

function translate(text, mode) {
    let result = "";
    if (mode === "toBraille") {
        let strings = text.split("");
        let lastIsNumber = false;
        for (let i = 0; i < strings.length; i++) {
            let str = strings[i];
            let asciiCode = strings[i].charCodeAt(0);
            //A~Z
            if (asciiCode >= 65 && asciiCode <= 90) {
                result += capitalFollow + letterMapInversion.get(str);
                lastIsNumber = false;
                //a~z
            } else if (asciiCode >= 97 && asciiCode <= 122) {
                str = str.toUpperCase();
                result += letterMapInversion.get(str);
                lastIsNumber = false;
                //O~9
            } else if (asciiCode >= 48 && asciiCode <= 57) {
                if (lastIsNumber === true) {
                    result += numberMapInversion.get(str);
                } else {
                    result += numberFollow + numberMapInversion.get(str);
                }
                lastIsNumber = true;
                //symbol
            } else {
                result += symbolMapInversion.get(str);
                lastIsNumber = false;
            }
        }
    } else {
        let strings = text.match(/.{1,6}/g);
        let nextCapital = false;
        let nextNumber = false;
        for (let i = 0; i < strings.length; i++) {
            let str = strings[i];
            //next symbol is capital letter
            if (str === capitalFollow) {
                nextCapital = true;
                nextNumber = false;
                continue;
                //next symbol is number
            } else if (str === numberFollow) {
                nextNumber = true;
                nextCapital = false;
                continue;
            }

            if (nextNumber === true) {
                result += numberMap[str];
            } else if (nextCapital === true) {
                result += letterMap[str];
                nextCapital = false;
            } else if (str in letterMap){
                result += letterMap[str].toLowerCase();
            } else if (str in symbolMap) {
                result += symbolMap[str];
                nextCapital = false;
                nextNumber = false;
            }
        }
    }

    return result;
}