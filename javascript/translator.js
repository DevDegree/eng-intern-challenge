//import object from alphabet.js
const { brailleTranslation, englishTranslation, brailleToNumber, englishToNumber, specialBraille, specialEnglish } = require('./alphabet');

//grab arguments passed from the command line 
const stringToTranslate = process.argv.slice(2).join(' ');

// function that verifies if the given argument is in Braille
const isBraille = function(toTranslate) {
  // Regex to check if input contain O or . only!!!
  return /^[O. ]+$/.test(toTranslate);
}

//function to translate from English to Braille
const brailleToEnglish = function(input) {
  
}

//function to translate from English to Braille
const englishToBraille = function(input) {
  
}

if (isBraille(stringToTranslate)) {
  // Call the function to translate Braille to English
  // return brailleToEnglish(stringToTranslate)
  console.log("the argument is in Braille")
} else {
  // Call the function to translate English to Braille
  // return englishToBraille(stringToTranslate)
  console.log("the argument is in English")
}