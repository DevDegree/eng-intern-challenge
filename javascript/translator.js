const toBrailleAlphabet = {
  "a": "O.....",
  "b": "O.O...",
  "c": "OO....",
  "d": "OO.O..",
  "e": "O..O..",
  "f": "OOO...",
  "g": "OOOO..",
  "h": "O.OO..",
  "i": ".OO...",
  "j": ".OOO..",
  "k": "O...O.",
  "l": "O.O.O.",
  "m": "OO..O.",
  "n": "OO.OO.",
  "o": "O..OO.",
  "p": "OOO.O.",
  "q": "OOOOO.",
  "r": "O.OOO.",
  "s": ".OO.O.",
  "t": ".OOOO.",
  "u": "O...OO",
  "v": "O.O.OO",
  "w": ".OOO.O",
  "x": "OO..OO",
  "y": "OO.OOO",
  "z": "O..OOO",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": ".OO..O",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
  "capital": ".....O",
  "number": ".O.OOO",

};

const toBrailleNumbers = {
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
  ".": ".O...O",
};

const toEnglishAlphabet = Object.fromEntries(
  Object.entries(toBrailleAlphabet).map(([key, value]) => [value, key])
);

const toEnglishNumbers = Object.fromEntries(
  Object.entries(toBrailleNumbers).map(([key, value]) => [value, key])
);

const englishBrailleTranslator = (input) => {
  const confirmBraille = (text) => {
    return ![...text].some(char => char !== 'O' && char !== '.');
  }
  const braille = confirmBraille(input);
  let output = "";
  let numbers = false;
  
  if (!braille) {
    for (let i = 0; i < input.length; i++) {
      // Check if the character is a capital letter
      if (input[i] >= 'A' && input[i] <= 'Z') {
        output += toBrailleAlphabet.capital + toBrailleAlphabet[input[i].toLowerCase()];
        // Check if the character is a number but not the first of a line of numbers
      } else if (input[i - 1] >= '0' && input[i - 1] <= '9' && input[i] >= '0' && input[i] <= '9') {
        output += toBrailleNumbers[input[i]];
        // Check if the character is a number and the first of a line of numbers
      } else if (input[i] >= '0' && input[i] <= '9') {
        output += toBrailleAlphabet.number + toBrailleNumbers[input[i]];
        // Check if the character is a period and is surrounded by numbers
      } else if (input[i] === "." && input[i - 1] >= '0' && input[i - 1] <= '9' && input[i + 1] >= '0' && input[i + 1] <= '9') {
        output += toBrailleNumbers["."];
      } else {
        output += toBrailleAlphabet[input[i]];
      };
    };
  } else {
    let i = 0;
    while (i < input.length) {
      // Break up code into 6 character chunks
      const brailleChar = input.slice(i, i + 6);
      const nextBrailleChar = input.slice(i, i + 6);
      const lastBrailleChar = input.slice(i - 6, i);
      // Check if the character is a number
      if (brailleChar === toBrailleAlphabet.number) {
        numbers = true;
        i += 6;
        continue;
      }
      if (numbers) {
        // While number is true, change to false when space value is found
        if (brailleChar === toBrailleAlphabet[' ']) {
          output += " ";
          i += 6;
          numbers = false;
        } else {
          // If not space, use Numbers list to decode
          const numberChar = Object.keys(toBrailleNumbers).find(key => toBrailleNumbers[key] === brailleChar);
          if (numberChar) {
            output += numberChar;
          }
          i += 6;
        }
        continue;
      }
      // Check if the character is a capital indicator and move to next letter
      if (brailleChar === toBrailleAlphabet.capital) {
        i += 6;
        // set next letter
        const nextBrailleChar = input.slice(i, i + 6);
        // Add capital indicator and uppercase letter
        output += toEnglishAlphabet[nextBrailleChar].toUpperCase();
        i += 6;
        continue;
        // Check if the character is a decimal
      } else if (brailleChar === toEnglishNumbers["."] && lastBrailleChar >= '0' && lastBrailleChar <= '9' && nextBrailleChar >= '0' && nextBrailleChar <= '9') {
        output += ".";
        i += 6;
      } else {
        output += toEnglishAlphabet[brailleChar];
        i += 6;
      }
    }
  }
  return output;
};

const input = process.argv.slice(2).join(" "); // Combine arguments into a single string
const output = englishBrailleTranslator(input);
console.log(output);