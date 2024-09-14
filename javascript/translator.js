//create map for standard char to braille representation
const charToBraille = {
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
  cap: '.....O',
  dec: '.O...O',
  num: '.O.OOO',
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  ':': '..OO..',
  ';': '..O.O.',
  '-': '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.',
  ' ': '......',
};

numToBraille = {
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

let brailleToChar = Object.fromEntries(
  Object.entries(charToBraille).map(([char, braille]) => [braille, char])
);

let brailleToNum = Object.fromEntries(
  Object.entries(numToBraille).map(([char, braille]) => [braille, char])
);

let inputString = process.argv.slice(2).join(' ');

const translate = (str) => {
  let isBraille = undefined;
  let result = [];
  let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
  //Parse if input string is braille or char string
  for (let char of str) {
    if (char !== '.' && char !== 'O') {
      isBraille = false;
      break;
    } else {
      isBraille = true;
    }
  }

  //translate from english to braille
  if (!isBraille) {
    let prevCharNum = false;
    for (let char of str) {
      if (numbers.includes(parseInt(char))) {
        if (!prevCharNum) {
          result.push(charToBraille['num'] + numToBraille[char]);
          prevCharNum = true;
        } else {
          result.push(numToBraille[char]);
        }
      }

      if (char === '.' && prevCharNum) {
        result.push(charToBraille[dec] + charToBraille[char]);
      }

      if (char == char.toLowerCase()) {
        result.push(charToBraille[char]);
        prevCharNum = false;
      } else {
        result.push(charToBraille['cap'] + charToBraille[char.toLowerCase()]);
        prevCharNum = false;
      }
    }
  }

  //translate from braille to english
  else {
    let isCap = false;
    let isNum = false;

    let chunkedString = [];
    let index = 0;
    while (index < str.length) {
      chunkedString.push(str.slice(index, index + 6));
      index += 6;
    }

    for (let brailleChar of chunkedString) {
      if (brailleChar === charToBraille['num']) {
        isNum = true;
        continue;
      }

      if (isNum && brailleToNum[brailleChar]) {
        result.push(brailleToNum[brailleChar]);
        continue;
      }

      if (brailleChar === '......') {
        result.push(brailleToChar[brailleChar]);
        isNum = false;
        continue;
      }

      if (brailleChar === charToBraille['cap']) {
        isCap = true;
        isNum = false;
        continue;
      }

      let char = brailleToChar[brailleChar];
      if (isCap) {
        char = char.toUpperCase();
        isCap = false;
        isNum = false;
      }

      result.push(char);
    }
  }

  return result.join('');
};

console.log(translate(inputString));
