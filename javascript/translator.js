const {
  alphabetToBraille,
  brailleToAlphabet,
  BRAILLE_CAPITAL,
  BRAILLE_CHAR_LENGTH,
  BRAILLE_SPACE,
  BRAILLE_NUMBER,
} = require("./constants");

function isUpperCase(char) {
  return char === char.toUpperCase() && char !== char.toLowerCase();
}

function isCharNumber(char) {
  return char.match(/^\d$/) !== null;
}

const isBraille = (inputString) => {
  let inputArray = [];
  for (let i = 0; i < inputString.length; i += 6) {
    inputArray.push(inputString.slice(i, i + 6));
  }
  const brailleAlphabet = Object.keys(brailleToAlphabet);
  const alphabetChars = inputArray.filter(
    (brailleChar) => !brailleAlphabet.includes(brailleChar)
  );
  return alphabetChars.length === 0;
};

const translateToBraille = (inputString) => {
  let resultString = "";
  let isNumber = false;
  for (char of inputString) {
    if (isUpperCase(char)) {
      resultString += BRAILLE_CAPITAL;
    } else if (isCharNumber(char) && !isNumber) {
      resultString += BRAILLE_NUMBER;
      isNumber = true;
    } else if (char === " ") {
      isNumber = false;
    }
    const alphabetChar = alphabetToBraille[char.toLowerCase()];
    resultString += alphabetChar;
  }
  return resultString;
};

const translateToAlphabet = (inputString) => {
  let resultString = "";
  let isCapital = false;
  let isNumber = false;
  for (let i = 0; i < inputString.length; i += BRAILLE_CHAR_LENGTH) {
    const brailleChar = inputString.slice(i, i + BRAILLE_CHAR_LENGTH);
    if (brailleChar === BRAILLE_CAPITAL) {
      isCapital = true;
      continue;
    } else if (brailleChar === BRAILLE_NUMBER) {
      isNumber = true;
      continue;
    } else if (brailleChar === BRAILLE_SPACE && isNumber) {
      isNumber = false;
    }
    const keyType = isNumber ? "number" : "alphabet";
    const alphabetChar =
      brailleToAlphabet[brailleChar]?.[keyType] ??
      brailleToAlphabet[brailleChar];
    resultString += isCapital ? alphabetChar.toUpperCase() : alphabetChar;
    isCapital = false;
  }
  return resultString;
};

function translateString(inputString) {
  if (isBraille(inputString)) {
    return translateToAlphabet(inputString);
  } else {
    return translateToBraille(inputString);
  }
}

const input = process.argv.slice(2).join(" ");
if (input) {
  console.log(translateString(input));
}
