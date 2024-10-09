// mappings
const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
  };
  
  const brailleSpecial = {
    capital: '.....O',
    number: '.O.OOO'
  };
  

  const englishFromBraille = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
  );
  
  function isBraille(input) {
    return /^[O.]+$/.test(input);
  }
  
  //  English to Braille
  function englishToBraille(input) {
    let result = '';
    let isNumber = false;
  
    for (let char of input) {
      if (char >= 'A' && char <= 'Z') {
        result += brailleSpecial.capital + brailleAlphabet[char.toLowerCase()];
      } else if (char >= '0' && char <= '9') {
        if (!isNumber) {
          result += brailleSpecial.number;
          isNumber = true;
        }
        result += brailleAlphabet[char];
      } else {
        result += brailleAlphabet[char];
        if (char === ' ') {
          isNumber = false;
        }
      }
    }
  
    return result;
  }
  
  // Braille to English
  function brailleToEnglish(input) {
    let result = '';
    let i = 0;
    let isCapital = false;
    let isNumber = false;
  
    while (i < input.length) {
      let brailleChar = input.slice(i, i + 6);
  
      if (brailleChar === brailleSpecial.capital) {
        isCapital = true;
        i += 6;
        continue;
      } else if (brailleChar === brailleSpecial.number) {
        isNumber = true;
        i += 6;
        continue;
      }
  
      let char = englishFromBraille[brailleChar];
  
      if (isCapital) {
        char = char.toUpperCase();
        isCapital = false;
      }
  
      if (isNumber) {
        isNumber = false;
      }
  
      result += char;
      i += 6;
    }
  
    return result;
  }
  

  function translate(input) {
    if (isBraille(input)) {
      return brailleToEnglish(input);
    } else {
      return englishToBraille(input);
    }
  }
  

  const input = process.argv.slice(2).join(' ');
  console.log(translate(input));
  