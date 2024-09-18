const englishToBrailleLookUp: Record<string, string> = {
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
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const brailleToAlphabetLookUp: Record<string, string> = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const NUMBER_FOLLOWS = ".O.OOO";
const CAPITAL_FOLLOWS = ".....O";
const DECIMAL_FOLLOWS = ".O...O";
const SPACE = "......";

const brailleToNumbersLookUp: Record<string, string> = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const translateToEnglish = (inputStr: string) => {
  const chunks: string[] = inputStr.match(/.{1,6}/g) || [];

  let numberFlag = false;

  const englishCharacters: string[] = [];
  for (let i = 0; i < chunks.length; i++) {
    const chunk = chunks[i];
    if (chunk === DECIMAL_FOLLOWS) {
      englishCharacters.push(".");
      continue;
    }

    if (chunk === NUMBER_FOLLOWS) {
      numberFlag = true;
      continue;
    }
    if (chunk === SPACE) {
      numberFlag = false;
      englishCharacters.push(" ");
      continue;
    }

    if (chunk === CAPITAL_FOLLOWS) {
      const nextChunk: string = chunks[i + 1];
      const englishChar: string =
        brailleToAlphabetLookUp[nextChunk].toUpperCase();
      englishCharacters.push(englishChar);
      i = i + 1;
      continue;
    }

    const englishChar: string = numberFlag
      ? brailleToNumbersLookUp[chunk]
      : brailleToAlphabetLookUp[chunk];
    englishCharacters.push(englishChar);
  }

  const translatedString = englishCharacters.join("");

  return translatedString;
};

const translateToBraille = (inputStr: string) => {
  let numberFlag = false;
  let brailleCharacters: string[] = [];

  for (let i = 0; i < inputStr.length; i++) {
    let char = inputStr[i];

    let flagString = "";

    if (isNaN(parseInt(char)) && char.toUpperCase() === char && char !== " ") {
      flagString = CAPITAL_FOLLOWS;
      char = char.toLowerCase();
    }
    if (!isNaN(parseInt(char)) && !numberFlag) {
      flagString = NUMBER_FOLLOWS;
      numberFlag = true;
    }

    if (char === ".") {
      const nextChar = inputStr[i + 1];
      if (!isNaN(parseInt(nextChar))) {
        flagString = DECIMAL_FOLLOWS;
      }
    }

    if (char === " ") {
      numberFlag = false;
    }

    const brailleString = englishToBrailleLookUp[char];

    brailleCharacters.push(flagString);
    brailleCharacters.push(brailleString);
  }

  return brailleCharacters.join("");
};

const translate = (inputStr: string) => {
  //Unauthentic Braille has not been included in the tests - for example -> strings like "OOOOOO". Since they are neither English nor Braille, the tool must show the user a prompt stating possible unauthentic Braille use 
  let isBraille = !/[^.O]+/.test(inputStr) && inputStr.length % 6 === 0;

  const translation = isBraille
    ? translateToEnglish(inputStr)
    : translateToBraille(inputStr);
  return translation;
};

const main = () => {
  const args = process.argv.slice(2);
  const inputStr = args.join(" ");

  const translation = translate(inputStr);
  console.log(translation);
};

main();
