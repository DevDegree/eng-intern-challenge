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

const BRAILLE_ALPHABETS_CAPS = ".....O";
const BRAILLE_NUMBER = ".O.OOO";
const ENGLISH_NUMBERS: Record<string, string> = {
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

const ENGLISH_ALPHABET: Record<string, string> = Object.keys(
  BRAILLE_ALPHABET
).reduce((a, c) => {
  a[BRAILLE_ALPHABET[c]] = c;
  return a;
}, {} as Record<string, string>);

const ENGLISH_NUMBERS_REVERSED: Record<string, string> = Object.keys(
  ENGLISH_NUMBERS
).reduce((a, c) => {
  a[ENGLISH_NUMBERS[c]] = c;
  return a;
}, {} as Record<string, string>);

class Translator {
  private input: string;

  constructor(input: string) {
    this.input = input;
  }

  private isBraille(): boolean {
    return /^[O.]+$/.test(this.input);
  }

  private englishToBraille(): string {
    let result = "";
    let isNumber = false;

    for (const char of this.input) {
      if (char.match(/[A-Z]/)) {
        result += BRAILLE_ALPHABETS_CAPS + BRAILLE_ALPHABET[char.toLowerCase()];
      } else if (char.match(/[0-9]/)) {
        if (!isNumber) {
          result += BRAILLE_NUMBER;
          isNumber = true;
        }
        result += ENGLISH_NUMBERS[char];
      } else if (char === " ") {
        isNumber = false;
        result += BRAILLE_ALPHABET[char];
      } else {
        isNumber = false;
        result += BRAILLE_ALPHABET[char];
      }
    }

    return result;
  }

  private brailleToEnglish(): string {
    let result = "";
    let isCapital = false;
    let isNumber = false;
    const symbols = this.input.match(/.{6}/g) || [];

    for (const symbol of symbols) {
      if (symbol === BRAILLE_ALPHABETS_CAPS) {
        isCapital = true;
        continue;
      } else if (symbol === BRAILLE_NUMBER) {
        isNumber = true;
        continue;
      } else if (ENGLISH_ALPHABET[symbol]) {
        const letter = ENGLISH_ALPHABET[symbol];
        if (isCapital) {
          result += letter.toUpperCase();
          isCapital = false;
        } else {
          result += letter;
        }
      } else if (ENGLISH_NUMBERS_REVERSED[symbol] && isNumber) {
        result += ENGLISH_NUMBERS_REVERSED[symbol];
      } else {
        result += ENGLISH_ALPHABET[symbol] || " ";
      }
    }

    return result;
  }
  public translate(): string {
    if (this.isBraille()) {
      return this.brailleToEnglish();
    } else {
      return this.englishToBraille();
    }
  }
}
function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("Usage: ts-node translator.ts <string_to_translate>");
    process.exit(1);
  }

  const input = args.join(" ");
  const translator = new Translator(input);
  console.log(translator.translate());
}

main();
