const brailleLetters = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
  'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
  's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO',
  '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
  '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
  ' ': '......', 'CAPITAL': '.....O', 'NUMBER': '.O.OOO'
};


const brailleNumbers = {
  '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
  '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '>': 'O..OO.', '<': '.OO..O',
};

// Create reverse mapping for letters
const englishLetters = Object.fromEntries(
  Object.entries(brailleLetters).map(([letter, braille]) => [braille, letter])
);

// Create reverse mapping for numbers
const englishNumbers = Object.fromEntries(
  Object.entries(brailleNumbers).map(([number, braille]) => [braille, number])
);

function isBraille(input) {
  return input.includes('.') && input.includes('O');
}


function translate(input) {
  if (isBraille(input)) {
    return convertBrailleToEnglish(input);
  } else {
    return convertEnglishToBraille(input);
  }
}


function convertBrailleToEnglish(input) {
  let letters = '';
  let capitalizeNext = false;
  let numberMode = false;

  for (let i = 0; i < input.length; i += 6) {
    let brailleChar = input.slice(i, i + 6);
    // Handle capitalization
    if (brailleChar === brailleLetters['CAPITAL']) {
      capitalizeNext = true;
      continue;
    }
    // Handle number mode
    if (brailleChar === brailleLetters['NUMBER']) {
      numberMode = true;
      continue;
    }
    let letter = '';

    if (numberMode) {
      letter = englishNumbers[brailleChar];
      if (letter === undefined) {
        numberMode = false; // Turn off number mode if the character is not a number
        // Reprocess the brailleChar in letter mode
        letter = englishLetters[brailleChar] || '';
      }
    } else {
      letter = englishLetters[brailleChar] || '';
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


function convertEnglishToBraille(input) {

  let braille = '';
  let numberMode = false;
  for (let char of input) {

    if (char >= 'A' && char <= 'Z') {
      if (numberMode) {
        numberMode = false;
        braille += '';
      }
      braille += brailleLetters['CAPITAL'] + (brailleLetters[char.toLowerCase()] || ''); // Capital handling
    } else if (char >= '0' && char <= '9') {
      if (!numberMode) {
        numberMode = true;
        braille += brailleLetters['NUMBER']; // Enter number mode
      }
      braille += (brailleNumbers[char] || ''); // Number handling
    } else {
      if (numberMode) {
        numberMode = false;
        braille += '';
      }
      braille += brailleLetters[char.toLowerCase()] || ''; // Default handling
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