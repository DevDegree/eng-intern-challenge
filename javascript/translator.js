const engToBraille = {
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
    " ": "......"  // space
};

const brailleToEng = Object.fromEntries(Object.entries(engToBraille).map(([eng, braille]) => [braille, eng]));

const numToBraille = {
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

const brailleToNum = Object.fromEntries(Object.entries(numToBraille).map(([num, braille]) => [braille, num]));

const additionals = {
    "capital_follows": ".....O",
    "number_follows": ".O.OOO"
};

function translateToBraille(text) {
    let result = [];
    let numberMode = false;

    for (let char of text) {
        if (/\d/.test(char)) {  // If it's a number
            if (!numberMode) {
                numberMode = true;
                result.push(additionals.number_follows);
            }
            result.push(numToBraille[char]);
        } else if (char === ' ') {  // In case of a space
            numberMode = false;
            result.push(engToBraille[char]);
        } else if (char.toUpperCase() === char && char.toLowerCase() in engToBraille) {  // In case of a capital letter
            result.push(additionals.capital_follows);
            result.push(engToBraille[char.toLowerCase()]);
        } else {
            result.push(engToBraille[char.toLowerCase()]);
        }
    }

    return result.join('');
}

function translateToEnglish(text) {
    let result = [];
    let i = 0;
    const length = text.length;
    let numberMode = false;

    while (i < length) {
        let chunk = text.slice(i, i + 6);
        if (chunk === additionals.capital_follows) {
            i += 6;
            chunk = text.slice(i, i + 6);
            result.push(brailleToEng[chunk].toUpperCase());
        } else if (chunk === additionals.number_follows) {
            numberMode = true;
        } else if (chunk === '......') {  // space
            numberMode = false;
            result.push(brailleToEng[chunk]);
        } else {
            if (numberMode) {
                result.push(brailleToNum[chunk]);
            } else {
                result.push(brailleToEng[chunk]);
            }
        }

        i += 6;
    }
    return result.join('');
}

function translateLanguage(inputText) {
    return /^[.O]+$/.test(inputText);
}

function main() {
    const inputText = process.argv.slice(2).join(' ');

    if (translateLanguage(inputText)) {
        console.log(translateToEnglish(inputText));
    } else {
        console.log(translateToBraille(inputText));
    }
}

if (require.main === module) {
    main();
}
