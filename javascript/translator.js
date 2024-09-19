// Braille mappings
const alphaToBraille = {
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
};

const numsToBraille = {
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

const specialBraille = {
  capital: '.....O',
  number: '.O.OOO',
  space: '......',
};

const brailleToAlpha = Object.fromEntries(
  Object.entries(alphaToBraille).map(([k, v]) => [v, k])
);

const brailleToNum = Object.fromEntries(
  Object.entries(numsToBraille).map(([k, v]) => [v, k])
);

function translateBraille(brailleText) {
  let isNumber = false;
  let isCapital = false;
  const brailleArray = [];
  for (let i = 0; i < brailleText.length; i += 6)
    brailleArray.push(brailleText.slice(i, i + 6));
  let result = '';
  for (let i = 0; i < brailleArray.length; i++) {
    let token = brailleArray[i];

    // check for special characters
    if (specialBraille.space === token) {
      result += ' ';
      isNumber = false;
      continue;
    } else if (specialBraille.number === token) {
      isNumber = true;
      continue;
    } else if (specialBraille.capital === token) {
      isCapital = true;
      isNumber = false;
      continue;
    }

    if (isNumber) {
      result += brailleToNum[token];
    } else {
      if (isCapital) {
        isCapital = false;
        result += brailleToAlpha[token].toUpperCase();
      } else {
        result += brailleToAlpha[token];
      }
    }
  }
  return result;
}

// Function to convert English text to Braille
function translateAlphaNum(string) {
  let result = '';
  let isNumber = false;

  for (let i = 0; i < string.length; i++) {
    const char = string[i];

    if (char === ' ') {
      result += specialBraille.space;
      isNumber = false;
      continue;
    }

    if (char >= '0' && char <= '9') {
      if (!isNumber) {
        result += specialBraille.number; // Add number marker if we enter number mode
        isNumber = true;
      }
      result += numsToBraille[char];
      continue;
    }

    // Handle letters
    if (char >= 'A' && char <= 'Z') {
      result += specialBraille.capital;
      result += alphaToBraille[char.toLowerCase()];
      isNumber = false;
    } else if (char >= 'a' && char <= 'z') {
      result += alphaToBraille[char];
      isNumber = false;
    }
  }

  return result;
}

function containsOnlyDotsAndOs(str) {
  const regex = /^[\.O]+$/;
  return regex.test(str);
}

const input = process.argv.slice(2);

if (input.length === 1) {
  if (containsOnlyDotsAndOs(input[0]));
  console.log(translateBraille(input[0]));
} else {
  console.log(translateAlphaNum(input.join(' ')));
}
