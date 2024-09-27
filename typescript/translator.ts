class Translator {
  /**
   * Map of braille to english
   */
  private static brailleToEnglish: Record<string, string> = {
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

  /**
   * Map of english to braille
   */
  private static englishToBraille: Record<string, string> = {
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

  /**
   * Map of special characters to braille
   */
  private static specialToBraille: Record<string, string> = {
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
    capital: ".....O",
    number: ".O.OOO",
    space: "......",
  };

  /**
   *
   */
  private static brailleToSpecial: Record<string, string> = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
  };

  /**
   * Map of braille to numbers
   */
  private static brailleToNumber: Record<string, string> = {
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

  /**
   * Map of numbers to braille
   */
  private static numberToBraille: Record<string, string> = {
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

  /**
   * Translates english text to braille and returns the braille translation
   *
   * @param {string} englishText english text to be translated to braille
   * @returns {string} braille translation of the english text
   */
  private static toBraille(englishText: string): string {
    let brailleText = "";
    let isNumber = false;

    const capital = this.specialToBraille["capital"];
    const number = this.specialToBraille["number"];

    for (let i = 0; i < englishText.length; ++i) {
      const char = englishText[i];

      // Check if character is a lowercase letter lexicographically
      if (char >= "a" && char <= "z") {
        if (isNumber) {
          isNumber = false; // Reset number flag when encountering a letter
        }

        brailleText += this.englishToBraille[char];
      }
      // Check if character is an uppercase letter lexicographically
      else if (char >= "A" && char <= "Z") {
        brailleText += capital;
        brailleText += this.englishToBraille[char.toLowerCase()];
      }
      // Check if character is a number lexicographically
      else if (char >= "0" && char <= "9") {
        if (!isNumber) {
          brailleText += number;
          isNumber = true; // Set number flag
        }

        brailleText += this.numberToBraille[char];
      } else {
        brailleText += this.specialToBraille[char];
      }
    }

    return brailleText;
  }

  /**
   * Translates braille text to english and returns the english translation
   *
   * Ends execution with exit code 1 if the braille text is invalid
   *
   * @param {string} brailleText braille text to be translated to english
   * @returns {string} english translation of the braille text
   */
  private static toEnglish(brailleText: string): string {
    // According to the braille standard, each braille character is 6 characters long
    if (brailleText.length % 6 !== 0) {
      console.error("Error: Invalid braille text.");
      process.exit(1);
    }

    let englishText = "";
    let isCapital = false;
    let isNumber = false;

    const capital = this.specialToBraille["capital"];
    const number = this.specialToBraille["number"];
    const space = this.specialToBraille[" "];

    for (let i = 0; i < brailleText.length; i += 6) {
      // Extract the current braille character
      const brailleChar = brailleText.slice(i, i + 6);

      if (brailleChar === capital) {
        isCapital = true;
        continue;
      }

      if (brailleChar === number) {
        isNumber = true;
        continue;
      }

      if (brailleChar === space) {
        englishText += " ";
        isNumber = false;
        continue;
      }

      if (isNumber) {
        const num = this.brailleToNumber[brailleChar];

        if (num) {
          englishText += num;
        } else {
          console.error("Error: Invalid braille number.");
          process.exit(1);
        }
      } else {
        let letter = this.brailleToEnglish[brailleChar];

        if (letter) {
          if (isCapital) {
            letter = letter.toUpperCase();
            isCapital = false;
          }

          englishText += letter;
        } else {
          const specialChar = this.brailleToSpecial[brailleChar];

          if (specialChar) {
            englishText += specialChar;
          } else {
            console.error("Error: Invalid braille special character.");
            process.exit(1);
          }
        }
      }
    }
    return englishText;
  }

  /**
   * Translates the input text to braille if it is in English, or to English if it is in braille
   * and prints the result to stdout
   *
   * @param {string[]} args command-line arguments
   */
  public static translate(args: string[]) {
    const concatenatedArgs = args.join(" ");

    // test braille text constraints
    const isBraille = args.length === 1 && /^[\.O]+$/.test(concatenatedArgs);

    if (isBraille) {
      return Translator.toEnglish(concatenatedArgs);
    }
    return Translator.toBraille(concatenatedArgs);
  }
}

function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error("Error: No input specified.");
    process.exit(1);
  }

  const translation = Translator.translate(args);

  console.log(translation);
}

main();
