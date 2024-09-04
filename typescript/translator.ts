const letterToBraille: Record<string, string> = {
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
};

const numberToBraille: Record<string, string> = {
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

const spaceBraille = "......";
const capitalFollowsBraille = ".....O";
const numberFollowsBraille = ".O.OOO";

const brailleToLetter = Object.fromEntries(
    Object.entries(letterToBraille).map(([letter, braille]) => [
        braille,
        letter,
    ]),
);

const brailleToNumber = Object.fromEntries(
    Object.entries(numberToBraille).map(([number, braille]) => [
        braille,
        number,
    ]),
);

const BRAILLE_SYMBOL_LENGTH = 6;

function isLetterUpperCase(letter: string): boolean {
    return letter.toUpperCase() === letter;
}

function isBrailleString(str: string): boolean {
    // In the constraints of the challenge, a simpler check could be just to look
    // at the first six characters and see if there is a dot in it.

    let seenDot = false;

    for (const char of str) {
        if (char !== "." && char !== "O") {
            return false;
        }

        if (!seenDot && char === ".") {
            seenDot = true;
        }
    }

    return seenDot;
}

function translateEnglishToBraille(english: string): string {
    let braille = "";
    let isReadingNumber = false;

    for (const char of english) {
        if (char === " ") {
            isReadingNumber = false;
            braille += spaceBraille;
            continue;
        }

        const letterBraille = letterToBraille[char.toLowerCase()];

        if (letterBraille) {
            isReadingNumber = false;

            if (isLetterUpperCase(char)) {
                braille += capitalFollowsBraille;
            }

            braille += letterBraille;
            continue;
        }

        const numberBraille = numberToBraille[char];

        if (numberBraille) {
            if (!isReadingNumber) {
                braille += numberFollowsBraille;
                isReadingNumber = true;
            }

            braille += numberBraille;
        }
    }

    return braille;
}

function translateBrailleToEnglish(braille: string): string {
    let english = "";
    let isReadingNumber = false;
    let isReadingCapitalized = false;

    for (let i = 0; i < braille.length; i += BRAILLE_SYMBOL_LENGTH) {
        const brailleSymbol = braille.substring(i, i + BRAILLE_SYMBOL_LENGTH);

        if (brailleSymbol === capitalFollowsBraille) {
            isReadingCapitalized = true;
            continue;
        }

        if (brailleSymbol === numberFollowsBraille) {
            isReadingNumber = true;
            continue;
        }

        if (brailleSymbol === spaceBraille) {
            isReadingNumber = false;
            english += " ";
            continue;
        }

        if (isReadingNumber) {
            english += brailleToNumber[brailleSymbol];
        } else {
            const letter = brailleToLetter[brailleSymbol];
            english += isReadingCapitalized ? letter.toUpperCase() : letter;
        }

        isReadingCapitalized = false;
    }

    return english;
}

const input = process.argv.slice(2).join(" ");

if (isBrailleString(input)) {
    console.log(translateBrailleToEnglish(input));
} else {
    console.log(translateEnglishToBraille(input));
}
