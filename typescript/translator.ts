// defining braille alphabet and numbers
const brailleAlphabet: { [key: string]: string } = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", 
    "capital": ".....O", "number": ".O.OOO"
};

const brailleNumbers: { [key: string]: string } = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Reverse the mapping for decoding
const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([k, v]) => [v, k])
);
const reverseBrailleNumbers = Object.fromEntries(
    Object.entries(brailleNumbers).map(([k, v]) => [v, k])
);

// function to determine if the input is Braille or English
function isBraille(input: string): boolean {
    return /^[O.]+$/.test(input);
}

// function to determine input type and translate
function main() {
    const input = process.argv.slice(2).join(" ");
    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

// function to translate English to Braille
function translateToBraille(input: string): string {
    let result = "";
    let isNumberMode = false;

    for (const char of input) {
        if (char >= "A" && char <= "Z") {
            result += brailleAlphabet["capital"];
            result += brailleAlphabet[char.toLowerCase()];
            isNumberMode = false; // Exit number mode on letter
        } else if (char >= "0" && char <= "9") {
            if (!isNumberMode) {
                result += brailleAlphabet["number"];
                isNumberMode = true;
            }
            result += brailleNumbers[char];
        } else if (char === " ") {
            result += brailleAlphabet[char];
            isNumberMode = false; // Reset number mode on space
        } else {
            result += brailleAlphabet[char];
        }
    }
    return result;
}

// function to translate Braille to English
function translateToEnglish(input: string): string {
    let result = "";
    let i = 0;
    let isCapital = false;
    let isNumberMode = false;

    while (i < input.length) {
        const brailleChar = input.slice(i, i + 6);
        if (brailleChar === brailleAlphabet["capital"]) {
            isCapital = true;
            i += 6;
            continue;
        } else if (brailleChar === brailleAlphabet["number"]) {
            isNumberMode = true;
            i += 6;
            continue;
        }

        if (isNumberMode) {
            result += reverseBrailleNumbers[brailleChar];
        } else {
            let letter = reverseBrailleAlphabet[brailleChar];
            if (isCapital) {
                letter = letter.toUpperCase();
                isCapital = false;
            }
            result += letter;
        }
        i += 6;
    }
    return result;
}

// calling the main function
main();
