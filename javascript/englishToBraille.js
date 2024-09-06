const { brailleTranslation, brailleToNumber, specialBraille} = require('./alphabet');

const englishToBraille = function(input) {
  let result = "";
  let isNumber = false;  //track number state

  //transofrming object (reverse key value) since we need engl to braille 
  const englishTranslation = Object.fromEntries(
    Object.entries(brailleTranslation).map(([key, value]) => [value, key])
  );
  const englishToNumber = Object.fromEntries(
    Object.entries(brailleToNumber).map(([key, value]) => [value, key])
  );
  const specialEnglish = Object.fromEntries(
    Object.entries(specialBraille).map(([key, value]) => [value, key])
  );

  //loop through input
  for (let i = 0; i < input.length; i++) {
    const char = input[i];
    let nextChar = '';

    //capitalization case
    if (/[A-Z]/.test(char)) {
      result += specialEnglish["capital"];  //Add the capital indicator
      nextChar = englishTranslation[char.toLowerCase()];  //Translate to Braille using lowercase
      isNumber = false;  //reset isNumber flag to false
    }
    
    //lowercase letters 
    else if (englishTranslation[char.toLowerCase()]) {
      nextChar = englishTranslation[char.toLowerCase()];
      isNumber = false;  //reset isNumber flag to false
    }

    //numbers
    else if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += specialEnglish["number"];  //Add number indicator if not already added
        isNumber = true;  //set isNumber flag to false
      }
      nextChar = englishToNumber[char];  //Translate number to Braille
    }

    //special char
    else {
      nextChar = specialEnglish[char];
      isNumber = false;  //reset isNumber flag to false
    }

    //append the Braille char to the result
    result += nextChar;
  }

  return result;
};

module.exports = englishToBraille