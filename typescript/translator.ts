const brailleMap: { [key: string]: string } = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", 
    "A": ".....O.....O.....", "B": ".....O.O...O.....", "C": ".....OO....O.....", "D": ".....OO.O..O.....", "E": ".....O..O..O.....",
    "F": ".....OOO...O.....", "G": ".....OOOO..O.....", "H": ".....O.OO..O.....", "I": ".....OO...O.....", "J": ".....OOO..O.....",
    "K": ".....O...O...O...", "L": ".....O.O.O...O...", "M": ".....OO..O...O...", "N": ".....OO.OO...O...", "O": ".....O..OO...O...",
    "P": ".....OOO.O...O...", "Q": ".....OOOOO...O...", "R": ".....O.OOO...O...", "S": ".....OO.O...O...", "T": ".....OOOO...O...",
    "U": ".....O...OO...O...", "V": ".....O.O.OO...O...", "W": ".....OOO.OO...O...", "X": ".....OO..OO...O...", "Y": ".....OO.OOO...O...",
    "Z": ".....O..OOO...O...",
    "0": ".O.OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
};

const brailleReverseMap: { [key: string]: string } = {};
for (let key in brailleMap) {
    brailleReverseMap[brailleMap[key]] = key;
}

function isBraille(input: string): boolean {
    return /^[O.]+$/.test(input);
}

function translateToBraille(input: string): string {
    return input.split('').map(char => brailleMap[char] || '').join('');
}

function translateToEnglish(input: string): string {
    let result = '';
    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.substr(i, 6);
        result += brailleReverseMap[brailleChar] || '';
    }
    return result;
}

function translate(input: string): string {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
if (!input) {
    console.error('Please provide a string to translate.');
    process.exit(1);
}

console.log(translate(input));