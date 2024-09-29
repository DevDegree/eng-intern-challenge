const brailleToEnglishMap = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z",
    ".....O": "capital follows", 
    ".O.OOO": "number follows",  
    "......": " "               
};

const englishToBrailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......"
};


const translateToEnglish = (brailleString) => {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < brailleString.length; i += 6) {
        const word = brailleString.slice(i, i + 6);
        if (brailleToEnglishMap[word] === "capital follows") {
            isCapital = true;
            isNumber = false; 
        } else if (brailleToEnglishMap[word] === "number follows") {
            isNumber = true;  
        } else if (word === "......") {
            result += " ";
            isNumber = false;  
        } else {
            let char = brailleToEnglishMap[word];
            if (char === undefined) continue;  
            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }
            if (isNumber) {
                // Convert letters a-j to corresponding numbers 1-9, 0
                if (char >= 'a' && char <= 'j') {
                    char = String.fromCharCode(char.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
                }
            }

            result += char;
        }
    }

    return result;
};



const translateToBraille = (englishString) => {
    let result = [];
    let isNumber = false;

    for (let char of englishString) {
        // Handle uppercase letters 
        if (/[A-Z]/.test(char)) {
            result.push(".....O"); 
            char = char.toLowerCase(); 
        }
        // Handle numbers 
        else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result.push(".O.OOO"); 
                isNumber = true;
            }
            result.push(englishToBrailleMap[char]); // Direct mapping for numbers
            continue;
        } else {
            isNumber = false;
        }
        // Handle spaces 
        if (char === " ") {
            result.push("......"); 
        } else {
            result.push(englishToBrailleMap[char]);
        }
    }

    return result.join("");
};

const detectAndTranslate = (inputString) => {
    if (inputString.includes("O") || inputString.includes(".")) {
        return translateToEnglish(inputString);
    } else {
        return translateToBraille(inputString);
    }
};

const inputString = process.argv.slice(2).join(" ");
console.log(detectAndTranslate(inputString));