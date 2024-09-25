const CHAR_TO_BRAILLE = {
  // Lowercase letters
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
  // Punctuation and special characters
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  // Special Braille indicators
  "capital": ".....O",  // Capital letter indicator
  "number": ".O.OOO",  // Number indicator
  "decimal": "..O.OO",  // Decimal point indicator (same as '?')
  " ": "......",  // Space
  "*": "O..O.O",  // Reserved char
};

const NUM_TO_BRAILLE = {
  // Numbers (same as a-j)
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

const State = {
    DEFAULT: "default",
    CAP: "capital",
    NUMBER: "number",
    DECIMAL: "decimal"
};

const MISSING = "*";
const SPACE = " ";

const braille2char = Object.fromEntries(
    Object.entries(CHAR_TO_BRAILLE).map(([k, v]) => [v, k])
);
const braille2num = Object.fromEntries(
    Object.entries(NUM_TO_BRAILLE).map(([k, v]) => [v, k])
);

class MalformedInput extends Error {
    constructor(message) {
        super(message);
        this.name = "MalformedInput";
    }
}

function parseBraille(tokens) {
    function lookAroundNum(i) {
        const lhsStep = -1, lhsEnd = 0;
        const rhsStep = 1, rhsEnd = tokens.length - 1;

        for (const [step, end] of [[lhsStep, lhsEnd], [rhsStep, rhsEnd]]) {
            let k = 0;
            while (i + k !== end) {
                k += step;
                if (braille2char[tokens[i + k]] === SPACE) continue;
                if (tokens[i + k] in braille2num) return true;
                else return false;
            }
        }
        return false;
    }

    let state = State.DEFAULT;
    let output = "";

    for (let i = 0; i < tokens.length; i++) {
        let char;
        if ((state === State.NUMBER || state === State.DECIMAL) && tokens[i] in braille2num) {
            char = braille2num[tokens[i]];
        } else {
            if (braille2char[tokens[i]] === "decimal") {
                char = i > 0 && braille2char[tokens[i - 1]] === "." ? "decimal" : "?";
            } else if (braille2char[tokens[i]] === ">") {
                char = lookAroundNum(i) ? ">" : "o";
            } else {
                char = braille2char[tokens[i]] || MISSING;
                if (state === State.CAP) {
                    char = char.toUpperCase();
                    state = State.DEFAULT;
                }
            }
        }

        if (char === State.CAP || char === State.NUMBER || char === State.DECIMAL) {
            state = char;
            continue;
        } else if (char === SPACE && (state === State.NUMBER || state === State.DECIMAL)) {
            state = State.DEFAULT;
        }

        output += char;
    }

    return output;
}

function parseString(tokens) {
    const tok2braille = { ...CHAR_TO_BRAILLE, ...NUM_TO_BRAILLE };
    let state = State.DEFAULT;
    let output = "";

    for (let i = 0; i < tokens.length; i++) {
        let bchar;
        if (/\d/.test(tokens[i])) {
            if (state !== State.NUMBER) {
                bchar = tok2braille[State.NUMBER] + tok2braille[tokens[i]];
                state = State.NUMBER;
            } else {
                bchar = tok2braille[tokens[i]];
            } 
        } else if (/^[A-Z]$/.test(tokens[i])) {
            bchar = tok2braille[State.CAP] + tok2braille[tokens[i].toLowerCase()];
        } else if (tokens[i] === SPACE && state === State.NUMBER) {
            state = State.DEFAULT;
            bchar = tok2braille[tokens[i]] || tok2braille[MISSING];
        } else {
            bchar = tok2braille[tokens[i]] || tok2braille[MISSING];
        }

        output += bchar;
    }

    return output;
}

function checkBraille(chrs) {
    return chrs.split('').every(c => c === '.' || c === 'O');
}

function parseArg(brIn, isBraille) {
    const tokens = [];

    for (let i = 0; i < brIn.length - 1; i += 6) {
        tokens.push(brIn.slice(i, i + 6));
    }
    if (tokens.length == 0) {
      tokens.push(brIn);
    }

    return isBraille ? parseBraille(tokens) : parseString(tokens.join(''));
}

function main(args) {
    const inputText = args.join(' ');
    if (!inputText) {
        console.log("No input supplied, exiting");
        process.exit(0);
    }

    const isBraille = checkBraille(inputText);
    const SEPARATOR = isBraille ? SPACE : CHAR_TO_BRAILLE[SPACE];
    const result = args.map(arg => parseArg(arg, isBraille)).join(SEPARATOR);

    // for debugging
    // if (!isBraille) {
    //   let output = "";
    //   result.split("").forEach((c, index) => {
    //     if (index % 6 == 0 && index != 0)
    //       output += "\n"
    //     output += c;  
    //   })
    //   console.log(output);
    // }

    console.log(result);
}

// If running as a script
if (require.main === module) {
    const args = process.argv.slice(2);
    main(args);
}