const BRAILLE_LETTER_DICTIONARY = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const BRAILLE_NUMBER_DICTIONARY = {
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
  ".": "..OO.O",
};

// Returns true on the first character in the given string that is a key in the dictionary
// The last two conditions in the .some() method account for false positives from the O character and the period character
const isStringEnglish = (string) =>
  string
    .split("")
    .some(
      (char) =>
        (char.toLowerCase() in BRAILLE_LETTER_DICTIONARY ||
          char in BRAILLE_NUMBER_DICTIONARY) &&
        char !== "." &&
        char !== "O"
    );

const isStringBraille = (string) =>
  !isStringEnglish(string) &&
  (string.includes(".") || string.includes("O")) &&
  string.length % 6 === 0 &&
  string.length > 0;

const convertEnglishToBraille = (char) => BRAILLE_LETTER_DICTIONARY[char];
const convertNumberToBraille = (num) => BRAILLE_NUMBER_DICTIONARY[num];

const convertBrailleToEnglish = (char) =>
  Object.keys(BRAILLE_LETTER_DICTIONARY).find(
    (key) => BRAILLE_LETTER_DICTIONARY[key] === char
  );

const convertBrailleToNumber = (num) =>
  Object.keys(BRAILLE_NUMBER_DICTIONARY).find(
    (key) => BRAILLE_NUMBER_DICTIONARY[key] === num
  );

const isLetterCapital = (letter) => letter === letter.toUpperCase();
const isCharNumber = (char) => !Number.isNaN(Number.parseInt(char));

function translateText(string) {
  let translation = "";
  let isNumber = false;

  if (isStringEnglish(string)) {
    string.split("").forEach((char, index) => {
      const previousChar = string[index - 1];
      const nextChar = string[index + 1];

      // If current char is a space, reset isNumber flag
      if (char === " ") {
        isNumber = false;
      }

      if (isCharNumber(char) && !isNumber) {
        translation += ".O.OOO";
        isNumber = true;
      } else if (char === "." && (isCharNumber(nextChar) || isCharNumber(previousChar))) {
        translation += ".O...O";
      } else if (isLetterCapital(char) && char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) {
        translation += ".....O";
      }

      const translatedChar = isNumber
        ? convertNumberToBraille(char)
        : convertEnglishToBraille(char.toLowerCase());

      // Necessary to prevent undefined from being added to the translation
      translation += translatedChar ? translatedChar : "";
    });

    return translation;
  }

  if (isStringBraille(string)) {
    // This regex splits the string into chunks of 6 characters each (aka valid braille characters)
    const brailleChars = string.match(/.{6}/g);
    let isNumber = false;

    brailleChars.forEach((char, index) => {
      const previousChar = brailleChars[index - 1];

      if (char === ".O.OOO") {
        isNumber = true;
      } else if (char === "......") {
        isNumber = false;
      }

      let translatedChar;

      if (isNumber) {
        translatedChar = convertBrailleToNumber(char);
      } else {
        // Capital letter check (i.e. if previous brailleChar was a capital letter signal, convert translated letter to uppercase)
        translatedChar =
          previousChar === ".....O"
            ? convertBrailleToEnglish(char).toUpperCase()
            : convertBrailleToEnglish(char);
      }

      translation += translatedChar ? translatedChar : "";
    });

    return translation;
  }

  // 'Sad' path
  return ''
}

if (require.main === module) {
  const input = process.argv.slice(2).join(" ");
  if (input && input.length > 0) {
    console.log(translateText(input));
  } else {
    console.log("Please enter a string to translate.");
  }
}
