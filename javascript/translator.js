// Mapping from Braille to English characters
const brail_to_eng = {
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
  "......": " ",
};

// Mapping from English characters to Numbers
const char_to_num = {
  a: "1",
  b: "2",
  c: "3",
  d: "4",
  e: "5",
  f: "6",
  g: "7",
  h: "8",
  i: "9",
  j: "0",
};

/**
 * Inverts the key-value mappings on the given object
 * @param {Object} obj
 * @returns {Object} inverted mapping
 */
function make_inverse(obj) {
  let inverse = {};
  for (let key in obj) {
    inverse[obj[key]] = key;
  }
  return inverse;
}

// Mapping from English to Braille characters
const eng_to_brail = make_inverse(brail_to_eng);

// Mapping from Numbers to English characters
const num_to_char = make_inverse(char_to_num);

// Constants for Braille translation
const CAPITAL_FOLLOWS = ".....O";
const NUMBER_FOLLOWS = ".O.OOO";

/**
 * Determines whether the given string is a valid Braille string.
 * If the string length is divisible by 6 and contains only 'O' and '.', it is a valid braille string.
 * We do not check individual characters, as translation functions will handle that.
 *
 * @param {String} str
 * @returns {Boolean} true if the given string is a valid braille string, false otherwise
 */
function is_valid_braille_str(str) {
  if (str.length % 6 !== 0) {
    return false;
  }
  for (let char of str) {
    if (char !== "O" && char !== ".") {
      return false;
    }
  }
  return true;
}

/**
 * Translate a given braille string into an alphanumerical string
 * @param {String} braille braile encoded string (as described in the challenge)
 * @returns {String} decoded alphanumerical string
 * @throws {Error} if the input string contains characters that cannot be translated
 */
function translate_to_eng(braille) {
  let result = "";
  let isNum = false;
  let isCap = false;

  for (let i = 0; i < braille.length; i += 6) {
    let brailleChar = braille.slice(i, i + 6);
    let engChar = brail_to_eng[brailleChar];

    if (engChar === " ") {
      // Space character resets number flag
      result += " ";
      isNum = false;
    } else if (brailleChar === CAPITAL_FOLLOWS) {
      isCap = true;
    } else if (brailleChar === NUMBER_FOLLOWS) {
      isNum = true;
    } else {
      // Here, we know we need to have a valid character
      if (engChar === undefined) {
        throw new Error("Invalid character in input");
      }

      // Capitalize, convert to number, or leave as is
      if (isCap) {
        result += engChar.toUpperCase();
        isCap = false;
      } else if (isNum) {
        result += char_to_num[engChar];
      } else {
        result += engChar;
      }
    }
  }
  return result;
}

/**
 * Translate a given alphanumerical string into a braille string
 * @param {String} eng alphanumerical string
 * @returns {String} braille encoded string
 * @throws {Error} if the input string contains characters that cannot be translated
 */
function translate_to_braille(eng) {
  let result = "";
  let isNum = false;

  for (let char of eng) {
    if (char === " ") {
      result += "......";
      isNum = false;
    } else if (char >= "0" && char <= "9") {
      if (!isNum) {
        result += NUMBER_FOLLOWS;
        isNum = true;
      }
      result += eng_to_brail[num_to_char[char]];
    } else {
      if (char === char.toUpperCase()) {
        result += CAPITAL_FOLLOWS;
      }
      let brailleChar = eng_to_brail[char.toLowerCase()];
      if (brailleChar === undefined) {
        throw new Error("Invalid character in input");
      }
      result += brailleChar;
    }
  }
  return result;
}

// Execute the program
if (process.argv.length > 2) {
  // Join all arguments into a single string (ignore 'node' and 'translator.js')
  let input = process.argv.slice(2).join(" ");

  try {
    if (is_valid_braille_str(input)) {
      console.log(translate_to_eng(input));
    } else {
      console.log(translate_to_braille(input));
    }
  } catch (err) {
    console.error(err.message);
  }
} else {
  console.error("Usage: node translator.js <input>");
}
