//Mapping Braille to English
const brailleToEnglish = {
  "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", 
  "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", 
  "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
  ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
  "OO.OOO": "y", "O..OOO": "z", ".....O": "cap", ".O.OOO": "num", ".O...O": "dec", "..OO.O": ".",
  "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-",
  ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")", "......": " "
};

//Mapping English to Braille
const englishToBraille = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
  "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
  "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
  "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
  "y": "OO.OOO", "z": "O..OOO", "cap": ".....O", "num": ".O.OOO", "dec": ".O...O", ".": "....OO",
  ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
  "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......"
};

//Mapping Numbers to Braille
const brailleToNumber = {
  "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", 
  "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
};

//Mapping Braille to Numbers
const numberToBraille = {
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
  "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

//To determine if input is Braille or English
const isBraille = (input) => {
  return /^[O\.]+$/.test(input);
};

//Function to translate Braille to English
const translateBrailleToEnglish = (braille) => {
  //Empty string to store results
  let result = "";

  //Check if next character is capitalized or a number
  let isCap = false;
  let isNum = false;

  //Loop through Braille string
  for (let i = 0; i < braille.length; i += 6) {
    //Extract the 6 symbols to analyze
    let symbol = braille.slice(i, i + 6);
    
    //check if symbol is capital indicator
    if (symbol === ".....O") {
      isCap = true;
    }
    //check if the symbol is number indicator
    else if (symbol === ".O.OOO") {
      isNum = true;
    } 
    // Braille character
    else {
      //Translate the Braille symbol to English letter or number
      let char = isNum ? brailleToNumber[symbol] : brailleToEnglish[symbol];

      //If character needs to be capitalized
      if (isCap) {
        char = char.toUpperCase();
        isCap = false;
      }

      result += char;

      //Reset number flag
      if (!isNum || brailleToNumber[symbol] === undefined) {
        isNum = false;
      }
    }
  }

  return result;
};

//Function to translate English to Braille
const translateEnglishToBraille = (english) => {
  let result = "";
  let isNum = false;

  //Loop through each character
  for (let i = 0; i < english.length; i++) {
    //Get current character
    let char = english[i];

    //Check if character is a number
    if (char >= "0" && char <= "9") {
      if (!isNum) {
        result += englishToBraille["num"];
        isNum = true;
      }
      result += numberToBraille[char];
    }
    //Check if character is an uppercase letter 
    else if (char >= "A" && char <= "Z") {
      result += englishToBraille["cap"];
      result += englishToBraille[char.toLowerCase()];
      isNum = false;
    } 
    //Handle other characters
    else {
      result += englishToBraille[char];
      isNum = false;
    }
  }

  return result;
}

//Main function to execute translation based on input
const main = () => {
  //Get the input from command line
  const input = process.argv.slice(2).join(" ");

  if (isBraille(input)) {
    console.log(translateBrailleToEnglish(input));
  } else {
    console.log(translateEnglishToBraille(input));
  }
}

main();