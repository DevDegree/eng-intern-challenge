//-------✨ Braille Mapping✨--------//
const BRAILLE_MAP = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".O.O..",
  j: ".OO...",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".O..O.",
  t: ".OO.O.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO..",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  " ": "......",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".O.O..",
  0: ".OO...",
};

//-------✨ Marks for Capitalization and Numbers✨--------//
const CAPITALIZATION_MARK = ".....O";
const NUMBER_MARK = ".O.OOO";

//-------✨ English Mapping from Braille✨--------//
const ENGLISH_MAP = Object.fromEntries(
  Object.entries(BRAILLE_MAP).map(([k, v]) => [v, k])
);

//-------✨ Main Translation Function✨--------//
function translate(input) {
  if (/^[O.]+$/.test(input)) {
    return translateBraille(input);
  } else {
    return translateEnglish(input);
  }
}

//-------✨ English to Braille Translation✨--------//
function translateEnglish(english) {
  let result = "";
  let inNumberSequence = false,
    inUpperCase = false;

  for (const char of english) {
    if (char >= "0" && char <= "9") {
      if (!inNumberSequence) {
        result += NUMBER_MARK;
        inNumberSequence = true;
      }
    } else if (char >= "A" && char <= "Z") {
      if (!inUpperCase) {
        result += CAPITALIZATION_MARK;
        inUpperCase = true;
      }
    } else {
      inUpperCase = false;
      inNumberSequence = false;
    }
    result += BRAILLE_MAP[char.toLowerCase()] || "";
  }

  return result;
}

//-------✨ Braille to English Translation✨--------//
function translateBraille(braille) {
  let result = "";
  let isNumber = false;

  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.substring(i, i + 6);
    if (symbol === NUMBER_MARK) {
      isNumber = true;
      continue;
    }

    const char = ENGLISH_MAP[symbol] || "";

    if (isNumber && char) {
      result += char;
    } else if (char) {
      if (
        char.toUpperCase() === char &&
        i > 0 &&
        braille.substring(i - 6, i).includes(CAPITALIZATION_MARK)
      ) {
        result += char.toUpperCase();
      } else {
        result += char.toLowerCase();
      }
      isNumber = false;
    }
  }

  return result;
}

//-------✨ Input Handling and Execution✨--------//
const input = process.argv.slice(2).join(" ");
console.log(translate(input));
