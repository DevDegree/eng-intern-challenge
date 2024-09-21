// Constants

const lettersToBraille = new Map([
    ["a", "O....."],
    ["b", "O.O..."],
    ["c", "OO...."],
    ["d", "OO.O.."],
    ["e", "O..O.."],
    ["f", "OOO..."],
    ["g", "OOOO.."],
    ["h", "O.OO.."],
    ["i", ".OO..."],
    ["j", ".OOO.."],
    ["k", "O...O."],
    ["l", "O.O.O."],
    ["m", "OO..O."],
    ["n", "OO.OO."],
    ["o", "O..OO."],
    ["p", "OOO.O."],
    ["q", "OOOOO."],
    ["r", "O.OOO."],
    ["s", ".OO..O"],
    ["t", ".OOOO."],
    ["u", "O...OO"],
    ["v", "O.O.OO"],
    ["w", ".OOO.O"],
    ["x", "OO..OO"],
    ["y", "OO.OOO"],
    ["z", "O..OOO"],
    [" ", "......"],
]);

const brailleToLetters = new Map(
    Array.from(lettersToBraille.entries())
        .map(([letter, braille]) => [braille, letter])
);

// used to convert back and fort between the letter format and the digit format (0123456789)
const digitsAlphabet = "jabcdefghi";

const capitalFollowsChar = ".....O";
const numberFollowsChar = ".O.OOO";

// Begin process

entrypoint(process.argv.slice(2).join(" ").trim());

/**
 *
 * @param input {string}
 */
function entrypoint(input) {
    const is_from_braille = /^[.O]+$/.test(input);

    const result = is_from_braille ? from_braille(input) : to_braille(input);

    console.log(result);
}

/**
 *
 * @param input {string}
 * @returns {string}
 */
function to_braille(input) {
    if (!/^[a-zA-Z 0-9]*$/.test(input))
        throw new Error("Can only convert letters (a-z and A-Z), numbers (0-9) and spaces");

    return input
        .replaceAll(
            /[A-Z]/g,
            (letter) => capitalFollowsChar + lettersToBraille.get(letter.toLowerCase()),
        )
        .replaceAll(
            /(\d+) ?/g,
            (_, digits) =>
                numberFollowsChar +
                digits
                    .split("")
                    .map((digit) => lettersToBraille.get(digitsAlphabet[digit]))
                    .join("") +
                lettersToBraille.get(" "),
        )
        .replaceAll(/[a-z ]/g, (letter) => lettersToBraille.get(letter));
}

/**
 *
 * @param input {string}
 * @returns {string}
 */
function from_braille(input) {
    if (!/^[.O]*$/.test(input))
        throw new Error("Braille input must only contain the characters . and O");
    if (input.length % 6 !== 0)
        throw new Error("Braille input must contain 6 characters per letter");

    const outputLetters = [];

    let numberSignaled = false;
    let capitalSignaled = false;

    for (const brailleChar of input.match(/.{6}/g)) {
        let letter = null;

        switch (brailleChar) {
            case numberFollowsChar:
                numberSignaled = true;
                break;
            case capitalFollowsChar:
                capitalSignaled = true;
                break;
            default:
                letter = brailleToLetters.get(brailleChar);
        }

        if (letter == null) continue; // ignore invalid letters

        if (letter === " ") numberSignaled = false;

        if (numberSignaled) {
            outputLetters.push(digitsAlphabet.indexOf(letter));
        } else if (capitalSignaled) {
            outputLetters.push(letter.toUpperCase());
            capitalSignaled = false;
        } else {
            outputLetters.push(letter);
        }
    }
    return outputLetters.join("");
}
