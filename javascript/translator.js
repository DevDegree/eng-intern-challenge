class Translator {
  static BRAILLE_MAPPING = {
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

  static NUMBER_MAPPING = {
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

  static brailleToEnglish(input) {
    let result = '';
    let capitalizeNext = false;
    let numberMode = false;

    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.slice(i, i + 6);

      if (brailleChar === this.BRAILLE_MAPPING['capital']) {
        capitalizeNext = true;
      } else if (brailleChar === this.BRAILLE_MAPPING['number']) {
        numberMode = true;
      } else if (brailleChar === this.BRAILLE_MAPPING[' ']) {
        result += ' ';
        numberMode = false;
      } else {
        let char;

        if (numberMode) {
          char = Object.keys(this.NUMBER_MAPPING).find(key => this.NUMBER_MAPPING[key] === brailleChar);
        } else {
          char = Object.keys(this.BRAILLE_MAPPING).find(key => this.BRAILLE_MAPPING[key] === brailleChar);
        }

        if (char) {
          result += capitalizeNext ? char.toUpperCase() : char;
        }

        capitalizeNext = false;
      }
    }

    return result;
  }

  static englishToBraille(input) {
    let result = '';
    let numberMode = false;

    for (let char of input) {
      if (/[a-zA-Z]/.test(char)) { // Regex to check if inputted character is an alphabetic letter
        if (char === char.toUpperCase()) {
          result += this.BRAILLE_MAPPING['capital'];
        }
        result += this.BRAILLE_MAPPING[char.toLowerCase()];
        numberMode = false;

      } else if (/[0-9]/.test(char)) { // If inputted character is a number
        if (!numberMode) {
          result += this.BRAILLE_MAPPING['number'];
          numberMode = true;
        }
        result += this.NUMBER_MAPPING[char];

      } else if (char === ' ') { // If inputted character is a space
        result += this.BRAILLE_MAPPING[' '];
        numberMode = false;
      }
    }

    return result;
  }

  static translate(input) {
    // Regex to check if input is Braille
    return /^[O.]+$/.test(input) ? this.brailleToEnglish(input) : this.englishToBraille(input);
  }
}

// Calling the main program
const input = process.argv.slice(2).join(' '); // Takes terminal/command-line inputs

if (input) {
  process.stdout.write(Translator.translate(input));
} else {
  process.stderr.write(""); // Error out to blank, as per test case
}
