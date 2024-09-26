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
  capital: '.....O',
  number: '.O.OOO',
  ' ': '......',
};

const charType = {
  Lower: 'Lower',
  Upper: 'Upper',
  Num: 'Num',
  Space: 'Space',
  Special: 'Special',
};

const checkCharType = str => {
  if (str.match(/[a-z]/)) {
    return charType.Lower;
  } else if (str.match(/[A-Z]/)) {
    return charType.Upper;
  } else if (str.match(/[0-9]/)) {
    return charType.Num;
  } else if (str.match(/[ ]/)) {
    return charType.Space;
  } else {
    return charType.Special;
  }
};

const isBraille = str => {
  return str.match(/[O.]/);
};

const getKeyByValue = (value, isNumber) => {
  if (isNumber) {
    return Object.keys(brailleMap).find(key => brailleMap[key] === value && !isNaN(key));
  } else {
    return Object.keys(brailleMap).find(key => brailleMap[key] === value && isNaN(parseInt(key)));
  }
};

const translateToEnglish = str => {
  let isCapital = false;
  let isNumber = false;

  let result = '';

  for (let i = 0; i < str.length; i += 6) {
    let temp = getKeyByValue(str.substr(i, 6), isNumber);
    if (temp.length === 1) {
      if (temp === ' ') {
        isNumber = false;
        result += temp;
        continue;
      }
      if (isCapital) {
        result += temp.toUpperCase();
        isCapital = false;
      } else {
        result += temp;
      }
    } else {
      if (temp === 'capital') {
        isCapital = true;
      } else if (temp === 'number') {
        isNumber = true;
      }
    }
  }

  return result;
};

const translateToBraille = str => {
  let result = '';
  let isNumber = false;

  for (let s of str) {
    const type = checkCharType(s);
    switch (type) {
      case charType.Lower:
        result += brailleMap[s];
        break;
      case charType.Upper:
        result += brailleMap['capital'];
        result += brailleMap[s.toLowerCase()];
        break;
      case charType.Num:
        if (!isNumber) {
          isNumber = true;
          result += brailleMap.number;
        }
        result += brailleMap[parseInt(s)];
        break;
      case charType.Space:
        result += brailleMap[' '];
        isNumber = false;
        break;
    }
  }

  return result;
};

const main = input => {
  if (isBraille(input)) {
    console.log(translateToEnglish(input));
  } else {
    console.log(translateToBraille(input));
  }
};

const testArgument = process.argv[2] + ' ' + process.argv[3] + ' ' + process.argv[4];
main(testArgument);
