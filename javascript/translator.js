const BRAILLE_MAPPING = {
  'a': 'O.....',
  'b': 'O.O...',
  'c': 'OO....',
  'd': 'OO.O..',
  'e': 'O..O..',
  'f': 'OOO...',
  'g': 'OOOO..',
  'h': 'O.OO..',
  'i': '.OO...',
  'j': '.OOO..',
  'k': 'O...O.',
  'l': 'O.O.O.',
  'm': 'OO..O.',
  'n': 'OO.OO.',
  'o': 'O..OO.',
  'p': 'OOO.O.',
  'q': 'OOOOO.',
  'r': 'O.OOO.',
  's': '.OO.O.',
  't': '.OOOO.',
  'u': 'O...OO',
  'v': 'O.O.OO',
  'w': '.OOO.O',
  'x': 'OO..OO',
  'y': 'OO.OOO',
  'z': 'O..OOO',
  'capital': '.....O',
  'number': '.O.OOO',
  ' ': '......' // Space character
};

const NUMBER_MAPPING = {
  '1': 'O.....',
  '2': 'O.O...',
  '3': 'OO....',
  '4': 'OO.O..',
  '5': 'O..O..',
  '6': 'OOO...',
  '7': 'OOOO..',
  '8': 'O.OO..',
  '9': '.OO...',
  '0': '.OOO..'
};

const brailleToEnglish = (input) => {
  return "brailleToEnglish";
};

const englishToBraille = (input) => {
  let result = '';
  let numberMode = false;

  for (let char of input) {
    if (/[a-zA-Z]/.test(char)) { // Regex to check if inputted character is an alphabetic letter
      if (char === char.toUpperCase()) {
        result += BRAILLE_MAPPING['capital'];
      }
      result += BRAILLE_MAPPING[char.toLowerCase()];
      numberMode = false;
    } else if (/[0-9]/.test(char)) { // If inputted character is a number
      if (!numberMode) {
        result += BRAILLE_MAPPING['number'];
        numberMode = true;
      }
      result += NUMBER_MAPPING[char];
    } else if (char === ' ') { // If the inputted character is a space
      result += BRAILLE_MAPPING[' '];
      numberMode = false;
    }
  }

  return result;
};

const translate = (input) => {
  if (/^[O.]+$/.test(input)) { // Regex to check if input is Braille
    return brailleToEnglish(input);
  }
  else {
    return englishToBraille(input);
  }
};

// Calling the main program
const input = process.argv.slice(2).join(' ');
if (input) {
  process.stdout.write(translate(input));
} else {
  process.stderr.write(""); // Error out to match test cases
}