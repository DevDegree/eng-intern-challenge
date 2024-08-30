/** Constants */
const brailleDict = new Map([
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
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  ["CAP", ".....O"],
  ["NUM", ".O.OOO"],
  [" ", "......"],
  ["0", ".OOO.."],
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
//   [".", "..OO.O"],
//   [",", "..O..."],
//   ["?", "..O.OO"],
//   ["!", "..OOO."],
//   [":", "..OOOO"],
//   [";", "..O.O."],
//   ["-", "....OO"],
//   ["/", ".O..O."],
//   ["<", ".OO..O"],
// //   [">", "O..OO."], there is a problem here, same symbol as O
//   ["(", "O.O..O"],
//   [")", ".O.OO."],
]);

const reverseBrailleLetters = new Map([
  ["O.....", "a"],
  ["O.O...", "b"],
  ["OO....", "c"],
  ["OO.O..", "d"],
  ["O..O..", "e"],
  ["OOO...", "f"],
  ["OOOO..", "g"],
  ["O.OO..", "h"],
  [".OO...", "i"],
  [".OOO..", "j"],
  ["O...O.", "k"],
  ["O.O.O.", "l"],
  ["OO..O.", "m"],
  ["OO.OO.", "n"],
  ["O..OO.", "o"],
  ["OOO.O.", "p"],
  ["OOOOO.", "q"],
  ["O.OOO.", "r"],
  [".OO.O.", "s"],
  [".OOOO.", "t"],
  ["O...OO", "u"],
  ["O.O.OO", "v"],
  [".OOO.O", "w"],
  ["OO..OO", "x"],
  ["OO.OOO", "y"],
  ["O..OOO", "z"],
  
//   ["..OO.O", "."],
//   ["..O...", ","],
//   ["..O.OO", "?"],
//   ["..OOO.", "!"],
//   ["..OOOO", ":"],
//   ["..O.O.", ";"],
//   ["....OO", "-"],
//   [".O..O.", "/"],
//   [".OO..O", "<"],
// //   ["O..OO.", ">"],  there is a problem here, same symbol as O
//   ["O.O..O", "("],
//   [".O.OO.", ")"],
]);

const reverseSpecialCharacters = new Map([
  [".O.OOO", "NUM"],
  ["......", " "],
]);

const reverseBrailleNumbers = new Map([
  [".OOO..", "0"],
  ["O.....", "1"],
  ["O.O...", "2"],
  ["OO....", "3"],
  ["OO.O..", "4"],
  ["O..O..", "5"],
  ["OOO...", "6"],
  ["OOOO..", "7"],
  ["O.OO..", "8"],
  [".OO...", "9"],
]);

/**
 * Checks if the given string consists only of the characters 'O' and '.'.
 * @param {string} str - The string to check.
 * @returns {boolean} - Returns true if all characters in the string are either 'O' or '.', otherwise false.
 */
function checkIsBraille(str) {
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== "O" && str[i] !== ".") return false;
  }
  return true && str.length % 6 === 0;
}

/**
 * Checks if the given character is an uppercase letter.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is an uppercase letter, otherwise false.
 */
const isCapitalLetter = (char) => char >= "A" && char <= "Z";

/**
 * Checks if the given character is a lowercase letter.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is a lowercase letter, otherwise false.
 */
const isLowerLetter = (char) => char >= "a" && char <= "z";

/**
 * Checks if the given character is a numeric digit.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is a numeric digit, otherwise false.
 */
const isNumeric = (char) => char >= "0" && char <= "9";

/**
 * Checks if a given character is one of the specified symbols.
 *
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is a symbol, otherwise false.
 */
const isSymbol = (char) =>
  [".", ",", "?", "!", ":", ";", "-", "/", ">", "<", "(", ")"].includes(char);

/**
 * Converts a string of English text into Braille representation.
 * @param {string} str - The string to convert to Braille.
 * @returns {string} - The Braille representation of the input string.
 */
function englishToBraille(str) {
  let numericState = false;
  let result = "";

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    let newChar;
    if (isCapitalLetter(char)) {
      newChar = brailleDict.get("CAP") + brailleDict.get(char.toLowerCase());
    } else if (isLowerLetter(char) /*|| isSymbol(char)*/) {
      newChar = brailleDict.get(char);
    } else if (isNumeric(char)) {
      newChar = brailleDict.get(char);
      if (!numericState) {
        numericState = true;
        newChar = brailleDict.get("NUM") + newChar;
      }
    } else if (char === " ") {
      if (numericState) numericState = false;
      newChar = brailleDict.get(" ");
    }
    // console.log(newChar, "vs", char);
    result += newChar || "";
  }
  return result;
}

/**
 * Converts a string of Braille representation into English text.
 * @param {string} str - The Braille string to convert to English.
 * @returns {string} - The English text representation of the input Braille string.
 */
function brailleToEnglish(str) {
  let result = "";
  let numericState = false;
  for (let i = 0; i < str.length; i += 6) {
    let newChar;
    const char = str.slice(i, i + 6);

    if (char === brailleDict.get("NUM")) {
      numericState = true;
    } else if (char === brailleDict.get(" ")) {
      if (numericState) numericState = false;
      newChar = " ";
    } else if (numericState) {
      newChar = reverseBrailleNumbers.get(char);
    } else if (brailleDict.get("CAP") === char) {
      i += 6;
      let nextChar = str.slice(i, i + 6);
      newChar = reverseBrailleLetters.get(nextChar).toUpperCase();
    } else {
      newChar = reverseBrailleLetters.get(char);
    }
    // console.log(newChar, "vs", char);
    result += newChar || "";
  }
  return result;
}

/**
 * Gets input from command line arguments and converts between Braille and English.
 * @type {string} inputString - The input string obtained from command line arguments.
 */
const inputString = process.argv.slice(2).join(" ");

/**
 * Checks if the input string is Braille.
 * @type {boolean} isBraille - A boolean indicating if the input string is Braille.
 */
const isBraille = checkIsBraille(inputString);

/**
 * Converts the input string based on whether it is Braille or English.
 * @type {string} result - The resulting string after conversion.
 */
const result = isBraille
  ? brailleToEnglish(inputString)
  : englishToBraille(inputString);

console.log(result);
