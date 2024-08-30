// braille -> alphabet
// alphabet -> braille

// Input: .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..
// Output: Abc 123

/**
 * .....O cap
 * O..... a
 * O.O... b
 * OO.... c
 * ...... space
 * .O.OOO number
 * O.O... 2
 * OO.... 3
 * OO.O.. 4
 */

// Input: 42
// Output: .O.OOOOO.O..O.O...

/**
 * .O.OOO number
 * OO.O.. 4
 * O.O... 2
 */

const isBraille = (string) => {
  if (string.length === 0) return false;
  const normalizedString = string.toUpperCase();
  const allowableCharacters = ["O", "."];
  for (let index = 0; index < normalizedString.length; index++) {
    const element = normalizedString[index];
    if (!allowableCharacters.includes(element)) return false;
  }
  return true;
};

module.exports = { isBraille };
