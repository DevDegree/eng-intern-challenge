// English to Braille and Braille to English dictionaries
const BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', // Space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
  };


  console.log(BRAILLE_DICT['a']);

  const REVERSE_BRAILLE_DICT = Object.entries(BRAILLE_DICT).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {});
  
  const CAPITAL_INDICATOR = '.....O';
  const NUMBER_INDICATOR = '..O.OO';
  
  // Function to translate English to Braille
  function englishToBraille(text) {
    let brailleOutput = '';
    let numberMode = false;
  
    for (const char of text) {
      if (char.match(/[A-Z]/)) {
        // Capital letter
        brailleOutput += CAPITAL_INDICATOR;
        brailleOutput += BRAILLE_DICT[char.toLowerCase()];
      } else if (char.match(/[0-9]/)) {
        // Number
        if (!numberMode) {
          brailleOutput += NUMBER_INDICATOR;
          numberMode = true;
          console.log(brailleOutput);
        }
        brailleOutput += BRAILLE_DICT[char];
      } else if (char === ' ') {
        // Space
        brailleOutput += BRAILLE_DICT[' '];
        numberMode = false; // Reset number mode on space
        console.log(brailleOutput);
      } else {
        // Regular letter
        brailleOutput += BRAILLE_DICT[char];
      }
    }
  
    return console.log(brailleOutput);
    
  }

  function brailleToEnglish(braille) {
    let englishOutput = '';
    let index = 0;
    let numberMode = false;
    let capitalMode = false;
  
    while (index < braille.length) {
      const symbol = braille.substring(index, index + 6);
  
      if (symbol === CAPITAL_INDICATOR) {
        capitalMode = true; // Capital letter mode
      } else if (symbol === NUMBER_INDICATOR) {
        numberMode = true; // Number mode
      } else if (symbol === BRAILLE_DICT[' ']) {
        englishOutput += ' '; // Space
        numberMode = false; // Reset number mode after space
      } else {
        let char = REVERSE_BRAILLE_DICT[symbol];
        if (numberMode) {
          // Handle numbers (map Braille a-j to 1-0)
          const numberMap = { 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0' };
          englishOutput += numberMap[char];
        } else {
          // Handle capital letters
          if (capitalMode) {
            englishOutput += char.toUpperCase();
            capitalMode = false; // Reset capital mode after one character
          } else {
            englishOutput += char;
          }
        }
      }
  
      index += 6;
    }
  
    return englishOutput;
  }

  // Function to translate Braille to English
function brailleToEnglish(braille) {
    let englishOutput = '';
    let index = 0;
    let numberMode = false;
    let capitalMode = false;
  
    while (index < braille.length) {
      const symbol = braille.substring(index, index + 6);
  
      if (symbol === CAPITAL_INDICATOR) {
        capitalMode = true; // Capital letter mode
      } else if (symbol === NUMBER_INDICATOR) {
        numberMode = true; // Number mode
      } else if (symbol === BRAILLE_DICT[' ']) {
        englishOutput += ' '; // Space
        numberMode = false; // Reset number mode after space
      } else {
        let char = REVERSE_BRAILLE_DICT[symbol];
        if (numberMode) {
          // Handle numbers (map Braille a-j to 1-0)
          const numberMap = { 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0' };
          englishOutput += numberMap[char];
        } else {
          // Handle capital letters
          if (capitalMode) {
            englishOutput += char.toUpperCase();
            capitalMode = false; // Reset capital mode after one character
          } else {
            englishOutput += char;
          }
        }
      }
  
      index += 6;
    }
  
    return englishOutput;
  }

  // Main translation function
function translate(input) {
    if (/^[O.]+$/.test(input)) {
      // If the input contains only Os and dots, it's Braille
      console.log(brailleToEnglish[input]);
      return brailleToEnglish(input);
    } else {
      // Otherwise, it's English
      console.log(englishToBraille[input]);
      return englishToBraille(input);
    }
  }
  
  // Example usage from command line arguments
  if (process.argv.length > 2) {
    const input = process.argv.slice(2).join(' '); // Join all command line arguments into a single string
    console.log(translate(input));
  } else {
    console.log("Please provide input to translate.");
  }