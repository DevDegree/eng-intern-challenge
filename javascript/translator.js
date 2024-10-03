const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
  };
  
  const brailleNumbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
  };
  
  const brailleSpecials = {
    'capital': '.....O',  // Special character to indicate capital letter
    'number': '.O.OOO'    // Special character to indicate numbers follow
  };
  
  function isBraille(input) {
    return /^[O.]+$/.test(input);
  }
  

  function englishToBraille(input) {
    let result = '';
    for (const char of input) {
      if (char >= 'A' && char <= 'Z') {
        result += brailleSpecials['capital'];  // Add capital indicator
        result += brailleAlphabet[char.toLowerCase()];
      } else if (char >= '0' && char <= '9') {
        result += brailleSpecials['number'];  // Add number indicator
        result += brailleNumbers[char];
      } else {
        result += brailleAlphabet[char];
      }
    }
    return result;
  }
  

  function brailleToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
    
    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.slice(i, i + 6);
  
      if (brailleChar === brailleSpecials['capital']) {
        isCapital = true;
      } else if (brailleChar === brailleSpecials['number']) {
        isNumber = true;
      } else {
        if (isNumber) {
          result += Object.keys(brailleNumbers).find(key => brailleNumbers[key] === brailleChar);
          isNumber = false;  // Reset after processing a number
        } else {
          let letter = Object.keys(brailleAlphabet).find(key => brailleAlphabet[key] === brailleChar);
          result += isCapital ? letter.toUpperCase() : letter;
          isCapital = false;  // Reset after processing one capitalized letter
        }
      }
    }
    
    return result;
  }
  

  const input = process.argv.slice(2).join(' ');  // Join all arguments into a single string

if (isBraille(input)) {
  console.log(brailleToEnglish(input));
} else {
  console.log(englishToBraille(input));
}
