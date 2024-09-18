const {
  englishToBrailleLetters,
  englishToBrailleNumbers,
  englishToBrailleSpecialChars,
  brailleToEnglishLetters,
  brailleToEnglishNumbers,
  brailleToEnglishSpecialChars,
  isInputBraille,
} = require('./utils');

// Translate the Braille input to English
const translateBrailleToEnglish = (brailleInput) => {
  // track capital char
  let isCapital = false;
  // track number
  let isNumber = false;

  let result = '';

  // iterate over the braille input
  for (let i = 0; i < brailleInput.length; i += 6) {
    let braille = brailleInput.substring(i, i + 6);

    // Translate:
    // potential uppercase
    if (isCapital) {
      result += brailleToEnglishLetters[braille].toUpperCase();
      // reset
      isCapital = false;
    }

    // space
    else if (braille == englishToBrailleSpecialChars[' ']) {
      result += brailleToEnglishSpecialChars[braille];
      // reset
      isNumber = false;
    }

    // number
    else if (isNumber) {
      result += brailleToEnglishNumbers[braille];
    } else if (braille == englishToBrailleSpecialChars['capital']) {
      isCapital = true;
    } else if (braille == englishToBrailleSpecialChars['number']) {
      isNumber = true;
    } else {
      result += brailleToEnglishLetters[braille];
    }
  }
  return result;
};

// Translate the English input to Braille
const translateEnglishToBraille = (englishInput) => {
  // output
  let result = '';
  // track number
  let isNumber = false;

  for (i = 0; i < englishInput.length; ++i) {
    let english = englishInput[i];

    // translate uppercase
    if (english >= 'A' && english <= 'Z') {
      result +=
        englishToBrailleSpecialChars['capital'] +
        englishToBrailleLetters[english.toLowerCase()];
    }
    // translate a space
    else if (english == ' ') {
      result += englishToBrailleSpecialChars[english];
      isNumber = false;
    }
    // translate number
    else if (english >= '0' && english <= '9') {
      if (!isNumber) {
        result += englishToBrailleSpecialChars['number'];
        isNumber = true;
      }
      result += englishToBrailleNumbers[english];
    }
    // translate lowercase alphabet
    else {
      result += englishToBrailleLetters[english];
    }
  }

  return result;
};

const translate = (input) => {
  if (isInputBraille(input)) return translateBrailleToEnglish(input);
  else return translateEnglishToBraille(input);
};

// Parse  the input
const input = process.argv.slice(2).join(' ');

// Get the output
const output = translate(input);

// Log the output
console.log(output);
