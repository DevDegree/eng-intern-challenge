// Mapping for English to Braille
const brailleAlphabets = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 'O': '.OOO..',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', '<': '.OO..O', '>': 'O..OO.',
    ' ': '......', 'CAPITAL': '.....O', 'DECIMAL': '.O...O', 'NUMBER': '.O.OOO' // Braille symbols for capital and numbers
  };
  
  // Braille to English 
  const englishAlphabets = Object.fromEntries(
    Object.entries(brailleAlphabets).map(([letter, braille]) => [braille, letter])
  );
  
  // Function to know if input is Braille or English
  function isBraille(input) {
    return input.includes('.') || input.includes('O');
  }
  
  // Translator functions
  function translate(input) {
    if (isBraille(input)) {
      return convertBrailleToEnglish(input);
    } else {
      return convertEnglishToBraille(input);
    }
  }
  
  // Convert from Braille to English
  function convertBrailleToEnglish(input) {
    let letters = '';
    let capitalizeNext = false;
    for (let i = 0; i < input.length; i += 6) {
      let brailleChar = input.slice(i, i + 6);
  
      // Handle capitalization
      if (brailleChar === brailleAlphabets['CAPITAL']) {
        capitalizeNext = true;
        continue;
      }
  
      // Retrieve the letter from the braille symbol
      let letter = englishAlphabets[brailleChar] || '';
  
      // check for > symbol not to mix up with letter o
      if (letter === '>') {
        let prevBraille = input.slice(i - 6, i);
        let nextBraille = input.slice(i + 6, i + 12);
        let prevLetter = englishAlphabets[prevBraille] || '';
        let nextLetter = englishAlphabets[nextBraille] || '';
  
        if (!/\d/.test(prevLetter) && !/\d/.test(nextLetter)) {
          letter = 'o';
        }
      }
  
      // Apply capitalization when required
      if (capitalizeNext) {
        letter = letter.toUpperCase();
        capitalizeNext = false;
      }
  
      letters += letter;
    }
  
    return letters;
  }
  
  // Convert English to Braille
  function convertEnglishToBraille(input) {
    let braille = '';
    for (let char of input) {
      if (char >= 'A' && char <= 'Z') {
        braille += brailleAlphabets['CAPITAL'] + (brailleAlphabets[char.toLowerCase()] || ''); // Capital handling
      } else if (char >= '0' && char <= '9') {
        braille += brailleAlphabets['NUMBER'] + (brailleAlphabets[char] || ''); // Number handling
      } else {
        braille += brailleAlphabets[char.toLowerCase()] || ''; // Default handling
      }
    }
    return braille;
  }
  
  // Terminal input handling
  const args = process.argv.slice(2);
  const input = args.join(' '); 
  if (!input) {
    console.log('Please provide a string to translate.');
  } else {
    console.log(translate(input));
  }
  
 
  