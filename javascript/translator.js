const brailleAlphabet = {
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
  " ": "......",
  "#": ".O.OOO", // Number follows
  "^": ".....O", // Capital follows
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
};

const englishAlphabet = Object.fromEntries(
  Object.entries(brailleAlphabet).map(([k, v]) => [v, k])
);

function isBraille(input) {
  return /^[O.]+$/.test(input);
}

function englishToBraille(text) {
  let braille = "";
  let numberMode = false;

  for (let char of text) {
    if (/[A-Z]/.test(char)) {
      if (numberMode) {
        braille += brailleAlphabet["^"];
        numberMode = false;
      }
      braille += brailleAlphabet["^"] + brailleAlphabet[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      if (!numberMode) {
        braille += brailleAlphabet["#"];
        numberMode = true;
      }
      braille += brailleAlphabet[char];
    } else {
      if (numberMode) {
        numberMode = false;
      }
      braille += brailleAlphabet[char.toLowerCase()] || "";
    }
  }
  return braille;
}

function brailleToEnglish(braille) {
  let english = "";
  let i = 0;
  let capitalNext = false;
  let numberMode = false;

  while (i < braille.length) {
    const symbol = braille.slice(i, i + 6);
    if (symbol === brailleAlphabet["^"]) {
      capitalNext = true;
    } else if (symbol === brailleAlphabet["#"]) {
      numberMode = true;
    } else {
      let char = englishAlphabet[symbol] || "";
      if (capitalNext) {
        char = char.toUpperCase();
        capitalNext = false;
      } else if (numberMode) {
        char = "0123456789"["abcdefghij".indexOf(char)] || char;
      }
      english += char;
      if (char === " ") numberMode = false;
    }
    i += 6;
  }
  return english;
}

function main() {
  const input = process.argv.slice(2).join(" ");
  if (isBraille(input)) {
    console.log(brailleToEnglish(input));
  } else {
    console.log(englishToBraille(input));
  }
}

main();
