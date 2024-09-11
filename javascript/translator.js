const BRAILLE_MAP = [
  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
  ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
  ["u", "v", "x", "y", "z", "w"],
  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
  [".", ",", ";", ":", "!", "?", '"', "(", ")", "/"],
  ["+", "=", "*", "-", "#", "'", "cap", " "],
];

const BRAILLE_PATTERNS = [
  ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."],
  ["O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO."],
  ["O...OO", "O.O.OO", "OO..OO", "OO.OOO", "O..OOO", ".OOO.O"],

  ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."],

  [".O.O..", "O.....", "O.O...", "OO....", "OOO...", ".OOO.O", "..OO.O", "OO.O..", ".O.O.O", "OO..O."],
  ["O.O.O.", ".OO.O.", "O..OO.", "O...OO", ".O.OOO", ".O..O.", ".....O", "......"],
];

const NUMBER_SIGN = BRAILLE_PATTERNS[5][4];
const CAPITAL_SIGN = BRAILLE_PATTERNS[5][6];

function isDigit(char) {
  return /[0-9]/.test(char);
}

function isUpperCase(char) {
  return /[A-Z]/.test(char);
}

function isLetter(char) {
  return /[a-z]/i.test(char);
}

function isLetterAToJ(char) {
  return /[a-j]/.test(char);
}

function charToBraille(char) {
  for (let i = 0; i < BRAILLE_MAP.length; i++) {
    let index = BRAILLE_MAP[i].indexOf(char);

    if (index !== -1) {
      return BRAILLE_PATTERNS[i][index];
    }
  }

  return char;
}

function brailleToChar(pattern) {
  for (let i = 0; i < BRAILLE_PATTERNS.length; i++) {
    let index = BRAILLE_PATTERNS[i].indexOf(pattern);

    if (index !== -1) {
      return BRAILLE_MAP[i][index];
    }
  }

  return pattern;
}

function letterToNumber(char) {
  return String(BRAILLE_MAP[0].indexOf(char.toLowerCase()));
}

function toBraille(text) {
  let braille = "";
  let isNumber = false;

  for (let char of text) {
    if (isDigit(char) && !isNumber) {
      braille += NUMBER_SIGN;
      isNumber = true;
    } else if (!isDigit(char)) {
      isNumber = false;
    }

    if (isUpperCase(char)) {
      braille += CAPITAL_SIGN;
      char = char.toLowerCase();
    }

    braille += charToBraille(char);
  }

  return braille;
}

function toText(braille) {
  let text = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < braille.length; i += 6) {
    const pattern = braille.slice(i, i + 6);

    if (pattern === CAPITAL_SIGN) {
      isCapital = true;
      continue;
    }

    if (pattern === NUMBER_SIGN) {
      isNumber = true;
      continue;
    }

    let char = brailleToChar(pattern);

    if (isCapital && isLetter(char)) {
      char = char.toUpperCase();
      isCapital = false;
    }

    if (isNumber && isLetterAToJ(char)) {
      char = letterToNumber(char);
    } else {
      isNumber = false;
    }

    text += char;
  }

  return text;
}

function main() {
  const args = process.argv.slice(2);
  const input = args.join(" ");

  if (/^[O\.]+$/.test(input)) {
    console.log(toText(input));
  } else {
    console.log(toBraille(input));
  }
}

main();
