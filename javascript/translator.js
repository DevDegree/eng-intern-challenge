// mvp
// imports
import { englishToBrailleMap, brailleToEnglishMap } from './maps/maps';
import englishToBraille from './converters/englishToBraille';
import brailleToEnglish from './converters/brailleToEnglish';
import inputChecker from './validators/inputValidator';

// create conversion function
function translator() {
  // store user arguments
  const input = process.argv.slice(2).join(' ');

  // call inputChecker to determine whether to translate into braille or english
  const inputType = inputChecker(input);

  // translate from english to braille
  if (inputType === 'braille') {
    console.log('Braille');
  } else {
    console.log('Alphanumeric');
  }
  // translate from braille to english
  // account for numbers, capital letters, and spaces

  // stretch
  // return an error message if arguments contain invalid characters
  // if argument is braille and contains characters other than "O" or ".", and if argument is not divisible by 6, return an error message
  // if argument is english and contains characters other than letters, numbers, or space, return an error message
}
