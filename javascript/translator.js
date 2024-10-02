const brailleAlphabet = {
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
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    " ": "......",
    "capitalFollows": ".....O",
    "numberFollows": ".O.OOO",
    "decimalFollows": ".0.000",
};

const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

function translateToBraille(input) {
    let result = "";
    let isNumber = false;

    for (let i = 0; i < input.length; i++) {
        let char = input[i].toLowerCase();
        if (char >= "0" && char <= "9") {
            if (!isNumber) {
                result += brailleAlphabet["numberFollows"];
                isNumber = true;
            }
            result += brailleAlphabet[char];
        } else {
            if (isNumber) {
                isNumber = false;
            }
            if (char >= "a" && char <= "z" && input[i] === input[i].toUpperCase()) {
                result += brailleAlphabet["capitalFollows"];
            }
            result += brailleAlphabet[char] || "";
        }
    }
    return result;
}

function translateFromBraille(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const char = input.slice(i, i + 6);
        if (char === brailleAlphabet['capitalFollows']) {
            isCapital = true;
        } else if (char === brailleAlphabet['numberFollows']) {
            isNumber = true;
        } else {
            let translated = reverseBrailleAlphabet[char];
            if (translated) {
                if (isNumber && 'abcdefghij'.includes(translated)) {
                    // Convert letters a-j to numbers 1-0
                    const num = 'abcdefghij'.indexOf(translated);
                    translated = num === 9 ? '0' : (num + 1).toString();
                } else {
                    // If we encounter a non-number character, turn off number mode
                    isNumber = false;
                    if (isCapital) {
                        translated = translated.toUpperCase();
                        isCapital = false;
                    }
                }
                result += translated;
            }
        }
    }
    return result;
}

function isBraille(input) {
  const validChars = new Set(["O", "."]);
  return input.split("").every((char) => validChars.has(char));
}


function translate(input) {
  if (isBraille(input)) {
    return translateFromBraille(input);
  } else {
    return translateToBraille(input);
  }
}

const args = process.argv.slice(2);
const input = args.join(" ");
console.log(translate(input));
