const ENGLISH_LETTER_TO_BRAILLE = {
  // Letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', 

  // Spaces
  ' ': '......',
};

const NUMBER_TO_BRAILLE = {
  // Numbers
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
  '8': 'O.OO..', '9': '.OO...', '0': '.O....', 

}

const BRAILLE_TO_ENGLISH_LETTER = Object.fromEntries(
  Object.entries(ENGLISH_LETTER_TO_BRAILLE).map(([key, value]) => [value, key])
);

const BRAILLE_TO_NUMBER = Object.fromEntries(
  Object.entries(NUMBER_TO_BRAILLE).map(([key, value]) => [value, key])
);

function isBraille(input) {
  return /^[O.]+$/.test(input) && input.length % 6 == 0;
}

function isCapitalized(char) {
  return /^[A-Z]$/.test(char);
}

function isNumber(char) {
  return /^\d$/.test(char);
}

function englishToBraille(text) {
  let result = "";
  let isNum = false;

  for(const char of text) {
    const lowerChar = char.toLowerCase();

    if(lowerChar in ENGLISH_LETTER_TO_BRAILLE | lowerChar in NUMBER_TO_BRAILLE) {
      // Close `number follow` 
      if(isNum & !isNumber(char)) {
        result += ".O.OOO";
        isNum = false;
      }

      // Handle `number follow`
      if(isNumber(char)) {
        if(!isNum) {
          result += ".O.OOO";
        }
        isNum = true;
        result += NUMBER_TO_BRAILLE[char];
      }      
      // Handle `capital follow`
      else if(isCapitalized(char)) {
        result += ".....O";
        result += ENGLISH_LETTER_TO_BRAILLE[lowerChar];
      }
      else {
        result += ENGLISH_LETTER_TO_BRAILLE[char];
      }
    }
    else {
      console.log(`ERROR: ${char} is not an alphanumerical character!`);
      return `ERROR: ${char} is not an alphanumerical character!`;
    }
  }
  console.log(result);
  return result;
}

function brailledToEnglish(text) {
  const brailleChunk = text.match(/.{1,6}/g);
  let result = "";
  let isNum = false;
  let isCapital = false;

  for(const chunk of brailleChunk) {
    // Handle `capitale follow`
    if(chunk === ".....O") {
      isCapital = true;
      continue;
    }
    // Handle `numbers follow`
    else if(chunk === ".O.OOO") {
      isNum = !isNum;
      continue;
    }
    else {
      if(!chunk in BRAILLE_TO_ENGLISH_LETTER | !chunk in BRAILLE_TO_NUMBER){
        console.log(`ERROR: ${chunk} is not a valid Braille character`);
        return `ERROR: ${chunk} is not a valid Braille character`
      }
      else{
        if(isCapital) {
          result += BRAILLE_TO_ENGLISH_LETTER[chunk].toUpperCase();
          isCapital = false;
        }
        else if(isNum) {
          result += BRAILLE_TO_NUMBER[chunk];
        }
        else {
          result += BRAILLE_TO_ENGLISH_LETTER[chunk];
        }
      }    
    }
  }

  console.log(result);
  return result;
}

console.log(brailledToEnglish(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..") === "Hello world");
console.log(brailledToEnglish(".O.OOOOO.O..O.O...") === "42");
console.log(brailledToEnglish(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....") === "Abc 123");
