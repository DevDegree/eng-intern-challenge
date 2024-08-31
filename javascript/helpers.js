const {
  CAPITAL_FOLLOWS,
  NUMBER_FOLLOWS,
  brailleAlphabet,
  brailleNumber,
  brailleOther,
} = require("./constants");

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

const reverseLookup = (lookup) => {
  return Object.entries(lookup).reduce((acc, curr) => {
    const key = curr[0];
    const value = curr[1];
    acc[value] = key;
    return acc;
  }, {});
};

const brailleToAlphabet = reverseLookup(brailleAlphabet);
const brailleToNumber = reverseLookup(brailleNumber);
const brailleToOther = reverseLookup(brailleOther);

const translateBrailleToEnglish = (string) => {
  const brailleLength = 6;
  let shouldCapitalize = false;
  let asNumber = false;
  let output = "";
  for (let index = 0; index < string.length; index += brailleLength) {
    const element = string.slice(index, index + brailleLength).toUpperCase();

    const isCapitalFollows = element === brailleOther[CAPITAL_FOLLOWS];
    const isNumberFollows = element === brailleOther[NUMBER_FOLLOWS];
    const isSpace = element === brailleOther[" "];

    if (isCapitalFollows) {
      shouldCapitalize = true;
      continue;
    }
    if (isNumberFollows) {
      asNumber = true;
      continue;
    }
    if (isSpace && asNumber) {
      asNumber = false;
    }

    const char = isSpace
      ? brailleToOther[element]
      : asNumber
      ? brailleToNumber[element]
      : brailleToAlphabet[element];
    if (shouldCapitalize) {
      output += char.toUpperCase();
      shouldCapitalize = false;
    } else {
      output += char;
    }
  }
  return output;
};

const translateEnglishToBraille = (string) => {
  let output = "";
  let hasNumberFollows = false;
  for (let index = 0; index < string.length; index++) {
    const char = string[index];

    const isSpace = char === " ";
    const isNumber = !Number.isNaN(Number(char)) && !isSpace;
    const isAlphabet = !isNumber && !isSpace;
    const isCapitalized = isAlphabet && char === char.toUpperCase();

    if (isCapitalized) {
      output +=
        brailleOther["CAPITAL_FOLLOWS"] + brailleAlphabet[char.toLowerCase()];
    } else if (isAlphabet) {
      output += brailleAlphabet[char.toLowerCase()];
    } else if (isNumber && !hasNumberFollows) {
      output += brailleOther["NUMBER_FOLLOWS"] + brailleNumber[char];
      hasNumberFollows = true;
    } else if (isNumber) {
      output += brailleNumber[char];
    } else {
      // should be a space, which also signifies the end of sequence of numbers
      output += brailleOther[char];
      hasNumberFollows = false;
    }
  }
  return output;
};

module.exports = {
  isBraille,
  translateBrailleToEnglish,
  reverseLookup,
  translateEnglishToBraille,
};
