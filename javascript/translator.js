const brailleSymbols = {
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
  capital_follows: ".....O",
  number_follows: ".O.OOO",
  space: "......",
};

// Function to translate English text to Braille
const translateToBraille = (input) => {
  let result = "";
  let numberMode = false;

  for (const char of input) {
    if (char === " ") {
      result += brailleSymbols.space;
      numberMode = false;
    } else if (!numberMode && /\d/.test(char)) {
      result += brailleSymbols.number_follows + brailleSymbols[char];
      numberMode = true;
    } else if (/[A-Z]/.test(char)) {
      result +=
        brailleSymbols.capital_follows + brailleSymbols[char.toLowerCase()];
    } else {
      result += brailleSymbols[char];
    }
  }
  return result;
};

// Function to translate Braille to English text
const translateToEnglish = (braille) => {
  let result = "";
  let capitalizeNext = false;
  let numberMode = false;
  const brailleSymbolsArray = Object.keys(brailleSymbols);
  const brailleSymbolsArrayWithoutNumbers = brailleSymbolsArray.slice(10);
  const symbols = braille
    .trim()
    .split(/(.{6})/)
    .filter(Boolean);

  for (const symbol of symbols) {
    if (symbol === brailleSymbols.space) {
      result += " ";
      numberMode = false;
    } else if (symbol === brailleSymbols.capital_follows) {
      capitalizeNext = true;
    } else if (symbol === brailleSymbols.number_follows) {
      numberMode = true;
    } else {
      if (numberMode) {
        let char = brailleSymbolsArray.find(
          (key) => brailleSymbols[key] === symbol
        );
        result += char;
      } else {
        let char = brailleSymbolsArrayWithoutNumbers.find(
          (key) => brailleSymbols[key] === symbol
        );
        result += capitalizeNext && char ? char.toUpperCase() : char;
      }
      capitalizeNext = false;
    }
  }
  return result;
};

// Function to check if input is Braille
const isBraille = (input) => {
  // Check if input is a multiple of 6 and contains only 'O' and '.' characters
  const cleanInput = input.trim();
  return /^[O.]+$/.test(cleanInput) && cleanInput.length % 6 === 0;
};

// Function to call the appropriate translation function based on input
const translate = (input) => {
  if (isBraille(input)) {
    return translateToEnglish(input);
  } else {
    return translateToBraille(input);
  }
};

// Main function to handle input and output
const main = () => {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log("Please provide input to translate.");
    process.exit(1);
  }
  const input = args.join(" ");
  const output = translate(input);
  console.log(output);
};

main();
