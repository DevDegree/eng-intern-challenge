const CHAR_TO_BRAILLE = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": ".O.OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const NUM_TO_BRAILLE = {
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

const FOLLOW_INDICATORS = {
  capital: ".....O",
  decimal: ".O...O",
  number: ".O.OOO",
};

// Regex Checks
const isBraille = /^[O.]+$/;
const isUppercase = /[A-Z]/;
const isDigit = /\d/;

// Swap the Keys and Values for easier lookups when converting from Braille to English
const BRAILLE_TO_CHAR = Object.fromEntries(
  Object.entries(CHAR_TO_BRAILLE).map(([key, value]) => [value, key])
);

const BRAILLE_TO_NUM = Object.fromEntries(
  Object.entries(NUM_TO_BRAILLE).map(([key, value]) => [value, key])
);

const checkIsBraille = (inputString) => {
  // Test if the string is made up of only O's and .'s.
  return isBraille.test(inputString);
};

const convertEngToBraille = (inputString) => {
  let brailleOutput = "";
  let isNumber = false;

  for (let i = 0; i < inputString.length; i++) {
    const character = inputString[i];

    // Regex check if character is upper case and if so apply the capial follows braille
    if (isUppercase.test(character)) {
      brailleOutput += FOLLOW_INDICATORS.capital;
    } else if (character === "." && isDigit.test(inputString[i - 1])) {
      // When the character is a '.' and comes after a number we add the decimal follows code
      brailleOutput += FOLLOW_INDICATORS.decimal;
      continue;
    } else if (isDigit.test(character) && !isNumber) {
      brailleOutput += FOLLOW_INDICATORS.number;
      isNumber = true;
    }

    // When we encounter a space, add it and disable number mode.
    if (character === " ") {
      brailleOutput += CHAR_TO_BRAILLE[" "];
      isNumber = false;
    } else {
      brailleOutput += isNumber
        ? NUM_TO_BRAILLE[character]
        : CHAR_TO_BRAILLE[character.toLowerCase()] || "";
    }
  }

  return brailleOutput;
};

const convertBrailleToEng = (inputString) => {
  let engOutput = "";
  let capitalize = false;
  let isNumber = false;

  for (let i = 0; i < inputString.length; i += 6) {
    const brailleSymbol = inputString.substring(i, i + 6);

    if (capitalize) {
      engOutput += BRAILLE_TO_CHAR[brailleSymbol].toUpperCase();
      capitalize = false;
      continue;
    }

    // Handle the various follow indicators appropriately
    switch (brailleSymbol) {
      case FOLLOW_INDICATORS.capital:
        capitalize = true;
        break;
      case FOLLOW_INDICATORS.decimal:
        engOutput += ".";
        break;
      case FOLLOW_INDICATORS.number:
        isNumber = true;
        break;
      case CHAR_TO_BRAILLE[" "]:
        isNumber = false;
        engOutput += " ";
        break;
      default:
        engOutput += isNumber
          ? BRAILLE_TO_NUM[brailleSymbol]
          : BRAILLE_TO_CHAR[brailleSymbol];
    }
  }

  return engOutput;
};

const main = () => {
  const args = process.argv.splice(2);
  // Create our input string from the args
  const inputString = [...args].join(" ");

  if (checkIsBraille(inputString)) {
    console.log(convertBrailleToEng(inputString));
  } else {
    console.log(convertEngToBraille(inputString));
  }
};

main();
