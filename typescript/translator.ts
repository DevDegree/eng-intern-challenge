// TODO: Add docstring + class description
class BrailleTranslator {
  private isCapitalMode: boolean = false;
  private isNumberMode: boolean = false;

  constructor(
    private brailleAlphabet: { [key: string]: string },
    private brailleNumbers: { [key: string]: string },
    private brailleSpecials: { [key: string]: string },
    private brailleCommands: { [key: string]: string }
  ) {}

  // TODO: Add docstring + function description
  public englishToBraille(input: string): string {
    let braille = "";
    this.isNumberMode = false;

    for (const char of input) {
      braille += this.translateCharToBraille(char);
    }

    this.isNumberMode = false;
    return braille;
  }

  private translateCharToBraille(char: string): string {
    // Check for space + track end of numeric sequence, if applicable
    if (char === " ") {
      this.isNumberMode = false;
      return this.brailleCommands["space"];
    }

    // Check for numerical digits
    if (/^[0-9]$/.test(char)) {
      return this.translateDigit(char);
    }

    // Check for uppercase/lowercase alphabets
    if (/^[a-zA-Z]$/.test(char)) {
      return this.translateAlphabet(char);
    }

    // Check for special characters
    if (char in this.brailleSpecials) {
      return this.brailleSpecials[char];
    }

    // Char outside of Braille language
    throw new Error(
      `Character "${char}" is not supported in Braille translation.`
    );
  }

  private translateDigit(char: string): string {
    let braille: string = "";

    if (!this.isNumberMode) {
      this.isNumberMode = true;
      braille += this.brailleCommands["number"];
    }

    braille += this.brailleNumbers[char];
    return braille;
  }

  private translateAlphabet(char: string): string {
    let braille = "";

    if (char === char.toUpperCase()) {
      braille += this.brailleCommands["capital"];
    }

    braille += this.brailleAlphabet[char.toLowerCase()];
    return braille;
  }

  // TODO: Add docstring + function description
  public brailleToEnglish(input: string): string {
    let english = "";
    this.isCapitalMode = false;
    this.isNumberMode = false;

    for (let i = 0; i < input.length; i += 6) {
      let braille = input.slice(i, i + 6);
      english += this.translateBrailleToChar(braille);
    }

    return english;
  }

  private translateBrailleToChar(braille: string): string {
    // Check for space and reset modes
    if (braille === this.brailleCommands["space"]) {
      this.isNumberMode = false;
      return " ";
    }

    // Check for capitalization command
    if (braille === this.brailleCommands["capital"]) {
      this.isCapitalMode = true;
      return "";
    }

    // Check for start of number sequence
    if (braille === this.brailleCommands["number"]) {
      this.isNumberMode = true;
      return "";
    }

    // If in number mode, translate as a digit
    if (this.isNumberMode) {
      return this.getKeyByValue(this.brailleNumbers, braille);
    }

    // Translate alphabet
    let char = this.getKeyByValue(this.brailleAlphabet, braille);
    if (char) {
      if (this.isCapitalMode) {
        this.isCapitalMode = false;
        return char.toUpperCase();
      }
      return char;
    }

    // Translate special characters
    let specChar = this.getKeyByValue(this.brailleSpecials, braille);
    if (specChar) {
      return specChar;
    }

    // Char outside of Braille language
    throw new Error(
      `Braille "${braille}" is not supported in Braille translation.`
    );
  }

  // TODO: Add docstring + function description
  private getKeyByValue(
    object: { [key: string]: string },
    value: string
  ): string {
    return Object.keys(object).find((key) => object[key] === value) || "";
  }
}

const brailleAlphabet: { [key: string]: string } = {
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

const brailleNumbers: { [key: string]: string } = {
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

const brailleCommands: { [key: string]: string } = {
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
  decimal: ".O...O",
};

const brailleSpecials: { [key: string]: string } = {
  ".": "..OO.O",
  "'": "..O...",
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
};

// TODO: Add docstring + function description
function isBraille(input: string): boolean {
  return /^[O.]{6}([O.]{6})*$/.test(input);
}

function main() {
  const args = process.argv.slice(2);
  const input = args.join(" ");

  const brailleTranslator = new BrailleTranslator(
    brailleAlphabet,
    brailleNumbers,
    brailleSpecials,
    brailleCommands
  );
  let output = isBraille(input)
    ? brailleTranslator.brailleToEnglish(input)
    : brailleTranslator.englishToBraille(input);

  console.log(output);

  // Code to convert back to original dialect to check loss of data
  // output = isBraille(input)
  //   ? brailleTranslator.englishToBraille(output)
  //   : brailleTranslator.brailleToEnglish(output);

  // console.log(output);
}

main();
