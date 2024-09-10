const STARTING_INDEX_OF_ARGS = 2;

const input = process.argv.slice(STARTING_INDEX_OF_ARGS);

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
  - */
