const brailleToEnglish = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " "
};

const brailleToNumber = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
};

const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
};

const numberToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

function translate(inputString) {

    if (/^[O.]+$/.test(inputString)) {
        let result = '';
        let nextIsCapital = false;
        let nextIsNumber = false;
        const brailleChars = inputString.match(/.{1,6}/g);

        for (let b of brailleChars) {
            if (b in brailleToEnglish) {
                let char = brailleToEnglish[b];

                if (nextIsCapital) {
                    char = char.toUpperCase();
                    nextIsCapital = false;
                }
                if (nextIsNumber) {
                    char = brailleToNumber[b] || '?';
                }

                result += char;
                if (char === ' ') {
                    nextIsNumber = false
                }
            } else if (b === '.....O') {
                nextIsCapital = true;
            } else if (b === '.O.OOO') {
                nextIsNumber = true;
            }

        }
        return result;
    } else {
        let result = '';
        let lstChar= '';
        for (let char of inputString) {
            if (char >= 'A' && char <= 'Z') {
                result += '.....O' + englishToBraille[char.toLowerCase()];
            } else if (char >= '0' && char <= '9') {
                if(lstChar >= '0' && lstChar <= '9'){
                    result += numberToBraille[char];
                }else{
                    result += '.O.OOO' + numberToBraille[char];
                }
                
            } else {
                result += englishToBraille[char] || '......';
            }
            lstChar=char;
        }
        return result;
    }
}

if (require.main === module) {
    const inputString = process.argv.slice(2).join(' ');
    console.log(translate(inputString));
}

module.exports = translate;
