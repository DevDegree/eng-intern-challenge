// Objects mapping English to Braille and Braille to English (letters and numbers)
const englishToBrailleIndex = {
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
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  " ": "......",
};
const brailleToEnglishLettersIndex = {
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
const brailleToEnglishNumbersIndex = {
  ".OOO..": "0",
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  "......": " ",
};

// Braille prefixes for capital letters and numbers
const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const capitalPrefixBraille = ".....O";
const numberPrefixBraille = ".O.OOO";

// English to Braille translator function
const englishToBrailleTranslator = (string) => {
  const englishArray = string.split("");
  const translatedToBrailleArray = [];
  let isNumber = false;
  let translatedString = "";

  // Loop through English characters and translate to Braille
  for (let i = 0; i < englishArray.length; i++) {
    // Add number prefix if it's a number
    if (numbers.includes(englishArray[i])) {
      if (isNumber === false) {
        translatedToBrailleArray.push(numberPrefixBraille);
        isNumber = true; // Start number mode if not yet started
      }
    }

    // Add capital letter prefix if the letter is uppercase
    else if (
      englishArray[i] === englishArray[i].toUpperCase() &&
      englishArray[i] != " "
    ) {
      translatedToBrailleArray.push(capitalPrefixBraille);
      englishArray[i] = englishArray[i].toLowerCase();
    }
    if (englishArray[i] === " ") {
      isNumber = false; // Reset number mode on space
    }

    // Append corresponding Braille character
    translatedToBrailleArray.push(englishToBrailleIndex[englishArray[i]]);
    translatedString = translatedToBrailleArray.join("");
  }
  return translatedString; // Return the final Braille string
};

// Braille to English translation function
const brailleToEnglishTranslator = (string) => {
  const translatedArray = [];
  let isNumber = false;
  let englishTranslatedString = "";

  // Split Braille input into chunks of 6 characters
  const brailleArray = string.match(/.{6}/g);

  // Loop through Braille characters and translate to English
  for (let i = 0; i < brailleArray.length; i++) {
    // Handle capital letter prefix
    if (brailleArray[i] == capitalPrefixBraille) {
      let englishLetter = brailleToEnglishLettersIndex[brailleArray[i + 1]];
      englishLetter = englishLetter.toUpperCase();
      translatedArray.push(englishLetter);
    }
    // Handle number prefix
    else if (brailleArray[i] == numberPrefixBraille) {
      isNumber = true;
    }
    // Translate normal letters
    else if (brailleArray[i - 1] != capitalPrefixBraille && !isNumber) {
      translatedArray.push(brailleToEnglishLettersIndex[brailleArray[i]]);
    }
    // Translate numbers
    if (isNumber && brailleArray[i] != numberPrefixBraille) {
      translatedArray.push(brailleToEnglishNumbersIndex[brailleArray[i]]);
    } else if (brailleArray[i] == " ") {
      isNumber = false;
    }

    englishTranslatedString = translatedArray.join("");
  }
  return englishTranslatedString; // Return the final English string
};

// Main translator function to detect input type and translate accordingly
const translator = (string) => {
  if (string.includes(".")) {
    return brailleToEnglishTranslator(string);
  } else {
    return englishToBrailleTranslator(string);
  }
};

// Command-line utility to run the translator
const runTranslator = () => {
  // Get the input from the command line
  const input = process.argv.slice(2).join(" ");
  if (!input) {
    console.error("Please provide input to translate.");
    process.exit(1); // Exit if no input provided
  }
  // Translate and output the result
  console.log(translator(input));
};

// Run translator
runTranslator();
