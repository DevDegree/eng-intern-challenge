/* Get command line arguments */
const args: string[] = process.argv.slice(2);

//
// Constants
//

const charFromBraille: Record<string, string> = {
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
};

const numFromBraille: Record<string, string> = {
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

const charToBraille: Record<string, string> = {
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
};

const numToBraille: Record<string, string> = {
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

const space: string = "......";
const capitalFollows: string = ".....O";
const numberFollows: string = ".O.OOO";

//
// Helper functions
//

function isBraille(str: string): boolean {
  // Check input uses only 'O' and '.'
  const strSet: Set<string> = new Set(str);
  if (strSet.size !== 2 || !strSet.has("O") || !strSet.has(".")) {
    return false;
  }

  // Check input is multiple of 6
  if (str.length % 6 !== 0) {
    return false;
  }

  return true;
}

function parseBraille(str: string): string {
  const chars: string[] = str.match(/.{1,6}/g);
  let output: string = "";

  let capitalFlag: boolean = false;
  let numberFlag: boolean = false;

  for (let char of chars) {
    switch (char) {
      case space:
        output += " ";
        numberFlag = false;
        break;

      case capitalFollows:
        capitalFlag = true;
        break;

      case numberFollows:
        numberFlag = true;
        break;

      default:
        if (numberFlag) {
          output += numFromBraille[char];
        } else {
          if (capitalFlag) {
            output += charFromBraille[char].toUpperCase();
            capitalFlag = false;
          } else {
            output += charFromBraille[char];
          }
        }
    }
  }

  return output;
}

function parseEnglish(str: string): string {
  let output: string = "";

  let numberFlag: boolean = false;

  for (let i = 0; i < str.length; i++) {
    const char: string = str[i];

    if (char === " ") {
      output += space;
      numberFlag = false;
    } else if (char >= "0" && char <= "9") {
      // Number case

      // Toggle number flag if false
      if (!numberFlag) {
        output += numberFollows;
        numberFlag = true;
      }

      output += numToBraille[char];
    } else if (char >= "A" && char <= "Z") {
      // Uppercase case
      if (numberFlag) {
        output += space;
        numberFlag = false;
      }

      output += capitalFollows;
      output += charToBraille[char.toLowerCase()];
    } else if (char >= "a" && char <= "z") {
      // Lowercase case
      if (numberFlag) {
        output += space;
        numberFlag = false;
      }

      output += charToBraille[char];
    } else {
      // Invalid case
      output = `Encountered invalid character : ${str}`;
    }
  }

  return output;
}

//
// Main code
//

function main() {
  const input: string = args.join(" ");
  let output: string = "";

  if (isBraille(input)) {
    output = parseBraille(input);
  } else {
    output = parseEnglish(input);
  }

  console.log(output);
}

main();
