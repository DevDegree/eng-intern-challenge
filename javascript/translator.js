const brailleMap = {
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
  ' ': '......',
  caps: '.....O',
  num: '.O.OOO',
};

function Braille(str) {
  const isBraille = /^[O.\s]+$/.test(str);

  if (isBraille) {
    return BrailleToAlphabet(str);
  } else {
    return AlphabetToBraille(str);
  }
}

function BrailleToAlphabet(str) {
  let result = '';
  let isCaps = false;
  let isNumber = false;

  const sanitizedString = str.replace(/ /g, '');
  const length = sanitizedString.length - 1;

  for (let i = 0; i <= length; i = i + 6) {
    const sub = sanitizedString.slice(i, i + 6);

    const value = getKeyByValue(brailleMap, sub, isNumber);

    if (value === 'num') {
      isNumber = true;
    } else if (value === 'caps') {
      isCaps = true;
    } else if (isCaps) {
      result = result + value?.toUpperCase();
      isCaps = false;
    } else if (isNumber && value == ' ') {
      isNumber = false;
      result = result + value;
    } else {
      result = result + value;
    }
  }

  return result;
}

function AlphabetToBraille(str) {
  let result = '';
  let isNumber = false;

  for (let chr of str) {
    if (chr === ' ') {
      result = result + brailleMap[' '];
      isNumber = false;
      continue;
    }

    const isString = isNaN(Number(chr));

    if (isString && chr === chr.toUpperCase()) {
      result = result + brailleMap['caps'] + brailleMap[chr.toLowerCase()];
    } else if (!isString && !isNumber) {
      result = result + brailleMap['num'] + brailleMap[chr];
      isNumber = true;
    } else if (!isString && isNumber) {
      result = result + brailleMap[chr];
    } else {
      result = result + brailleMap[chr.toLowerCase()];
    }
  }

  return result;
}

function getKeyByValue(object, value, numFlag) {
  let result;

  const matches = Object.keys(object).filter((key) => object[key] === value);

  if (!numFlag) {
    matches.forEach((match) => {
      if (isNaN(parseFloat(match))) {
        result = match;
      }
    });
  } else {
    result = Object.keys(object).find((key) => object[key] === value);
  }

  return result;
}

const args = process.argv.slice(2);
const input = args.join(' ');

const translation = Braille(input);
console.log(translation);
