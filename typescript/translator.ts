const BRAILLE_ALPHABET: Record<string, string> = {
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

const BRAILLE_NUMBERS: Record<string, string> = {
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  O: ".OOO..",
};

const BRAILLE_CAPITAL_FOLLOWS = ".....O";
const BRAILLE_NUMBER_FOLLOWS = ".O.OOO";

function isBraille(text: string): boolean {
  return /^[.0\s]+$/.test(text);
}

function englishToBraille(text: string): string {
  let translatedText = "";
  let inNumberMode = false;

  for (const char of text) {
    if (char >= "A" && char <= "Z") {
      // Capital letters
      translatedText +=
        BRAILLE_CAPITAL_FOLLOWS + BRAILLE_ALPHABET[char.toLowerCase()];
    } else if (char >= "a" && char <= "z") {
      // Lowercase letters
      translatedText += BRAILLE_ALPHABET[char];
    } else if (char >= "0" && char <= "9") {
      // Numbers
      if (!inNumberMode) {
        translatedText += BRAILLE_NUMBER_FOLLOWS;
        inNumberMode = true;
      }
      translatedText += BRAILLE_NUMBERS[char];
    } else if (char === " ") {
      translatedText += BRAILLE_ALPHABET[" "];
      inNumberMode = false;
    } else {
      throw new Error(`Unknown character: ${char}`);
    }
  }
  return translatedText;
}

function brailleToEnglish(braille: string): string {
  let translatedText = "";
  let index = 0;
  let inNumberMode = false;

  while (index < braille.length) {
    const letter = braille.slice(index, index + 6);

    if (letter === BRAILLE_CAPITAL_FOLLOWS) {
      // next letter is capital
      const nextLetter = braille.slice(index + 6, index + 12);
      for (const [key, value] of Object.entries(BRAILLE_ALPHABET)) {
        if (value === nextLetter) {
          translatedText += key.toUpperCase();
          break;
        }
      }
      index += 12; // move past capital follows and the capital letter
    } else if (letter === BRAILLE_NUMBER_FOLLOWS) {
      inNumberMode = true;
      index += 6;
    } else if (letter === BRAILLE_ALPHABET[" "]) {
      translatedText += " ";
      inNumberMode = false;
      index += 6;
    } else {
      if (inNumberMode) {
        for (const [num, brailleNum] of Object.entries(BRAILLE_NUMBERS)) {
          if (brailleNum === letter) {
            translatedText += num;
            break;
          }
        }
      } else {
        for (const [letter, brailleLetter] of Object.entries(
          BRAILLE_ALPHABET
        )) {
          if (brailleLetter === letter) {
            translatedText += letter;
            break;
          }
        }
      }
      index += 6;
    }
  }

  return translatedText;
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.error("Usage: node translator.js <text>");
    process.exit(1);
  }

  const text = args.join(" ");
  const translatedText = isBraille(text)
    ? brailleToEnglish(text)
    : englishToBraille(text);

  console.log(translatedText);
}

main();
