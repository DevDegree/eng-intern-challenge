const E2B = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "(": "O.O..O",
  ")": ".O.OO.",
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

const B2E = {
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
  "......": " ",
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
};

const B2E_digits = {
  ".OOO..": "0",
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
};

const capital_follows = ".....O";
const number_follows = ".O.OOO";
const space = "......";

function convertEnglishToBraille(input) {
  let ans = "";

  for (let i = 0; i < input.length; i++) {
    if (input[i] >= "A" && input[i] <= "Z") {
      ans += capital_follows; // Add capital follows
      ans += E2B[input[i].toLowerCase()]; // Converts Upercase to Braile
    } else if (input[i] >= "0" && input[i] <= "9") {
      ans += number_follows; // Add number follows

      while (i < input.length && input[i] !== " ") {
        ans += E2B[input[i]]; //Converts Digits to Braile
        i++;
      }
      if (i < input.length) {
        ans += E2B[" "]; // Add Space if numbers ended
      }
    } else {
      ans += E2B[input[i]]; // Converts Lowercase to Braile
    }
  }

  return ans;
}

function convertBrailleToEnglish(input) {
  let ans = "";

  for (let i = 0; i < input.length; i += 6) {
    let current = input.slice(i, i + 6); // Reads BLocks of 6

    if (current === capital_follows) {
      i += 6;
      ans += B2E[input.slice(i, i + 6)].toUpperCase(); // Converts Braile to Uppercase
    } else if (current === number_follows) {
      i += 6;
      while (i < input.length && input.slice(i, i + 6) !== space) {
        ans += B2E_digits[input.slice(i, i + 6)]; // Converts Braile to Digits
        i += 6;
      }
      if (i < input.length) {
        ans += " ";
      }
    } else {
      ans += B2E[current]; // Converts Braile to Lowercase
    }
  }

  return ans;
}

// Read command line arguments
const args = process.argv.slice(2);

// Combine input arguments
const input = args.join(" ");

let isBraille = true;
if (input.length % 6 !== 0) {
  //if input it not divisible by, it cannot be braile
  isBraille = false;
}
for (let char of input) {
  if (char !== "O" && char !== ".") {
    // if any character is present other than 0 or . it is not Braile
    isBraille = false;
    break;
  }
}

if (isBraille) {
  console.log(convertBrailleToEnglish(input));
} else {
  console.log(convertEnglishToBraille(input));
}
