// Take CLI arguments
const userInput = process.argv.slice(2);

// braille letters and prefixes
const brailleCharacters = {
  // Letters
  "a": "O.....",
  "b": "O.O...",
  "c": "OO....",
  "d": "OO.O..",
  "e": "O..O..",
  "f": "OOO...",
  "g": "OOOO..",
  "h": "O.OO..",
  "i": ".OO...",
  "j": ".OOO..",
  "k": "O...O.",
  "l": "O.O.O.",
  "m": "OO..O.",
  "n": "OO.OO.",
  "o": "O..OO.",
  "p": "OOO.O.",
  "q": "OOOOO.",
  "r": "O.OOO.",
  "s": ".OO.O.",
  "t": ".OOOO.",
  "u": "O...OO",
  "v": "O.O.OO",
  "w": ".OOO.O",
  "x": "OO..OO",
  "y": "OO.OOO",
  "z": "O..OOO",

  // Space
  " ": "......",

  // Prefixes
  "#": ".O.OOO",  // Number follows
  "CAP": ".....O",  // Capital follows
};

// braille numbers
const brailleNumbers = {
  // Numbers (same as letters a-j with number sign prefix)
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
}
// determine if given arguments are English or Braille
const languageType = (language) => {
  // Braille will ALWAYS include a period .
  if (language[0].includes('.')) {
    let brailleArray = splitBrailleCharacters(language[0]);
    return brailleToEnglish(brailleArray);
  } else {
    return englishToBraille(language.join(' '));
  }
};

// split the braille characters for each 6 symbols
const splitBrailleCharacters = (braille) => {
  return braille.match(/.{1,6}/g);
}

let capitalize = false;
let isNums = false;

// translate individual Braille characters
const brailleCharacterTranslate = (character) => {
  if (character === '......') {
    isNums = false;
  }
  if (!isNums) {
    for (const char in brailleCharacters) {
      if (brailleCharacters[char] === character) {
        if (char === 'CAP') {
          capitalize = true;
          return '';
        }

        if (char === '#') {
          isNums = true;
          return '';
        }

        if (capitalize) {
          capitalize = false;
          return char.toUpperCase();
        } else {
          return char;
        }
      }
    }
  } else {
    for (const num in brailleNumbers) {
      if (brailleNumbers[num] === character) {
        return num;
      }
    }
  }
}

// construct the English sentence from Braille input
const brailleToEnglish = (brailleArray) => {
  let outputString = '';
  for (const character of brailleArray) {
    outputString += brailleCharacterTranslate(character);
  }
  console.log(outputString);
  return outputString;
}

let firstTimeNum = true;

// translate individual English characters
const englishCharacterTranslate = (character, isNumber) => {
  let output = '';
  if (!isNumber) {
    for (const char in brailleCharacters) {
      if (character === char || character === char.toUpperCase()) {
        if (character === character.toUpperCase() && char !== ' ' && !isNumber) {
          output += brailleCharacters["CAP"]
        }
        output += brailleCharacters[char];
        return output;
      }
    }
  } else {
    for (const num in brailleNumbers) {
      if (character === num) {
        if (firstTimeNum) {
          output += brailleCharacters["#"];
          firstTimeNum = false;
        }
        output += brailleNumbers[character];
        return output;
      }
    }
  }
}

// construct the Braille sentence from English input
const englishToBraille = (sentence) => {
  let outputString = '';
  for (const letter of sentence) {
    if (isNaN(letter) || letter === ' ') {
      outputString += englishCharacterTranslate(letter, false);
    } else {
      outputString += englishCharacterTranslate(letter, true);
    }
  }
  console.log(outputString);
  return outputString;
}

languageType(userInput);



