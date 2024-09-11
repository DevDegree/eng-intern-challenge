let words = process.argv.slice(2);

type BrailleCategory = Record<string, string>;

interface BrailleCharacters {
    alphabet: BrailleCategory;
    numbers: BrailleCategory;
    punctuation: BrailleCategory;
    follows: BrailleCategory;
}

interface CharactersToBraille {
    alphabet: BrailleCategory;
    numbers: BrailleCategory;
    punctuation: BrailleCategory;
}

const brailleCharacters: BrailleCharacters = {
    alphabet: {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
    },
    numbers: {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
    },
    punctuation: {
        "..OO.O": ".",
        "..O...": ",",
        "..O.OO": "?",
        "..OOO.": "!",
        "..OO..": ":",
        "..O.O.": ";",
        "....OO": "-",
        ".O..O.": "/",
        ".OO..O": "<",
        "O..OO.": ">",
        "O.O..O": "(",
        ".O.OO.": ")",
        "......": " ",
    },
    follows: {
        ".....O": "capital",
        ".O...O": "decimal",
        ".O.OOO": "number",
    },
};

const charactersToBraille: CharactersToBraille = {
    alphabet: {
        a: "O.....",
        b: "O.O...",
        c: "OO....",
        d: "OO.O..",
        e: "O..O..",
        f: "OOO...",
        g: "OOOO..",
        h: "O.OO..",
        i: ".OO...",
        j: ".OOO..",
        k: "O...O.",
        l: "O.O.O.",
        m: "OO..O.",
        n: "OO.OO.",
        o: "O..OO.",
        p: "OOO.O.",
        q: "OOOOO.",
        r: "O.OOO.",
        s: ".OO.O.",
        t: ".OOOO.",
        u: "O...OO",
        v: "O.O.OO",
        w: ".OOO.O",
        x: "OO..OO",
        y: "OO.OOO",
        z: "O..OOO",
    },
    numbers: {
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
    },
    punctuation: {
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
        " ": "......",
    },
};
const checkIsBraille = (str: string) => {
    if (str.length % 6 !== 0) {
        return false;
    }
    if (!/^[O.]+$/.test(str)) {
        return false;
    }
    return true;
};
let output: string[] = [""];
const main = (words: string[]) => {
    let isNum = false;
    let isCapital = false;
    if (checkIsBraille(words[0])) {
        for (let i = 0; i < words[0].length; i += 6) {
            const brailleChar: string = words[0].substring(i, i + 6);
            if (brailleCharacters.follows[brailleChar] === "number") {
                isNum = true;
            } else if (brailleCharacters.follows[brailleChar] === "capital") {
                isCapital = true;
            } else {
                if (brailleCharacters.punctuation[brailleChar]) {
                    output.push(brailleCharacters.punctuation[brailleChar]);
                    if (brailleCharacters.punctuation[brailleChar] === " ") {
                        isNum = false;
                    }
                } else if (isNum) {
                    if (brailleCharacters.numbers[brailleChar]) {
                        output.push(brailleCharacters.numbers[brailleChar]);
                    }
                } else if (brailleCharacters.alphabet[brailleChar]) {
                    let alphabet = brailleCharacters.alphabet[brailleChar];
                    if (isCapital) {
                        alphabet = alphabet.toUpperCase();
                        isCapital = false;
                    }
                    output.push(alphabet);
                } else {
                    throw new Error("Unexpected Braille: " + brailleChar);
                }
            }
        }
    } else {
        words.map((word, index) => {
            for (let c = 0; c < word.length; c++) {
                const char: string = word[c];
                if (charactersToBraille.punctuation[char]) {
                    output.push(char);
                } else if (charactersToBraille.numbers[char]) {
                    if (!charactersToBraille.numbers[word[c - 1]]) {
                        output.push(".O.OOO");
                    }
                    output.push(charactersToBraille.numbers[char]);
                } else if (charactersToBraille.alphabet[char]) {
                    output.push(charactersToBraille.alphabet[char]);
                } else if (charactersToBraille.alphabet[char.toLowerCase()]) {
                    output.push(".....O");
                    output.push(
                        charactersToBraille.alphabet[char.toLowerCase()]
                    );
                } else {
                    throw new Error("Unexpected character: " + char);
                }
            }
            if (index < words.length - 1) {
                output.push("......");
            }
        });
    }
    console.log(output.join(""));
};
main(words);
