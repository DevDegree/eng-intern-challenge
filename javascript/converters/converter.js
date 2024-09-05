const { englishToBrailleMap, brailleToEnglishMap } = require('../maps/maps.js');

function englishToBraille(input) {
  // define translated string variable
  let translation = '';

  // regular expressions
  const regex = {
    separator: /[^ ]+| +/g,
    spaces: /^\s*$/,
    numbers: /^\d+$/,
    letters: /^[A-Za-z]+$/,
    uppercase: /^[A-Z]$/,
  };
  // separate input string by space
  const sequences = input.match(regex.separator);

  // iterate through sequences array
  for (const sequence of sequences) {
    // check if sequence is spaces
    if (regex.spaces.test(sequence)) {
      for (const char of sequence) {
        translation += '......';
      }
    }
    // check if sequence is numbers
    else if (regex.numbers.test(sequence)) {
      // insert braille number signifier
      translation += '.O.OOO';
      for (const char of sequence) {
        translation += englishToBrailleMap.numbers[char];
      }
    }
    // check if sequence is letters
    else if (regex.letters.test(sequence)) {
      for (const char of sequence) {
        // check if uppercase
        if (regex.uppercase.test(char)) {
          // insert braille uppercase signifier
          translation += '.....O';
        }

        translation += englishToBrailleMap.letters[char.toUpperCase()];
      }
    }
  }

  // return translation
  return translation;
}

function brailleToEnglish(input) {
  // separate string into sequences of six characters
  const sequences = input.match(/.{1,6}/g);
  // define translated string variable
  let translation = '';
  // define toggles for capital letters and numbers
  let isCapitalized = false;
  let isNumber = false;

  // iterate through each sequence
  for (const sequence of sequences) {
    // check if sequence is number signifier
    if (sequence === '.O.OOO') {
      isNumber = true;
    }
    // check if sequence is capital letter signifier
    else if (sequence === '.....O') {
      isCapitalized = true;
    }
    // else, convert and insert character
    else {
      // insert space
      if (sequence === '......') {
        translation += ' ';
        // turn off number toggle
        isNumber = false;
      }
      // if isNumber, insert number
      else if (isNumber) {
        translation += brailleToEnglishMap.numbers[sequence];
      }
      // if isCapitalized, insert uppercase letter
      else if (isCapitalized) {
        translation += brailleToEnglishMap.letters[sequence];
        // turn off capitalization toggle
        isCapitalized = false;
      }
      // otherwise, insert lowercase letter
      else {
        translation += brailleToEnglishMap.letters[sequence].toLowerCase();
      }
    }
  }

  return translation;
}

module.exports = {
  englishToBraille,
  brailleToEnglish,
};
