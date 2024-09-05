//import object from alphabet.js
const { brailleTranslation, brailleToNumber, specialBraille} = require('./alphabet');

//grab arguments passed from the command line 
const stringToTranslate = process.argv.slice(2).join(' ');

//function that verifies if the given argument is in Braille
const isBraille = function(toTranslate) {
  //Regex to check if input contain O or . only!!!
  return /^[O. ]+$/.test(toTranslate);
}

//function to translate from English to Braille
const brailleToEnglish = function(input) {
  let result = "";
  let isCapital = false;  //track capitalization state
  let isNumber = false;   //track number state
  let isDecimal = false;  //track decimal state
  let nextChar; 

  //loop through input to split it in 6 char
  for (let i = 0; i < input.length; i += 6) {
    //Get the current Braille character (6 characters long)
    const inputChar = input.slice(i, i + 6);

    //verify if next char(s) is captial, decimal or number
    if (specialBraille[inputChar]) {
      const specialChar = specialBraille[inputChar];

      switch (specialChar) {
        case 'capital':
          isCapital = true;  //Set flag for capital
          break;
        
        case 'number':
          isNumber = true;   //Set flag for numbers
          break;
        
        case 'decimal':
          isDecimal = true;  //Set flag for decimal
          break;
        
        default: //If none of the cases match, do nothing
          console.log("Special Char not valid");  //If none of the cases match, error message
      }
      continue;
    }

    if (isNumber) {
      //char is number
      nextChar = brailleToNumber[inputChar];  //grab the number from brailleToNumber object
      if (inputChar === "......") {
        isNumber = false;  //reset isNumber flag to false
      }
    //char not a number
    } else {
      nextChar = brailleTranslation[inputChar];  //grab the letter from brailleTranslation object
    }

    //
    if (isDecimal) {
      result += '.';  //Add decimal point before the number
      isDecimal = false;  //reset isDecimal flag to false
    }

    //
    if (isCapital) {
      nextChar = nextChar.toUpperCase();  //Capitalize letter
      isCapital = false;  //reset isNumber flag to false
    }

    //Append the translated character to the result string
    result += nextChar;

  }
  
  return result;
}

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






if (isBraille(stringToTranslate)) {
  //Call the function to translate Braille to English
  //return brailleToEnglish(stringToTranslate);
  console.log(brailleToEnglish(stringToTranslate));
  
} else {
  //Call the function to translate English to Braille
  //return englishToBraille(stringToTranslate);
  console.log(englishToBraille(stringToTranslate));
}
