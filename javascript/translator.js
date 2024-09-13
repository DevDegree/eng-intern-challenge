// Defines all characters to Braille except for special and numeric characters
const alphabetChars = {
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
  "-": "..O..O",
  "/": "..O..O",
  "<": "..O.O.",
  ">": "..OO.O",
  "(": "..OO..",
  ")": "..OO..",
};

const numericChars = {
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
  ".": ".0...0",
};

// Defines special characters
const specialChars = {
  space: "......",
  capital: ".....O",
  numeric: ".O.OOO",
};

const translateAlphaNumeric = (userInput) => {
  let newInput = "";
  const capitalAlphabetRegex = /^[A-Z]/;
  const allChars = { ...numericChars, ...alphabetChars };
  for (const char of userInput) {
    newInput += capitalAlphabetRegex.test(char)
      ? specialChars.capital + allChars[char.toLowerCase()]
      : allChars[char.toLowerCase()];
  }
  return newInput;
};

const replaceAlphabetAndNumber = (userInput) => {
  const alphabetRegex = /^[A-Za-z]/;
  const numberRegex = /^[0-9]/;
  const allNumberRegex = /\d[^a-zA-Z]/gi;

  if (alphabetRegex.test(userInput)) {
    return translateAlphaNumeric(userInput);
  } else if (numberRegex.test(userInput)) {
    if (allNumberRegex.test(userInput)) {
      let newInput = "";
      for (const char of userInput) {
        newInput += numericChars[char.toLowerCase()];
      }
      return specialChars.numeric + newInput;
    } else {
      return specialChars.numeric + translateAlphaNumeric(userInput);
    }
  }
};

const translatorEngToBraille = (userInputList) => {
  let res = [];
  userInputList.forEach((input) => {
    res.push(replaceAlphabetAndNumber(input));
  });
  res = res.join(specialChars.space);
  console.log(
    res,
    res ==
      ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
  );
};

const getAllBrailleChars = (text) => {
  // split text every 6 char
  const length = text.length;
  const splitNumber = 6;
  const totalChars = length / splitNumber;
  let brailleList = [];
  for (let i = 0; i < totalChars; i++) {
    let char = text.slice(i * splitNumber, splitNumber * (i + 1));
    brailleList.push(char);
  }
  return brailleList;
};

const translatorBrailleToEng = (text) => {
  const brailleList = getAllBrailleChars(text);

  const alphabets = Object.values(alphabetChars);
  const numbers = Object.values(numericChars);
  let res = [];
  let isNextCapitalized = false;
  let isNextNumeric = false;
  brailleList.forEach((char) => {
    if (char === specialChars.space) {
      res.push(" ");
      return;
    } else if (char === specialChars.capital) {
      isNextCapitalized = true;
      return;
    } else if (char === specialChars.numeric) {
      res.push("");
      isNextNumeric = true;
    }

    const alphabetIndex = alphabets.findIndex((b) => b === char);
    const numberIndex = numbers.findIndex((b) => b === char);
    if (alphabetIndex > -1 && !isNextNumeric) {
      res.push(
        isNextCapitalized
          ? Object.keys(alphabetChars)[alphabetIndex].toUpperCase()
          : Object.keys(alphabetChars)[alphabetIndex]
      );
      isNextCapitalized = false;
    } else if (numberIndex > -1) {
      res.push(Object.keys(numericChars)[numberIndex]);
    }
  });

  console.log(res.join(""));
  return res.join("");
};

const isBraille = (text) => {
  const regex = /[0\.]/gi;
  return regex.test(text);
};

// const userInput = "Abc 123 xYz".split(" ");
const userInput = process.argv.splice(2);

if (isBraille(userInput.join(""))) {
  translatorBrailleToEng(userInput.join(""));
} else {
  translatorEngToBraille(userInput);
}
