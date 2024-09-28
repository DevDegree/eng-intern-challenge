
const BRAILLE_MAP = {

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

  '1': 'O.....',
  '2': 'O.O...',
  '3': 'OO....',
  '4': 'OO.O..',
  '5': 'O..O..',
  '6': 'OOO...',
  '7': 'OOOO..',
  '8': 'O.OO..',
  '9': '.OO...',
  '0': '.OOO..',
  ' ': '......', 
  'cap': '.....O', 
  'num': '.O.OOO' 
};

const BRAILLE_MAP_INVERSE = {};
for (let key in BRAILLE_MAP) {
  if (key !== 'cap' && key !== 'num') {
    BRAILLE_MAP_INVERSE[BRAILLE_MAP[key]] = key;
  }
}

const NUM_MAP = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'0'};
const NUM_MAP_INVERSE = {};
for (let key in NUM_MAP) {
  NUM_MAP_INVERSE[NUM_MAP[key]] = key;
}

function isBrailleInput(input) {
  return input.trim().replace(/[O\. ]/g, '') === '';
}

function englishToBraille(input) {
  let output = '';
  let numberMode = false;

  for (let i = 0; i < input.length; i++) {
    let char = input[i];

    if (char === ' ') {
      output += BRAILLE_MAP[' '];
      numberMode = false;
      continue;
    }

    if (char.match(/[A-Z]/)) {
      output += BRAILLE_MAP['cap'];
      char = char.toLowerCase();
    }

    if (char.match(/[0-9]/)) {
      if (!numberMode) {
        output += BRAILLE_MAP['num'];
        numberMode = true;
      }
      let brailleChar = BRAILLE_MAP[NUM_MAP_INVERSE[char]];
      output += brailleChar;
    } else {
      numberMode = false;
      if (BRAILLE_MAP[char]) {
        output += BRAILLE_MAP[char];
      } else {
        continue;
      }
    }
  }
  return output;
}

function brailleToEnglish(input) {
  let output = '';
  let capitalizeNext = false;
  let numberMode = false;

  let sanitizedInput = input.replace(/ /g, '');
  let cells = [];
  for (let i = 0; i < sanitizedInput.length; i +=6) {
    cells.push(sanitizedInput.slice(i, i+6));
  }

  for (let i = 0; i < cells.length; i++) {
    const cell = cells[i];

    if (cell === BRAILLE_MAP[' ']) {
      output += ' ';
      capitalizeNext = false;
      numberMode = false;
      continue;
    }

    if (cell === BRAILLE_MAP['cap']) {
      capitalizeNext = true;
      continue;
    }

    if (cell === BRAILLE_MAP['num']) {
      numberMode = true;
      continue;
    }

    const char = BRAILLE_MAP_INVERSE[cell];

    if (char) {
      if (numberMode) {
        const num = NUM_MAP[char];
        if (num) {
          output += num;
        } else {
          output += '?'; 
        }
      } else {
        if (capitalizeNext) {
          output += char.toUpperCase();
          capitalizeNext = false;
        } else {
          output += char;
        }
      }
    } else {
      output += '?'; 
    }
  }

  return output.trim();
}

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Please provide input to translate.');
  process.exit(1);
}

const input = args.join(' ');

if (isBrailleInput(input)) {
  console.log(brailleToEnglish(input));
} else {
  console.log(englishToBraille(input));
}
