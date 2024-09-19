
const {alphabet, numbers, symbols, follows} = require('./alphabetMapping');

// symbols for accessing "follows"
const CAPITAL = 'CAP';
const NUMBER = 'NUM';
const DECIMAL = 'DEC';


const toEnglish = string => {
  let result = '';
  let numberConvertStarted = false;
  let isCapital = false;
  let isNumber = false;

  // parses a braille string into an array of strings that are 6 characters long
  const brailleArrayString = string.match(/.{1,6}/g);

  for (let brailleSymbol of brailleArrayString) {
    //if number was enabled but nothing matches numbers, then turn of number converter
    if (isNumber && !numbers[brailleSymbol]) {
      isNumber = false;
    }
    // preconditions
    if (follows[brailleSymbol]) {
      // if seen a capital symbol, set flag, go to the next character
      if (follows[brailleSymbol] === CAPITAL) {
        isCapital = true;
        continue;
      }

      // seen a number symbol, set flag and go to the next character
      if (follows[brailleSymbol] === NUMBER) {
        isNumber = true;
        continue;
      }
    }

    // alphabet and symbols conditions
    if (alphabet[brailleSymbol] && !isNumber) {
      result += isCapital ? alphabet[brailleSymbol].toUpperCase() : alphabet[brailleSymbol];
      // reset capital letter flag if it was set before
      if (isCapital) {
        isCapital = false;
      }
    } else if (symbols[brailleSymbol]) {
      result += symbols[brailleSymbol];
    }

    // number conditions
    if (isNumber && numbers[brailleSymbol]) {
      result += numbers[brailleSymbol];
    }
  }

  return result;

}

module.exports = toEnglish;