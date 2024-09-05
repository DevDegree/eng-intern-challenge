import { englishToBraille, brailleToEnglish } from './converters/converter.js';
import validator from './validators/validator.js';

function translator() {
  // store user arguments
  const input = process.argv.slice(2).join(' ');

  // call inputChecker to determine whether to translate into braille or english
  const inputType = inputValidator(input);

  // translate and store in a variable
  const translation =
    inputType === 'english' ? englishToBraille(input) : brailleToEnglish(input);
  // account for numbers, capital letters, and spaces
}

translator();
