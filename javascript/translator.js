const BrailleDictionary = {
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
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

const reverseMapping = (map) => {
  const reversed = {};
  Object.keys(map).forEach((key) => {
    reversed[map[key]] = key;
  });
  return reversed;
};

const translateEnglishToBraille = (input) => {
  let result = "";
  let isNumberMode = false;

  for (const char of input) {
    if (/[A-Z]/.test(char)) {
      result +=
        BrailleDictionary.capital + BrailleDictionary[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      if (!isNumberMode) {
        result += BrailleDictionary.number;
        isNumberMode = true;
      }
      result += BrailleDictionary[char];
    } else if (char === " ") {
      result += BrailleDictionary.space;
      isNumberMode = false;
    } else {
      result += BrailleDictionary[char];
      isNumberMode = false;
    }
  }

  return result;
};

const translateBrailleToEnglish = (input) => {
  const brailleChunks = input.match(/.{1,6}/g);
  let result = "";
  let isCapital = false;
  let isNumber = false;
  const reversedDict = reverseMapping(BrailleDictionary);

  for (const chunk of brailleChunks) {
    if (chunk === BrailleDictionary.capital) {
      isCapital = true;
    } else if (chunk === BrailleDictionary.number) {
      isNumber = true;
    } else if (chunk === BrailleDictionary.space) {
      result += " ";
      isNumber = false;
    } else {
      let char = reversedDict[chunk];
      if (isCapital) {
        char = char.toUpperCase();
        isCapital = false;
      }
      result += char;
      isNumber = false;
    }
  }

  return result;
};

const detectType = (input) => (/^[O.]+$/.test(input) ? "braille" : "english");

const translate = (input) => {
  const type = detectType(input);
  return type === "english"
    ? translateEnglishToBraille(input)
    : translateBrailleToEnglish(input);
};

const inputString = process.argv.slice(2).join(" ");
console.log(translate(inputString));
