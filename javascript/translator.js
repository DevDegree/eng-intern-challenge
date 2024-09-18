// Consolidated map for both letters and numbers
const brailleMap = {
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
};

//convert to array, swap key and value, convert back to object
const brailleToEnglishMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);

// activate number mode
const numberPrefix = ".O.OOO";
//activates uppercase mode
const uppercasePrefix = ".....O";

function translate(input) {
  const isBraille = input
    .split("")
    .every((char) => char === "O" || char === ".");

  if (isBraille) {
    // BRAILLE TO ENGLISH
    let result = "";
    let isNumber = false;
    let isNextUppercase = false;

    //move in chunks of 6 for braille grid
    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.slice(i, i + 6);
      if (brailleChar === numberPrefix) {
        // If we hit number prefix, set number mode
        isNumber = true;
        continue;
      }
      if (brailleChar === uppercasePrefix) {
        // If we hit uppercase prefix, set the next char to uppercase
        isNextUppercase = true;
        continue;
      }

      let char = brailleToEnglishMap[brailleChar] || "";

      if (isNumber) {
        // If number mode, try to convert to a number
        char = Number.isInteger(parseInt(char)) ? char : "";
        // Only exit number mode if we encounter a space
        if (char === " ") {
          isNumber = false;
        }
      } else if (isNextUppercase) {
        // If uppercase mode, convert the character to uppercase
        char = char.toUpperCase();
        isNextUppercase = false; // Reset the uppercase flag after using it
      }
      result += char;
    }
    return result;
  } else {
    // ENGLISH TO BRAILLE
    let result = "";
    let isNumber = false;
    for (let i = 0; i < input.length; i++) {
      const char = input[i];

      if (/[0-9]/.test(char)) {
        // If the character is a number
        if (!isNumber) {
          // If we're not already in number mode, add the number prefix
          result += numberPrefix;
          isNumber = true;
        }
        // Add the Braille version of the number
        result += brailleMap[char] || "";
      } else {
        // If the character is not a number
        if (isNumber) {
          // If we're exiting number mode
          isNumber = false;
        }

        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
          // If it's an uppercase letter
          result += uppercasePrefix;
        }

        result += brailleMap[char.toLowerCase()] || "";
      }
    }
    return result;
  }
}

// Get input from command line arguments
const args = process.argv.slice(2);
const input = args.join(" "); // Join all arguments into a single string
if (!input) {
  // If no input is provided, show an error and exit
  console.error("Please provide an input string as a command line argument.");
  process.exit(1);
}

// Translate the input and print the result
console.log(translate(input));
