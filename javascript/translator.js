const brailleMap = {
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
  capitalFollows: ".....O",
  decimalFollows: ".O...O",
  numberFollows: ".O.OOO",
  ["."]: "..OO.O",
  [","]: "..O...",
  ["?"]: "..O.OO",
  ["!"]: "..OOO.",
  [":"]: "..OO..",
  [";"]: "..O.O.",
  ["-"]: "....OO",
  ["/"]: ".O..O.",
  ["<"]: ".OO..O",
  [">"]: "O..OO.",
  ["("]: "O.O..O",
  [")"]: ".O.OO.",
  space: "......",
};
const numberMap = {
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

const brailleToNumberMap = Object.fromEntries(
  Object.entries(numberMap).map(([key, value]) => [value, key])
);

//inverted map of brailleMap where keys are values and values are keys
const brailleToEnglishMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);
const translateWord = (string) => {
  let finalStr = "";
  let hasNumberStarted = false;

  for (const char of string) {
    /* special character processing */
    let appendChar = "";
    const specialCharPattern = /[!@#\$%\^\&*\)\(+=._-]/g;

    if (specialCharPattern.test(char)) {
      if (char === ".") {
        appendChar = brailleMap["decimalFollows"] + brailleMap[char];
      } else {
        appendChar = brailleMap[char];
      }
    } else if (!isNaN(char)) {
      /* number processing */
      if (!hasNumberStarted) {
        appendChar = brailleMap["numberFollows"] + numberMap[char];
        hasNumberStarted = true;
      } else appendChar = numberMap[char];
    } else if (char.match(/[a-z]/i)) {
      /* alphabet processing */
      if (char.toUpperCase() === char) {
        let lowerCaseChar = char.toLowerCase();
        appendChar = brailleMap["capitalFollows"] + brailleMap[lowerCaseChar];
      } else appendChar = brailleMap[char];
    }
    finalStr += appendChar;
  }

  return finalStr;
};
const englishToBrailleTranslator = (string) => {
  return string
    .split(" ")
    .map((word) => translateWord(word))
    .join(brailleMap["space"]);
};

const brailleToEnglishTranslator = (input) => {
  let isCapitalized = false;
  let isFollowedUpByNumbers = false;
  let finalReturn = "";
  //split 6 at a time for easy reading, is reliable as braille is always in a matrix of 3*2
  const brailleInputArr = input.match(/.{6}/g);

  for (brailleSentence of brailleInputArr) {
    let accumulatedCharacters = "";
    /* check for space */
    if (brailleSentence === brailleMap["space"]) {
      isFollowedUpByNumbers = false;
      accumulatedCharacters += " ";
    } else if (brailleSentence === brailleMap["capitalFollows"]) {
      /* check for capitalFollows */
      isCapitalized = true;
    } else if (brailleSentence === brailleMap["numberFollows"]) {
      /* check for numberFollows */
      isFollowedUpByNumbers = true;
    } else if (brailleSentence === brailleMap["decimalFollows"]) {
      /* check for decimalFollows */
      accumulatedCharacters += ".";
    } else if (brailleToEnglishMap[brailleSentence].match(/[a-z]/i)) {
      /* check for alphabet */
      if (isCapitalized) {
        accumulatedCharacters +=
          brailleToEnglishMap[brailleSentence].toUpperCase();
        isCapitalized = false;
      } else if (isFollowedUpByNumbers) {
        accumulatedCharacters += brailleToNumberMap[brailleSentence];
      } else accumulatedCharacters += brailleToEnglishMap[brailleSentence];
    }
    finalReturn += accumulatedCharacters;
  }
  return finalReturn;
};
// modulo of 6 needed to confirm that it is the 3x2 braille matrix
const isBraille = (input) => /^[O.]+$/.test(input) && input.length % 6 === 0;

const translator = (string) => {
  const translatedString = isBraille(string)
    ? brailleToEnglishTranslator(string)
    : englishToBrailleTranslator(string);
  console.log(translatedString);
};

const inputString = process.argv.slice(2).join(" ");
translator(inputString);
