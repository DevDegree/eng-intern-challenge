const charBrailleMap = {
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
    " ": "......",
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
    "number": ".O.OOO"
}

let charEnglishMap = {};
Object.keys(charBrailleMap).forEach(key => {
    charEnglishMap[charBrailleMap[key]] = key
})

function translator(input) {
    if(isBraille(input)) {
        return translateBrailleToEnglish(input)
    }

    return translateEnglishToBraille(input)
}

function isBraille(input) {
    let regex = /^[O.]*$/;
    return regex.test(input)
}

function translateBrailleToEnglish(input) {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        switch (brailleChar) {
            case ".....O": {
                isCapital = true;
                break;
            }
            case ".O.OOO": {
                isNumber = true;
                break
            }
            case "......": {
                result += " ";
                isNumber = false;
                break;
            }
            default: {
                if (isNumber) {
                    result += charEnglishMap[brailleChar];
                } else if (isCapital) {
                    result += charEnglishMap[brailleChar].toUpperCase();
                    isCapital = false;
                } else {
                    result += charEnglishMap[brailleChar];
                }
            }
        }
    }

    return result;
}

function translateEnglishToBraille(input) {
    let result = "";
    let isNumber = false

    for (let char of input) {
         switch (true) {
             case /[A-Z]/.test(char):
                 result += charBrailleMap["capital"] + charBrailleMap[char.toLowerCase()]
                 break
             case /[0-9]/.test(char):
                 if(!isNumber) {
                     result += charBrailleMap["number"]
                     isNumber = true
                 }
                 result += charBrailleMap[char]
                 break
             case char === " ":
                 result += charBrailleMap[" "]
                 isNumber = false;
                 break
             default:
                 result += charBrailleMap[char]
                 break
         }
    }
    return result;
}

const argvs = process.argv.slice(2).join(" ");
if (!argvs) {
    console.log("Please enter the text you wish to translate.");
}

console.log(translator(argvs))
