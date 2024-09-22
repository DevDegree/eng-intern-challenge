// let's create a braille mapping for the translator to use

//  mapping of the braille characters to the English alphabet
const brailleMap: { [key: string]: string } = {
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
  // mapping of capital and number indicators
  CAPITAL: ".....O",
  NUMBER: "..OO..",
  // mapping of numbers
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

// let's detect if the input is braille
function isBraille(input: string): boolean {
  return /^[O.]+$/.test(input);
}

// let's create a function to convert english to braille
function englishToBraille(input: string): string {
  let braille = "";
  let inNumber = false;

  for (let i = 0; i < input.length; i++) {
    const char = input[i];
    if (char === " ") {
      braille += brailleMap[" "];
      inNumber = false;
      continue;
    }

    if (/\d/.test(char)) {
      if (!inNumber) {
        braille += brailleMap["NUMBER"];
        inNumber = true;
      }
      braille += brailleMap[char];
      continue;
    } else {
      if (inNumber) {
        inNumber = false;
      }
    }

    if (/[A-Z]/.test(char)) {
      braille += brailleMap["CAPITAL"];
      braille += brailleMap[char.toLowerCase()];
    } else if (/[a-z]/.test(char)) {
      braille += brailleMap[char];
    } else {
      // Handle unsupported characters if necessary
    }
  }

  return braille;
}



// driver application
function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("No input provided.");
    process.exit(1);
  }

  const input = args.join(" ");

  let output: string;

  if (isBraille(input)) {
    // output = brailleToEnglish(input);
  } else {
    output = englishToBraille(input);
  }

//   console.log(output);
}

main();
