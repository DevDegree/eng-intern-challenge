// note about braille:
// O = raised dot
// . = flat (empty) space

type Dictionary = Record<string, string>;

const romanToBraille: Dictionary = {
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
};

const englishToBraille: Dictionary = {
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

const CONTROL_SEQUENCE = {
  CAPITAL_FOLLOWS: ".....O",
  NUMBER_FOLLOWS: ".O.OOO",
} as const;

const reverseKeyValueMapping = (obj: Dictionary): Dictionary =>
  Object.fromEntries(Object.entries(obj).map(([key, value]) => [value, key]));

const isEnglishText = (text: string) => /^[a-zA-Z\d\s]+$/.test(text);
const isInt = (char: string) => /^\d$/.test(char);

const convertEnglishToBraille = (text: string) => {
  let output = "";
  let isNumber = false;

  for (let char of text) {
    if (char === " ") {
      isNumber = false;
    } else if (isInt(char)) {
      // only add the control sequence before the first number in the block
      if (!isNumber) {
        output += CONTROL_SEQUENCE.NUMBER_FOLLOWS;
        isNumber = true;
      }
    } else if (char === char.toUpperCase()) {
      output += CONTROL_SEQUENCE.CAPITAL_FOLLOWS;
      char = char.toLowerCase(); // as we only have lowercase braille
    }

    output += isNumber ? romanToBraille[char] : englishToBraille[char];
  }

  return output;
};

const convertBrailleToEnglish = (brailleText: string) => {
  const letters = brailleText.match(/.{6}/g) ?? [];
  const brailleToEnglish = reverseKeyValueMapping(englishToBraille);
  const brailleToRoman = reverseKeyValueMapping(romanToBraille);

  let output = "";
  let isUpperCase = false;
  let isNumber = false;

  for (const letter of letters) {
    if (letter === CONTROL_SEQUENCE.CAPITAL_FOLLOWS) {
      isUpperCase = true;
      continue;
    }
    if (letter === CONTROL_SEQUENCE.NUMBER_FOLLOWS) {
      isNumber = true;
      continue;
    }

    isNumber = letter === englishToBraille[" "] ? false : isNumber;

    if (isUpperCase) {
      output += brailleToEnglish[letter].toUpperCase();
    } else if (isNumber) {
      output += brailleToRoman[letter];
    } else {
      output += brailleToEnglish[letter];
    }

    isUpperCase = false;
  }

  return output;
};

const getArgumentFromCmd = () => process.argv.slice(2).join(" ");

const main = () => {
  let argument = getArgumentFromCmd();
  if (!argument) return;

  const output = isEnglishText(argument)
    ? convertEnglishToBraille(argument)
    : convertBrailleToEnglish(argument);

  console.log(output);
};

main();
