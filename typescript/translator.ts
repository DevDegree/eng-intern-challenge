
enum Type {
    ENGLISH = "english",
    BRAILLE = "braille"
}

const NUMBER_FOLLOWS = "number_follows";
const CAPITAL_FOLLOWS = "capital_follows";
const SPACE = " ";

const ENGLISH_TO_BRAILLE: Record<string, string> = {
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
    [SPACE]: "......",
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
    [CAPITAL_FOLLOWS]: ".....O",
    [NUMBER_FOLLOWS]: ".O.OOO"
}

const BRAILLE_TO_ENGLISH: Record<string, string> = {
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
    "......": SPACE,
    ".O.OOO": NUMBER_FOLLOWS,
    ".....O": CAPITAL_FOLLOWS,
}

const BRAILLE_TO_NUMBER: Record<string, string> ={
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
}

const getType = (input: string): Type => {
    return input.includes('.') ? Type.BRAILLE : Type.ENGLISH
}

const englishToBraille = (english: string): string => {
    const characters = english.split('');

    let braille = "";

    let isNumberMode = false;

    characters.forEach((c) => {
        if (c != c.toLowerCase()) {
            braille += ENGLISH_TO_BRAILLE[CAPITAL_FOLLOWS]
        }

        if (!Number.isNaN(parseInt(c))) {
            if (!isNumberMode) {
                braille += ENGLISH_TO_BRAILLE[NUMBER_FOLLOWS]
                isNumberMode = true;
            }
            braille += ENGLISH_TO_BRAILLE[c];
        } else if (c === SPACE) {
            isNumberMode = false;
            braille += ENGLISH_TO_BRAILLE[c];
        } else {
            braille += ENGLISH_TO_BRAILLE[c.toLowerCase()]
        }
    })

    return braille;
}

const brailleToEnglish = (braille: string) => {
    let isNumberMode = false;
    let capitalMode = false;

    let english = "";

    for (let i = 0; i < braille.length; i += 6) {
        const character = braille.slice(i, i + 6)

        if (BRAILLE_TO_ENGLISH[character] == NUMBER_FOLLOWS) {
            isNumberMode = true;
        } else if (BRAILLE_TO_ENGLISH[character] == CAPITAL_FOLLOWS) {
            capitalMode = true;
        } else if (BRAILLE_TO_ENGLISH[character] === SPACE) {
            isNumberMode = false;
            english += SPACE;
        } else if (isNumberMode) {
            english += BRAILLE_TO_NUMBER[character];
        } else if (capitalMode) {
            english += BRAILLE_TO_ENGLISH[character].toUpperCase();
            capitalMode = false;
        } else {
            english += BRAILLE_TO_ENGLISH[character];
        }
    }

    return english;
}

const translate = (input: string): string => {
    const type = getType(input);

    switch (type) {
        case Type.ENGLISH:
            return englishToBraille(input.toString());
        case Type.BRAILLE:
            return brailleToEnglish(input.toString());
    }
}

const input = process.argv.slice(2).join(' ')
console.log(translate(input))