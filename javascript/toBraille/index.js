
const {alphabet, numbers, symbols, follows} = require('./brailleMapping');

// symbols for accessing "follows"
const CAPITAL = 'CAP';
const NUMBER = 'NUM';

const toBraille = string => {
  let result = '';
  let numberConvertStarted = false;

  for (let letter of string) {

    if (numberConvertStarted && (!letter.match(/[.0-9]/))) {
      numberConvertStarted = false;
    }

    if (letter.match(/[a-z]/)) {   // match lowercase letter

      result += alphabet[letter];
      
    } else if (letter.match(/[A-Z]/)) { // match uppercase letter and add "CAPITAL FOLLOWS"

      result += `${follows[CAPITAL]}${alphabet[letter.toLowerCase()]}`;

    } else if (letter.match(/[.,?!:;\-\/<>\(\)\s]/)) {

      result += symbols[letter];

    } else if (letter.match(/[0-9]/)) { // match digit

      if (!numberConvertStarted) {
        numberConvertStarted = true;
        result += `${follows[NUMBER]}`
      }
      result += numbers[letter];

    }
  }

  return result;
}

module.exports = toBraille;