const { brailleTranslation, brailleToNumber, specialBraille} = require('./alphabet');

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

module.exports = brailleToEnglish

