const brailleToEnglish = require('./brailleToEnglish');  // Import the function that translates from braille to engl
const englishToBraille = require('./englishToBraille');  // Import the function that translates from engl to braille

//grab arguments passed from the command line 
const stringToTranslate = process.argv.slice(2).join(' ');

//function that verifies if the given argument is in Braille
const isBraille = function(toTranslate) {
  //Regex to check if input contain O or . only!!!
  return /^[O. ]+$/.test(toTranslate);
}


if (isBraille(stringToTranslate)) {
  //Call the function to translate Braille to English
  //return brailleToEnglish(stringToTranslate);
  console.log(brailleToEnglish(stringToTranslate));
  
} else {
  //Call the function to translate English to Braille
  //return englishToBraille(stringToTranslate);
  console.log(englishToBraille(stringToTranslate));
}
