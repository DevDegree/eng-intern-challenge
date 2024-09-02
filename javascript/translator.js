const brailleMap = {
  // Letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO',

  // Numbers (Braille's numeric indicator followed by letters a-j)
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

  // Special Symbols
  ' ': '......',      // Space
  '#': '.O.OOO',     // Number follows indicator
  'CAP': '.....O',   // Capital follows indicator
  'DEC': '.O...O',   // Decimal follows indicator
  '.': '..OO.O',     // Period (.)
  ',': '..O...',     // Comma (,)
  '?': '..O.OO',     // Question mark (?)
  '!': '..OOO.',     // Exclamation mark (!)
  ':': '..OO..',     // Colon (:)
  ';': '..O.O.',     // Semicolon (;)
  '-': '....OO',     // Hyphen (-)
  '/': '.O..O.',     // Slash (/)
  '<': '.OO..O',     // Less than (<)
  //'>': 'O..OO.',     // Greater than (>) Removed greater than because it somehow is the exact symbol of the letter 'o'
  '(': 'O.O..O',     // Open parenthesis (()
  ')': '.O.OO.'      // Close parenthesis ())
};

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

const isBraille = (input) => /^[O.]+$/.test(input);

const translateToEnglish = (braille) => {
  let result = '';
  let i = 0;
  let capitalizeNext = false;
  let isNumber = false;

  while (i < braille.length) {
    const char = braille.slice(i, i + 6);

    if (char === brailleMap['CAP']) {
      capitalizeNext = true;
    } else if (char === brailleMap['#']) {
      isNumber = true;
    } else {
      let translatedChar = englishMap[char] || '?';
      
      if (isNumber) {
        translatedChar = Object.keys(brailleMap).find(key => brailleMap[key] === char && key >= '0' && key <= '9') || '?';
      }
      
      if (capitalizeNext) {
        translatedChar = translatedChar.toUpperCase();
        capitalizeNext = false;
      }
      
      result += translatedChar;

      if (translatedChar === ' ') {
        isNumber = false;
      }
    }
    i += 6;
  }
  return result;
};

const translateToBraille = (text) => {
  let result = '';
  let wasCapital = false;
  let wasNumber = false;

  for (let i = 0; i < text.length; i++) {
    let char = text[i];
    if (/[A-Z]/.test(char)) {
      if (!wasCapital) {
        result += brailleMap['CAP'];
        wasCapital = true;
      }
      char = char.toLowerCase();
    } else if (/[0-9]/.test(char)) {
      if (!wasNumber) {
        result += brailleMap['#'];
        wasNumber = true;
      }
    } else {
      wasCapital = false;
      wasNumber = false;
    }
    
    result += brailleMap[char] || '......';
  }

  return result;
};

const input = process.argv.slice(2).join(' ');
const output = isBraille(input) ? translateToEnglish(input) : translateToBraille(input);
console.log(output);
