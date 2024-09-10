const brailleToEnglish = {
  "O.....": "A",
  "O.O...": "B",
  "OO....": "C",
  "OO.O..": "D",
  "O..O..": "E",
  "OOO...": "F",
  "OOOO..": "G",
  "O.OO..": "H",
  ".OO...": "I",
  ".OOO..": "J",
  "O...O.": "K",
  "O.O.O.": "L",
  "OO..O.": "M",
  "OO.OO.": "N",
  "O..OO.": "O",
  "OOO.O.": "P",
  "OOOOO.": "Q",
  "O.OOO.": "R",
  ".OO.O.": "S",
  ".OOOO.": "T",
  "O...OO": "U",
  "O.O.OO": "V",
  ".OOO.O": "W",
  "OO..OO": "X",
  "OO.OOO": "Y",
  "O..OOO": "Z",
  "......": " ",
};

const brailleToNumbers = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const SPACE = "......";
const CAPITAL_FOLLOWS = ".....O";
const NUMBER_FOLLOWS = ".O.OOO";
const DECIMAL_FOLLOWS = ".O...O";

const englishToBraille = Object.keys(brailleToEnglish).reduce((acc, e) => {
  const key = brailleToEnglish[e];
  const value = e;
  acc[key] = value;
  return acc;
}, {});

const numbersToBraille = Object.keys(brailleToNumbers).reduce((acc, e) => {
  const key = brailleToNumbers[e];
  const value = e;
  acc[key] = value;
  return acc;
}, {});

const allEnglishToBraille = {
  ...englishToBraille,
  ...numbersToBraille,
};

const upperCaseEnglishCharacters = Object.keys(englishToBraille);
const lowerCaseEnglishCharacters = upperCaseEnglishCharacters
  .join("")
  .toLowerCase()
  .split("");
const numbers = Object.keys(numbersToBraille).map((e) => parseInt(e));

const english = [
  ...upperCaseEnglishCharacters,
  ...lowerCaseEnglishCharacters,
  ...numbers,
];

function translateBrailleToEnglish(inputString) {
  const splitFactor = 6;
  const braille = [];
  let makeUpperCase = false;
  let checkNumbers = false;
  let addDecimal = false;
  let english = "";
  for (let i = 0; i < inputString.length; i = i + 6) {
    braille.push(inputString.slice(i, i + 6));
  }

  for (let i = 0; i < braille.length; i++) {
    if (braille[i] === CAPITAL_FOLLOWS) {
      makeUpperCase = true;
      continue;
    } else if (braille[i] === NUMBER_FOLLOWS) {
      checkNumbers = true;
      continue;
    } else if (braille[i] === DECIMAL_FOLLOWS) {
      addDecimal = true;
      continue;
    }

    if (checkNumbers) {
      if (braille[i] !== SPACE) {
        english = english + brailleToNumbers[braille[i]];
      } else {
        english = english + brailleToEnglish[braille[i]];
        checkNumbers = false;
      }
    } else {
      if (makeUpperCase) {
        english = english + brailleToEnglish[braille[i]];
        makeUpperCase = false;
      } else {
        english = english + brailleToEnglish[braille[i]].toLowerCase();
      }
    }
  }
  console.log(english);
}

function translateEnglishToBraille(inputString) {
  let braille = "";
  let prevLetter = "";
  const regexToCheckUpperCase = /^[A-Z]$/;
  const regexToCheckLowerCase = /^[a-z]$/;
  const regexToCheckNumber = /^[0-9]$/;

  for (let i = 0; i < inputString.length; i++) {
    const letter = inputString[i];

    if (i > 0) {
      prevLetter = inputString[i - 1];
    }
    if (regexToCheckUpperCase.test(letter)) {
      braille = braille + CAPITAL_FOLLOWS;
      braille = braille + allEnglishToBraille[letter];
    }

    if (regexToCheckLowerCase.test(letter)) {
      const capitalLetter = letter.toUpperCase();
      braille = braille + allEnglishToBraille[capitalLetter];
    }

    if (regexToCheckNumber.test(letter)) {
      const isPrevNumber = regexToCheckNumber.test(prevLetter);
      const isFirstLetter = i === 0 ? true : false;
      const isNewSentence = prevLetter === " " ? true : false;

      if (!isPrevNumber || isFirstLetter || isNewSentence) {
        braille = braille + NUMBER_FOLLOWS;
      }
      braille = braille + allEnglishToBraille[letter];
    }

    if (letter === " ") {
      braille = braille + SPACE;
    }
  }

  console.log(braille);
}

function translate(inputArg) {
  let inputString = inputArg[0];

  // determine if input string is english or braille
  const regexToCheckBraille = /^[O.]+$/;

  if (regexToCheckBraille.test(inputString) && inputString.length % 6 === 0) {
    // translate braille to english
    translateBrailleToEnglish(inputString);
  } else {
    if (inputArg.length > 1) {
      inputString = inputArg.join(" ");
    }
    // translate english to braille
    translateEnglishToBraille(inputString);
  }
}

translate(process.argv.slice(2));
