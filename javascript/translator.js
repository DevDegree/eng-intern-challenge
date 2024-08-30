const BRAILLE_MAP = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  0: "O.....", // Updated mapping
  1: "O.O...", // Updated mapping
  2: "OO....", // Updated mapping
  3: "OO.O..", // Updated mapping
  4: "O..O..", // Updated mapping
  5: "OOO...", // Updated mapping
  6: "OOOO..", // Updated mapping
  7: "O.OO..", // Updated mapping
  8: ".OO...", // Updated mapping
  9: ".OOO..", // Updated mapping
  " ": "......",
  "#": ".O.OOO",
  cap: ".....O",
  ",": "O.....",
  ";": "O.O...",
  ":": "OO....",
  ".": ".O.O..",
  "!": "OOO...",
  "?": ".OOO.O",
  "-": "O...OO",
  "/": "OO..O.",
  "(": "OO.O..",
  ")": "OO.O..",
};

const REVERSE_BRILLEMAP = Object.fromEntries(Object.entries(BRAILLE_MAP).map(([key, value]) => [value, key]));

function isLetter(char) {
  return /[A-Za-z]/.test(char);
}

function isUpperCase(char) {
  return char === char.toUpperCase();
}

function isDigit(char) {
  return /[0-9]/.test(char);
}

function toBraille(text) {
  let braille = "";
  let isPreviousNumber = false;

  for (let i = 0; i < text.length; i++) {
    const char = text[i];

    if (isLetter(char)) {
      if (isUpperCase(char)) {
        braille += BRAILLE_MAP["cap"];
      }

      isPreviousNumber = false;
    }

    if (isDigit(char)) {
      if (!isPreviousNumber) {
        braille += BRAILLE_MAP["#"];

        isPreviousNumber = true;
      }
    } else {
      isPreviousNumber = false;
    }

    braille += BRAILLE_MAP[char.toLowerCase()] || char;
  }

  return braille;
}

function toText(text) {
  // implement the reverse braille mapping
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
