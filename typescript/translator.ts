const brailleAlphabetMap = {
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
  cap: ".....O",
  number: ".O.OOO",
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
  " ": "......",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O.O",
  ")": ".O.OO.",
};

const enum charDetected {
  upperCase = "upperCase",
  number = "number",
  space = "space",
}

const charDetection = (c: string): string => {
  let charType = "";
  if (/[0-9]/.test(c)) charType = "number";
  if (/[A-Z]/.test(c)) charType = "upperCase";
  if (/[ ]/.test(c)) charType = "space";
  return charType;
};

const translateToBraille = (input: string) => {
  let isNumberMode = false;

  return input
    .split("")
    .map((c) => {
      const detectedChar = charDetection(c);
      switch (detectedChar) {
        case charDetected.upperCase:
          return brailleAlphabetMap["cap"] + brailleAlphabetMap[c.toLowerCase()];

        case charDetected.number:
          if (!isNumberMode) {
            isNumberMode = true;
            return brailleAlphabetMap["number"] + brailleAlphabetMap[c];
          }
          return brailleAlphabetMap[c];

        case charDetected.space:
          if (isNumberMode) {
            isNumberMode = false;
          }
          return brailleAlphabetMap[" "];
        default:
          return brailleAlphabetMap[c];
      }
    })
    .join("");
};
const translateToEnglish = (input: string) => {
  const alphabetToBrailleMap = Object.fromEntries(
    Object.entries(brailleAlphabetMap)
      .filter(([key]) => /[a-z]/.test(key))
      .map(([key, value]) => [value, key]),
  );

  const numberToBrailleMap = Object.fromEntries(
    Object.entries(brailleAlphabetMap)
      .filter(([key]) => /[0-9]/.test(key))
      .map(([key, value]) => [value, key]),
  );

  const specialCharToBrailleMap = Object.fromEntries(
    Object.entries(brailleAlphabetMap)
      .filter(([key]) => !/[a-z0-9]/.test(key))
      .map(([key, value]) => [value, key]),
  );

  const output: string[] = [];
  let isNumberMode = false;
  let isCapital = false;

  for (let i = 0; i < input.length; i += 6) {
    const braille =
      input[i] + input[i + 1] + input[i + 2] + input[i + 3] + input[i + 4] + input[i + 5];

    switch (true) {
      case isCapital:
        isCapital = false;
        output.push(alphabetToBrailleMap[braille].toUpperCase());
        break;
      case isNumberMode:
        output.push(numberToBrailleMap[braille]);
        break;
      case braille === brailleAlphabetMap["cap"]:
        isCapital = true;
        break;
      case braille === brailleAlphabetMap["number"]:
        isNumberMode = true;
        break;
      default:
        const char = alphabetToBrailleMap[braille] || specialCharToBrailleMap[braille];
        char && output.push(char);
    }
  }
  return output.join("");
};
console.log(
  translateToEnglish(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."),
);
function translator(input: string): string {}
