import assert from "assert";

type Modifier = "lowercase" | "uppercase" | "number";

type DotOrO = "." | "O";
type Glyph = `${DotOrO}${DotOrO}${DotOrO}${DotOrO}${DotOrO}${DotOrO}`;
type Alphabet = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z";
type HasGlyph = Alphabet | " " | "uppercase" | "number";

const character_to_braille = {
    // main alphabet
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..",
    h: "O.OO..", i: ".OO...", j: ".OOO..", k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.",
    o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",
    // special characters
    " ": "......", uppercase: ".....O", number: ".O.OOO",
    // validates that all characters are covered, and correspond to a glyph matching braille
} satisfies Record<HasGlyph, Glyph> as Record<string, Glyph>;

// inverse character_to_braille
const braille_to_character = Object.fromEntries(
    Object.entries(character_to_braille).map(([k, v]) => [v, k])
);

const number_to_character = {
    "1": "a", "2": "b", "3": "c", "4": "d", "5": "e",
    "6": "f", "7": "g", "8": "h", "9": "i", "0": "j",
} as Record<string, Alphabet>;

const character_to_number = Object.fromEntries(
    Object.entries(number_to_character).map(([k, v]) => [v, k])
);

function toBrailleWord(word: string): string {
    let translation = "";
    for (let i = 0; i < word.length; i++) {
        if (word[i].match(/[A-Z]/)) {
            translation += character_to_braille.uppercase;
            translation += character_to_braille[word[i].toLowerCase()];
        } else if (word[i].match(/[0-9]/)) {
            translation += character_to_braille.number;
            // numbers run until the end of the word
            while (i < word.length) {
                assert(word[i] in number_to_character, `${word[i]} is a number`);
                translation += character_to_braille[number_to_character[word[i]]];
                i++;
            }
        } else {
            assert(word[i] in character_to_braille, `${word[i]} is a supported character`);
            translation += character_to_braille[word[i]];
        }
    }
    return translation;
}

function toBraille(words: string): string {
    return words.split(" ").map(toBrailleWord).join("......");
}

function fromBraille(braille: string): string {
    assert(braille.length % 6 === 0, "braille.length % 6 === 0");

    let translation = "";
    let modifier: Modifier = "lowercase";
    for (let i = 0; i < braille.length; i += 6) {
        const glyph = braille.slice(i, i + 6);

        assert(glyph in braille_to_character, `${glyph} is supported braille glyph`);
        const letter = braille_to_character[glyph];

        if (letter === " ") {
            translation += " ";
            modifier = "lowercase";
        } else if (letter === "uppercase") {
            modifier = "uppercase";
        } else if (letter === "number") {
            modifier = "number";
        } else {
            assert(letter.length === 1, "letter.length === 1");

            if (modifier === "uppercase") {
                translation += letter.toUpperCase();
                modifier = "lowercase";
            } else if (modifier === "number") {
                translation += character_to_number[letter];
            } else {
                translation += letter;
            }
        }
    }

    return translation;
}

const words_or_braille = process.argv.slice(2).join(" ");

if (
    // braille doesn't include any spaces
    !words_or_braille.includes(" ") &&
    Array.from(words_or_braille[0]).every((c) => c === "." || c === "O")
) {
    console.log(fromBraille(words_or_braille));
} else {
    console.log(toBraille(words_or_braille));
}
