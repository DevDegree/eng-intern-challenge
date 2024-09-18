// Braille to English mapping
const brailleToEnglish = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO..': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '.O....': '1',
    '.O.O..': '2',
    '.OO...': '3',
    '.OOO..': '4',
    '.O..O.': '5',
    '.OOO.O': '6',
    '.OOOO.': '7',
    '.O.OOO': '8',
    '..O...': '9',
    '..O.O.': '0',
    '......': ' ' // Space
  };
  
  // English to Braille mapping
  const englishToBraille = Object.fromEntries(
    Object.entries(brailleToEnglish).map(([braille, english]) => [english, braille])
  );
  
  // Translate Braille to English
  function translateBrailleToEnglish(braille) {
    let english = '';
    const brailleChars = braille.match(/.{6}/g); // Split Braille string into 6-character chunks
  
    brailleChars.forEach(char => {
      english += brailleToEnglish[char] || '?'; // Use '?' for unknown Braille patterns
    });
  
    return english;
  }
  
  // Translate English to Braille
  function translateEnglishToBraille(english) {
    let braille = '';
    for (let char of english.toLowerCase()) {
      if (char === ' ') {
        braille += '......'; // Space
      } else {
        braille += englishToBraille[char] || '......'; // Use '......' for unknown characters
      }
    }
    return braille;
  }
  
  // Detect if the input is Braille or English
  function detectInputType(input) {
    return /^[O.]+$/.test(input) ? 'braille' : 'english';
  }
  
  // Main translation function
  function translate(input) {
    const type = detectInputType(input);
    if (type === 'braille') {
      return translateBrailleToEnglish(input);
    } else {
      return translateEnglishToBraille(input);
    }
  }
  
  // Handle command-line arguments
  const input = process.argv[2]; // Get the input string from the command line
  if (!input) {
    console.error('Please provide a string to translate.');
    process.exit(1);
  }
  
  const output = translate(input);
  console.log(output);