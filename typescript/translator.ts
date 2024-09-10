const STARTING_INDEX_OF_ARGS = 2;
const BRAILLE_TO_ALPHABET: { [brailleCharacter: string]: string } = {
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
  "......": " ",
  ".....O": "Capital",
  "..OOOO": "Number",
};

function isEnglishString(input: string) {
  return /^[a-zA-Z0-9 ]+$/.test(input);
}

function isBrailleString(input: string) {
  return /^[.O]+$/.test(input);
}

const commandLineInput = process.argv.slice(STARTING_INDEX_OF_ARGS);
const formattedInput = commandLineInput.join(" ");

if (isEnglishString(formattedInput)) {
  console.log("English: ", formattedInput);
} else if (isBrailleString(formattedInput)) {
  console.log("Braille:", formattedInput);
} else {
  console.log("Error, invalid input");
}
/*
node version: 18.20.4

input: string
  - in "English", Alphanumeric, upper/lower, spaces
  - in "Braille": . and O (not zero)
    . white (flat)
    O black (raised)
  - No other special characters will be input

Output: string
  - Only output the translation, NOTHING ELSE

Rules:
  - When a braille "Capital follows" (.....O), only the next symbol is capitalized
  - when a braille "Number follows" (O.O.OO), all following symbols are numbers until a space (......)
  - Each braille character consists of 6 characters

Questions:
  - Will inputs always be English OR Braille, or can it be a mix of both? Assuming it will always be one or the other
  - Will the input always be a valid character? (e.g. English: only alphanumeric + space, Braille: always . and O, length is divisible by 6?)
  - What happens when no arguments are provided? Assuming argument will always be provided
  - What happens if the input is very large? 
  - README.md was not present

  - determine whether input is braille or english
    - if english, translate each letter into braille
    - if braille,
      - divide the string into each character into an array of strings that are 6 chars
      - translate each braille character to english character
    - return translation
  - */
