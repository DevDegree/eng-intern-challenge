type CharactersToBrailleMap = { [key: string]: string };
type NumbersToBrailleMap = { [key: string]: string };
type BraileToCharactersMap = { [key: string]: string };

const swapKeyValues = (
  obj: CharactersToBrailleMap | NumbersToBrailleMap
): BraileToCharactersMap => {
  const swapped: BraileToCharactersMap = {};

  for (const [key, value] of Object.entries(obj)) {
    swapped[value] = key;
  }

  return swapped;
};

const capitalFollows = '.....O';
const decimalFollows = '.O...O';
const numberFollows = '.O.OOO';

const charactersToBraille: CharactersToBrailleMap = {
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
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  '!': '..OOO.',
  ':': '..O.O.',
  '-': '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.',
  ' ': '......',
};
const numbersToBraille: NumbersToBrailleMap = {
  1: 'O.....',
  2: 'O.O...',
  3: 'OO....',
  4: 'OO.O..',
  5: 'O..O..',
  6: 'OOO...',
  7: 'OOOO..',
  8: 'O.OO..',
  9: '.OO...',
  0: '.OOO..',
};
const braileToCharacters: BraileToCharactersMap =
  swapKeyValues(charactersToBraille);
const braileToNumbers: BraileToCharactersMap = swapKeyValues(numbersToBraille);

const convertEnglishToBraille = (englishStr: string): string => {
  let res = '';
  let isNumberSequence = false;
  for (const ch of englishStr) {
    // handle numeric characters
    if (ch >= '0' && ch <= '9') {
      if (!isNumberSequence) {
        res += numberFollows;
        isNumberSequence = true;
      }
      res += numbersToBraille[ch];
      continue;
    }

    // handle non-numeric characters
    if (ch === ' ') {
      isNumberSequence = false;
    } else if (ch === ch.toUpperCase()) {
      res += capitalFollows;
    }
    res += charactersToBraille[ch.toLowerCase()];
  }

  return res;
};

const convertBrailleToEnglish = (braileStr: string): string => {
  const BRAILE_SYMBOL_LENGTH = 6;
  console.assert(braileStr.length % BRAILE_SYMBOL_LENGTH === 0);

  let res = '';
  let isNumberSequence = false;
  let isCapital = false;
  for (let i = 0; i < braileStr.length; i += BRAILE_SYMBOL_LENGTH) {
    const symbol = braileStr.slice(i, i + BRAILE_SYMBOL_LENGTH);

    switch (symbol) {
      case numberFollows:
        isNumberSequence = true;
        break;
      case charactersToBraille[' ']:
        isNumberSequence = false;
        res += ' ';
        break;
      case capitalFollows:
        isCapital = true;
        break;
      default:
        const ch = isNumberSequence
          ? braileToNumbers[symbol]
          : braileToCharacters[symbol];

        if (isCapital) {
          res += ch.toUpperCase();
          isCapital = false;
        } else {
          res += ch;
        }
    }
  }

  return res;
};

const isBraileString = (str: string) => {
  return Array.from(str).every((ch) => ch == 'O' || ch == '.');
};

function main() {
  let res = '';
  const testInput = '42';
  if (isBraileString(testInput)) {
    res = convertBrailleToEnglish(testInput);
  } else {
    res = convertEnglishToBraille(testInput);
  }
  console.log(res);
}
main();

/*
 * TEST ASSERTIONS
 */
console.assert(isBraileString('42') == false);
console.assert(isBraileString('...OOO..O.O.1') == false);
console.assert(isBraileString('...OOO..O.O.') == true);

console.assert(convertEnglishToBraille('42') === '.O.OOOOO.O..O.O...');
console.assert(
  convertEnglishToBraille('Hello world') ===
    '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
);
console.assert(
  convertEnglishToBraille('Abc 123 xYz') ===
    '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
);

console.assert(
  convertBrailleToEnglish(
    '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'
  ) === 'Abc 123'
);
