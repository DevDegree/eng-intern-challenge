const brailleAlphabet = {
    // Lowercase letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    // Capital and number follows symbols
    'capital': '.....O', 'number': '.O.OOO',
    // Numbers (0-9)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    // special characters
    '.': '..OO.O', ',': 'O.....', '?': '..O..O', '!': '..OOO.', ' ': '......'
  };
  
  const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
  );
  
   // To Check if the input contains 'O' and '.' which indicates it's Braille.
  function isBraille(input) {
    return input.includes('O') || input.includes('.');
  }
  
  function translateToBraille(text) {
    let result = '';
    let isNumber = false;
  
    for (let char of text) {
      if (char === ' ') {
        result += brailleAlphabet[' '];
        isNumber = false;  // Reset number mode after space
      } else if (/[A-Z]/.test(char)) {
        result += brailleAlphabet['capital'] + brailleAlphabet[char.toLowerCase()];
        isNumber = false;  // Reset number mode after capital letter
      } else if (/\d/.test(char)) {
        if (!isNumber) {
          result += brailleAlphabet['number'];
          isNumber = true;
        }
        result += brailleAlphabet[char];
      } else {
        result += brailleAlphabet[char];
        isNumber = false;
      }
    }
  
    return result;
  }
  
  function translateToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
  
    // Split braille input into 6-character chunks
    for (let i = 0; i < braille.length; i += 6) {
      const symbol = braille.substring(i, i + 6);
  
      if (symbol === brailleAlphabet['capital']) {
        isCapital = true;
        continue;
      }
      if (symbol === brailleAlphabet['number']) {
        isNumber = true;
        continue;
      }
  
      let translatedChar = reverseBrailleAlphabet[symbol];
      if (isCapital) {
        translatedChar = translatedChar.toUpperCase();
        isCapital = false;
      }
  
      result += translatedChar;
      if (isNumber) {
        isNumber = /\d/.test(translatedChar); 
      }
    }
  
    return result;
  }
  
  // Main function to determine input type and perform translation
  function translator(input) {
    if (isBraille(input)) {
      return translateToEnglish(input);
    } else {
      return translateToBraille(input);
    }
  }
  
  // Run the script from the command-line
  const input = process.argv.slice(2).join(' ');  // Get input passed in the command-line
  if (input) {
    console.log(translator(input));
  } else {
    console.log("Please provide input to translate.");
  }
  
  