// Braille mappings for letters, numbers, and space
const BRAILLE_ALPHANUM = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
  };
  
  // Special Braille indicators for capitalization and numbers
  const BRAILLESPS = {
    'capital': '.....O',
    'number': '.O.OOO'
  };
  
  // Determine if the input is Braille or English
  function textBraille(text) {
    return /^[O.]+$/.test(text);
  }
  
  // Translate English text to Braille
  function translateEtoB(text) {
    let result = [];
    let numberMode = false;
  
    for (let char of text) {
      if (/\d/.test(char) && !numberMode) {
        result.push(BRAILLESPS['number']);
        numberMode = true;
      } else if (/[A-Z]/.test(char)) {
        result.push(BRAILLESPS['capital']);
      } else if (char === ' ') {
        numberMode = false;
      }
  
      result.push(BRAILLE_ALPHANUM[char.toLowerCase()]);
    }
  
    return result.join('');
  }
  
// Translate Braille to English text
function translateBtoE(braille) {
    const reverseMap = Object.fromEntries(Object.entries(BRAILLE_ALPHANUM).map(([k, v]) => [v, k]));
    let result = [];
    let i = 0;
    let numberMode = false;
    let capitalMode = false;
  
    while (i < braille.length) {
      let char = braille.substring(i, i + 6);
  
      if (char === BRAILLESPS['capital']) {
        capitalMode = true;
        i += 6;
        continue;
      } else if (char === BRAILLESPS['number']) {
        numberMode = true;
        i += 6;
        continue;
      }
  
      let translated = reverseMap[char];
  
      if (!translated) {
        console.error(`Error: Unrecognized Braille pattern '${char}' at position ${i}`);
        return; // ERROR HANDLING
      }
  
      if (numberMode) {
        const numberMap = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'};
        translated = numberMap[translated];
      }
  
      if (capitalMode) {
        translated = translated.toUpperCase();
        capitalMode = false;
      }
      
      result.push(translated);
      i += 6;
    }
    
  
    return result.join('');
  }
  
  
  // Main function to handle input and output
  function main() {
    const inputText = process.argv[2];
  
    if (textBraille(inputText)) {
      console.log(translateBtoE(inputText));
    } else {
      console.log(translateEtoB(inputText));
    }
  }
  
  main();

  
  
