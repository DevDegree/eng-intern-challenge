type BrailleMap = { [key: string]: string };

const lettersToBraille: BrailleMap = {
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
};

const numbersToBraille: BrailleMap = {
  "0": ".OOO..",
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
};

const brailleToLetters: BrailleMap = Object.fromEntries(
  Object.entries(lettersToBraille).map(([key, value]) => [value, key])
);

const brailleToNumbers: BrailleMap = Object.fromEntries(
  Object.entries(numbersToBraille).map(([key, value]) => [value, key])
);

const capitalSign = ".....O";
const numberSign = ".O.OOO";

const isBraille = (input: string): boolean =>
  input.split("").every((char) => char === "O" || char === ".");

const translateToBraille = (input: string): string => {
  let result = "";
  let isNumber = false;

  for (const char of input) {
    const lowerChar = char.toLowerCase();

    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += numberSign;
        isNumber = true;
      }
      result += numbersToBraille[char];
    } else {
      isNumber = false;
      if (char !== lowerChar) result += capitalSign;
      result += lettersToBraille[lowerChar] || "";
    }
  }

  return result;
};

const translateToEnglish = (input: string): string => {
  let result = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < input.length; i += 6) {
    const brailleChar = input.slice(i, i + 6);

    if (brailleChar === capitalSign) {
      isCapital = true;
    } else if (brailleChar === numberSign) {
      isNumber = true;
    } else if (isNumber) {
      const char = brailleToNumbers[brailleChar];
      if (char) {
        result += char;
      } else {
        isNumber = false;
      }
    } else {
      const char = brailleToLetters[brailleChar];
      if (char) {
        result += isCapital ? char.toUpperCase() : char;
        isCapital = false;
      }
    }
  }

  return result;
};

const translate = (input: string): string =>
  isBraille(input) ? translateToEnglish(input) : translateToBraille(input);

const main = () => {
  const input = process.argv.slice(2).join(" ");
  console.log(translate(input));
};

main();
