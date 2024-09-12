const braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..", " ": "......", "CAPITAL": ".....O", "NUMBER": ".O.OOO"
};

const english = Object.fromEntries(Object.entries(braille).map(([key, value]) => [value, key]));


function englishToBraille(englishText) {

    let convertedText = '';
    let isNumber = false;

    for (let char of englishText) {
        if (char === ' ') {
            convertedText += braille[' '];
        } else if (char >= 'A' && char <= 'Z') {
            convertedText += braille['CAPITAL'];
            char = char.toLowerCase();
            convertedText += braille[char] || '......';

        } else if (char >= '0' && char <= '9') {
            if (!isNumber) {
                convertedText += braille['NUMBER'];
                isNumber = true;
            }
            convertedText += braille[char];
        } else {
            if (isNumber) {
                isNumber = false;
            }
            convertedText += braille[char] || '......';
        }
    }

    return convertedText;
}

function brailleToEnglish(brailleText) {
    let convertedText = "";
    let isCaptial = false;
    let isNumber = false;

    for (let i = 0; i < brailleText.length; i += 6) {
        let brailleChar = brailleText.slice(i, i + 6);


        if (brailleChar === braille["NUMBER"]) {
            isNumber = true;
            continue;
        }
        if (brailleChar === braille["CAPITAL"]) {
            isCaptial = true;
            continue;
        }

        let englishChar = english[brailleChar] || '';

        if (isNumber) {
            if (brailleChar === braille["1"]) englishChar = "1";
            else if (brailleChar === braille["2"]) englishChar = "2";
            else if (brailleChar === braille["3"]) englishChar = "3";
            else if (brailleChar === braille["4"]) englishChar = "4";
            else if (brailleChar === braille["5"]) englishChar = "5";
            else if (brailleChar === braille["6"]) englishChar = "6";
            else if (brailleChar === braille["7"]) englishChar = "7";
            else if (brailleChar === braille["8"]) englishChar = "8";
            else if (brailleChar === braille["9"]) englishChar = "9";
            else if (brailleChar === braille["0"]) englishChar = "0";
            else isNumber = false;
        }

        if (isCaptial) {
            englishChar = englishChar.toUpperCase();
            isCaptial = false;
        }

        convertedText += englishChar;

    }

    return convertedText;

}

function ifBraille(text) {
    return text.length % 6 === 0 && /^[O.]+$/.test(text);
}

function translator() {
    const input = process.argv[2];

    if (ifBraille(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }

}

translator()


