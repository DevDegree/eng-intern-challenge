const {
  englishToBraille,
  brailleToEnglish,
} = require('./converters/converter.js');
const validator = require('./validators/validator.js');

function translator() {
  // store user arguments
  const input = process.argv.slice(2).join(' ');

  // call inputChecker to determine whether to translate into braille or english
  const inputType = validator(input);

  // translate and store in a variable
  const translation =
    inputType === 'english' ? englishToBraille(input) : brailleToEnglish(input);
  console.log(translation);

  // return translation
  return translation;
}

translator();
