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

function brailleToEnglish(input) {}

module.exports = {
  englishToBraille,
  brailleToEnglish,
};
