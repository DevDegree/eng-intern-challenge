// Mapping of English alphabet characters to Braille representations

const ENGLISH_TO_BRAILLE = {
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

// Mapping of numeric digits to Braille representations

const NUMBER_TO_BRAILLE = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
};

// Mapping of special symbols (e.g., capital letter indicator) to Braille

const SYMBOL_TO_BRAILLE = {
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

/**
 * Inverts a given dictionary so that keys become values and values become keys.
 * This is essential for translating Braille back to English.
 *
 * @param {Object} dictionary - The dictionary to invert.
 * @returns {Object} - The inverted dictionary.
 */
function invertDict(dictionary) {
  const inverted = {};
  for (let key in dictionary) {
    inverted[dictionary[key]] = key;
  }
  return inverted;
}

/**
 * Checks whether the provided text is in Braille format.
 *
 * @param {Array<string>} text - The text to check, as an array of strings.
 * @returns {boolean} - True if the text is Braille, otherwise false.
 */
function isBraille(text) {
  for (let word of text) {
    if (word.includes(".")) {
      return true;
    }
  }
  return false;
}

/**
 * Converts an English text input to its Braille representation.
 * Handles letters, numbers, capitalization, and spacing.
 *
 * @param {Array<string>} text - The text to convert, as an array of words.
 * @returns {string} - The converted Braille string.
 */

function toBraille(text) {
  const length = text.length;
  let brailleOutput = [];

  // Merge all relevant dictionaries into a single lookup object
  const brailleLookup = {
    ...ENGLISH_TO_BRAILLE,
    ...NUMBER_TO_BRAILLE,
    ...SYMBOL_TO_BRAILLE,
  };

  // Iterate over each word in the input text
  text.forEach((word, ind) => {
    let numberFollows = false;

    // Convert each character in the word
    for (let symbol of word) {
      if (symbol.match(/[A-Z]/)) {
        brailleOutput.push(brailleLookup["capital"]);
      }
      if (symbol.match(/[0-9]/) && !numberFollows) {
        brailleOutput.push(brailleLookup["number"]);
        numberFollows = true;
      }

      // Add the Braille representation of the character
      brailleOutput.push(brailleLookup[symbol.toLowerCase()]);
    }

    if (ind < length - 1) {
      // Do not add space for the last word
      brailleOutput.push(brailleLookup["space"]);
    }
  });

  return brailleOutput.join("");
}

/**
 * Converts a Braille input to its English text representation.
 * Handles letters, numbers, capitalization, and spacing.
 *
 * @param {Array<string>} text - The Braille input to convert, as an array of words.
 * @returns {string} - The converted English string.
 */

function toEnglish(text) {
  let englishOutput = [];

  // Create Braille to English lookup
  const englishLookup = invertDict(ENGLISH_TO_BRAILLE);
  const numberLookup = invertDict(NUMBER_TO_BRAILLE);
  const symbolLookup = invertDict(SYMBOL_TO_BRAILLE);

  // Create list of Braille symbols
  const braille = [];
  text.forEach((word) => {
    for (let ind = 0; ind < word.length; ind += 6) {
      braille.push(word.slice(ind, ind + 6));
    }
  });

  // Construct English output
  let capitalFollows = false;
  let numberFollows = false;
  for (let symbol of braille) {
    if (symbol in symbolLookup) {
      if (symbolLookup[symbol] === "space") {
        englishOutput.push(" ");
        numberFollows = false;
      }

      capitalFollows = symbolLookup[symbol] === "capital";
      numberFollows = symbolLookup[symbol] === "number";
      continue;
    }

    // Letter or number
    if (numberFollows) {
      englishOutput.push(numberLookup[symbol]);
    } else if (capitalFollows) {
      englishOutput.push(englishLookup[symbol].toUpperCase());
    } else {
      englishOutput.push(englishLookup[symbol]);
    }

    capitalFollows = false;
  }

  return englishOutput.join("");
}

/**
 * Main function to execute the script.
 * Determines whether the input is in English or Braille and calls the appropriate conversion function.
 * Outputs the result to the console.
 */

function main() {
  const inputWords = process.argv.slice(2);
  let output = "";

  if (isBraille(inputWords)) {
    output = toEnglish(inputWords);
  } else {
    output = toBraille(inputWords);
  }

  console.log(output);
}

main();
