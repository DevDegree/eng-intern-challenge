import process from "process";

const ENGLISH_TO_BRAILLE: Record<string, string> = Object.freeze({
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.O",
  "!": "..O.",
  ":": "..O..",
  ";": "..O.O.",
  "-": "....O",
  "/": ".O..O.",
  "<": ".O..O",
  ">": "O..O.",
  "(": "O.O..O",
  ")": ".O.O.",
  " ": "......",
});

const DIGIT_TO_BRAILLE: Record<string, string> = Object.freeze({
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
});

const BRAILLE_TO_ENGLISH: Record<string, string> = Object.freeze(
  Object.fromEntries(Object.entries(ENGLISH_TO_BRAILLE).map(([k, v]) => [v, k]))
);

const BRAILLE_TO_DIGIT: Record<string, string> = Object.freeze(
  Object.fromEntries(Object.entries(DIGIT_TO_BRAILLE).map(([k, v]) => [v, k]))
);

const CAPITAL_FOLLOWS = ".....O";
const DECIMAL_FOLLOWS = ".O...O";
const NUMBER_FOLLOWS = ".O.OOO";
const BRAILLE_SPACE = "......";

const isBraille = (input: string): boolean => {
  return input.length % 6 === 0 && /^[O.]+$/.test(input);
};

const isDigit = (char: string): boolean => {
  return /[0-9]/.test(char);
};

const isUppercaseLetter = (char: string): boolean => {
  return /[A-Z]/.test(char);
};

const englishToBraille = (input: string): string => {
  const outputArray: string[] = [];
  const inputArray: string[] = input.split("");

  let currIndex = 0;
  while (currIndex < inputArray.length) {
    const char = inputArray[currIndex];

    if (isDigit(char)) {
      outputArray.push(NUMBER_FOLLOWS + DIGIT_TO_BRAILLE[char]);
      currIndex++;

      // add digits to output until space character is found
      while (
        currIndex < inputArray.length &&
        inputArray[currIndex] !== " " &&
        isDigit(inputArray[currIndex])
      ) {
        outputArray.push(DIGIT_TO_BRAILLE[inputArray[currIndex]]);
        currIndex++;
      }
    } else if (isUppercaseLetter(char)) {
      // add capital letter indicator
      outputArray.push(
        CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.toLowerCase()]
      );
      currIndex++;
    } else {
      outputArray.push(ENGLISH_TO_BRAILLE[char]);
      currIndex++;
    }
  }

  return outputArray.join("");
};

const brailleToEnglish = (input: string): string => {
  const outputArray: string[] = [];
  const inputArray: string[] = input.match(/.{1,6}/g) as string[];

  let currIndex = 0;
  while (currIndex < inputArray.length) {
    const symbol = inputArray[currIndex];

    // parse capital letter
    if (symbol === CAPITAL_FOLLOWS && currIndex + 1 < inputArray.length) {
      outputArray.push(
        BRAILLE_TO_ENGLISH[inputArray[currIndex + 1]].toUpperCase()
      );
      currIndex += 2;
    } else if (symbol === NUMBER_FOLLOWS) {
      currIndex++;

      // add digits to output until space symbol is found
      while (
        currIndex < inputArray.length &&
        inputArray[currIndex] !== BRAILLE_SPACE
      ) {
        outputArray.push(BRAILLE_TO_DIGIT[inputArray[currIndex]]);
        currIndex++;
      }
    } else {
      outputArray.push(BRAILLE_TO_ENGLISH[symbol]);
      currIndex++;
    }
  }

  return outputArray.join("");
};

const translate = (input: string): string => {
  if (!input) {
    return "";
  }

  return isBraille(input) ? brailleToEnglish(input) : englishToBraille(input);
};

const main = () => {
  const input = process.argv.slice(2).join(" ");
  const output = translate(input);

  console.log(output);
};

main();
