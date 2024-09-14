const args = process.argv.slice(2);
const argText = args.join(' ')
const regex = /^[O.]+$/;
const isBraille = (argText.length % 6 == 0 ) && regex.test(argText)

const brailleToEnglish = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z"
};

const brailleToNumber = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}
const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

function isUpperCase(char) {
    return 'A' <= char && char <= 'Z';
}
if (!isBraille) {
    var res = "";

    for(let i = 0; i < args.length; i++) {
        const word = args[i];
        if (i > 0){
            res += "......";
        }
        if ('0' <= word[0] && word[0] <= '9'){
            res += ".O.OOO"
        }
        for(const char of word) {
            if (isUpperCase(char)) {
                res += ".....O";
            }
            res += englishToBraille[char.toLowerCase()];
        }
    }

    console.log(res)
}
else {
    var capital = false;
    var number = false;

    var res = "";


    for(let i = 0; i < argText.length - 5; i += 6){
        const word = argText.substring(i, i+6);

        if (word == ".....O"){ //next is capital
            capital = true;
            continue;
        } else if (word == ".O.OOO") { // next is number
            number = true;
        } else if (word == "......") { //space
            res += " ";
            number = false;
        } else if (number) { // number
            res += brailleToNumber[word];
        } else if (capital){ // captial
            res += brailleToEnglish[word].toUpperCase();
        } else {
            res += brailleToEnglish[word];
        }
        capital = false;
    }

    console.log(res)
}