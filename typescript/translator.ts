const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No message provided for translation.');
  console.log('Usage: ts-node translator.ts <message>');

  process.exit(1);
}

const message = args.join(' ');

// Translation table
const braille = {
  a: 'O.....',
  b: 'O.O...',
  c: 'OO....',
  d: 'OO.O..',
  e: 'O..O..',
  f: 'OOO...',
  g: 'OOOO..',
  h: 'O.OO..',
  i: '.OO...',
  j: '.OOO..',
  k: 'O...O.',
  l: 'O.O.O.',
  m: 'OO..O.',
  n: 'OO.OO.',
  o: 'O..OO.',
  p: 'OOO.O.',
  q: 'OOOOO.',
  r: 'O.OOO.',
  s: '.OO.O.',
  t: '.OOOO.',
  u: 'O...OO',
  v: 'O.O.OO',
  w: '.OOO.O',
  x: 'OO..OO',
  y: 'OO.OOO',
  z: 'O..OOO',
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
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  '!': '..OOO.',
  ':': '..OO..',
  ';': '..O.O.',
  _: '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.',
  ' ': '......',
};

const special = {
  cap: '.....O',
  dec: '.O...O',
  num: '.O.OOO',
};

/**
 * Translate a message in English to Braille
 * @param message - The message to translate
 * @returns The translated message in Braille
 */
const translateToBraille = (message: string) => {
  let result = '';
  let flagNum = false;

  for (let i = 0; i < message.length; i++) {
    const char = message[i].toLowerCase();
    const isUpperCase = message[i] !== char;

    if (isUpperCase) result += special.cap;

    if (/[0-9]/.test(char) && !flagNum) {
      result += special.num;
      flagNum = true;
    }

    if (char === ' ') flagNum = false;

    if (char === '.') result += flagNum ? special.dec : braille[char];
    else if (braille[char]) result += braille[char];
  }

  return result;
};

/**
 * Translate a message in Braille to English
 * @param message - The message to translate
 * @returns The translated message in English
 */
const translateToEnglish = (message: string) => {
  let result = '';
  let flagNum = false;
  let flagCap = false;

  for (let i = 0; i < message.length; i += 6) {
    const char = message.slice(i, i + 6);
    const key = Object.keys(braille).filter((key) => braille[key] === char);

    if (key.length > 1) {
      if (flagNum) result += key[0];
      else if (flagCap) {
        result += key[1].toUpperCase();
        flagCap = false;
      } else result += key[1];
    } else if (key.length > 0) {
      result += flagCap ? key[0].toUpperCase() : key[0];
      flagCap = false;
    }

    if (char === special.cap) flagCap = true;
    if (char === special.num) flagNum = true;
    if (char === special.dec) result += '.';
    if (key[0] === ' ') flagNum = false;
  }

  return result;
};

const isEnglish = /^[a-zA-Z0-9 ]+$/.test(message);

if (isEnglish) {
  console.log(translateToBraille(message));
} else {
  console.log(translateToEnglish(message));
}
