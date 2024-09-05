const userInput = process.argv.slice(2).join(" "); // Get the command line input

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
  Capital: ".....O",
  Decimal: ".O...O",
  Number: ".O.OOO",
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

const splitBraillesArr = [];
const translatedArr = [];

function translateToBraille(input) {
  let isNumberMode = false; // Use to track if loop is in "Number" mode

  if (input.includes(".")) {
    // If input is in Braille, split into 6-character strings and add to splitBrailleArr
    for (let i = 0; i < input.length; i += 6) {
      splitBraillesArr.push(input.substring(i, i + 6));
    }
    // Loop over the splitBrailleArr and find matching key in brailleMap
    splitBraillesArr.forEach((braille, index) => {
      if (braille === brailleMap.Number) {
        // If the braille value is for "Number", enable number mode
        isNumberMode = true;
      } else if (braille === brailleMap[" "]) {
        // If the braille value is for empty space, disable number mode
        isNumberMode = false;
        translatedArr.push(" ");
      } else {
        // Translate based on the current mode (number or alphabet)
        for (let [key, value] of Object.entries(brailleMap)) {
          if (braille === value) {
            if (braille === brailleMap.Capital) {
              // Handle capitalization
              break; // Move to the next character
            }

            if (isNumberMode && !isNaN(key)) {
              // If loop is in number mode and the key is a number
              translatedArr.push(key);
              break;
            } else if (!isNumberMode && isNaN(key)) {
              // If loop is not in number mode and the key is a letter or symbol
              if (splitBraillesArr[index - 1] === brailleMap.Capital) {
                // If the braille in the previous index is a Capital, convert current braille into uppercase
                translatedArr.push(key.toUpperCase());
              } else {
                translatedArr.push(key); // Otherwise keep it as lowercase alphabet
              }
              break;
            }
          }
        }
      }
    });
  } else {
    // If input is a string of alphabets, split string into Alphabet Array
    const splitAlphabetArr = input.split("");
    // Loop over Alphabet Array and find matching braille value in brailleMap
    splitAlphabetArr.forEach((alphabet, index) => {
      if (!isNaN(parseInt(alphabet))) {
        // If character is a number, enable number mode
        if (!isNumberMode) {
          // Only push the Number symbol when entering number mode
          isNumberMode = true;
          translatedArr.push(brailleMap.Number);
        }
        translatedArr.push(brailleMap[alphabet]);
        return;
      }

      if (alphabet === " ") {
        // If character is an empty space, disable number mode
        isNumberMode = false;
        translatedArr.push(brailleMap[" "]); // Push braille value of " "
        return; // Continue to next character
      }

      if (
        isNaN(parseInt(alphabet)) &&
        alphabet.trim() == alphabet.toUpperCase()
      ) {
        // If character is an uppercase, push "Capital" symbol into Translation Array
        // Exclude empty space and numbers
        translatedArr.push(brailleMap.Capital); // Push braille value of "Capital"

        translatedArr.push(brailleMap[alphabet.toLowerCase()]); // Convert uppercase character into lowercase to match the key in brailleMap object

        return; // Continue to next character
      }

      // Handle Lowercase Letters and Symbols
      translatedArr.push(brailleMap[alphabet.toLowerCase()]);
    });
  }
  return translatedArr.join(""); // Return translated array as string
}

const result = translateToBraille(userInput);
console.log(result);
return result;
