type BrailleMap = { [key: string]: string };

const englishToBrailleMap: BrailleMap = {
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

const numberToBrailleMap: BrailleMap = {
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
};

const capitalIndicator = ".....O";
const numberIndicator = ".O.OOO";

function englishToBraille(input: string): string {
  let result = "";
  let numberMode = false;

  for (const char of input) {
    if (char === " ") {
      result += englishToBrailleMap[" "];
      numberMode = false;
    } else if (char >= "A" && char <= "Z") {
      result += capitalIndicator + englishToBrailleMap[char.toLowerCase()];
      numberMode = false;
    } else if (char >= "0" && char <= "9") {
      if (!numberMode) {
        result += numberIndicator;
        numberMode = true;
      }
      result += numberToBrailleMap[char];
    } else {
      result += englishToBrailleMap[char];
      numberMode = false;
    }
  }

  return result;
}

const input = process.argv.slice(2).join(" ");
console.log(englishToBraille(input));
