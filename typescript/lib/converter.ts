import readline from "readline";
import { alphabet, brailleRegex, symbols, numbers } from "../mappings";
import { splash, loader, showSpinner } from "../config";

class Converter {

  public run(input: string): string {
    const isBraille = this.isBraille(input);
    return isBraille
      ? this.decodeBraille(input)
      : this.encodeBraille(input);
  };

  public startup() {
    console.clear();
    console.log(splash);

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    rl.question('\x1b[2m Enter your string: ', async (input: string) => {
      const spinnerInt = showSpinner();
      await loader();
      clearInterval(spinnerInt);

      let conversion: string;
      const isBraille = this.isBraille(input);

      conversion = isBraille
        ? this.decodeBraille(input)
        : this.encodeBraille(input);

      console.log(`\n`);
      console.log(`\x1b[0m ${conversion}`);
      console.log(`\n`);

      rl.close();
    });
  };

  private isBraille(input: string): boolean {
    const formattedInput = input.replace(/\s+/g, '');
    return brailleRegex.test(formattedInput) && formattedInput.length % 6 === 0;
  };

  private encodeBraille(input: string): string {
    let braille = '';
    let isNumber = false;

    for (const char of input) {
      switch (true) {
        case char === ' ':
          braille += alphabet[char] || '';
          isNumber = false;
          break;

        case /^[A-Z]$/.test(char):
          braille += symbols.capital;
          braille += alphabet[char.toLowerCase()] || '';
          isNumber = false;
          break;

        case /^[0-9]$/.test(char):
          if (!isNumber) {
            braille += symbols.number;
            isNumber = true;
          }
          braille += numbers[char] || '';
          break;

        case /^[a-z]$/.test(char):
          braille += alphabet[char] || '';
          isNumber = false;
          break;

        default:
          console.error(`Unsupported character: ${char}`);
          break;
      }
    }

    return braille;
  };

  private decodeBraille(braille: string) {
    let text = '';
    let isNumber = false;
    let isCapital = false;

    const chars = braille.match(/.{1,6}/g) || [];

    for (const char of chars) {
      switch(true) {
        case char === symbols.number:
          isNumber = true;
          break;

        case char === symbols.capital:
          isCapital = true;
          break;

        case isNumber:
          const number = Object.keys(numbers).find(key => numbers[key] === char);
          if (number) {
            text += number;
          }
          isNumber = false;
          break;

        default:
          const specialSymbol = Object.keys(symbols).find(key => symbols[key] === char);
          if (specialSymbol) {
            text += specialSymbol;
          } else {
            const letter = Object.keys(alphabet).find(key => alphabet[key] === char);
            if (letter) {
              text += isCapital ? letter.toUpperCase() : letter;
            }
          }
          isCapital = false;
          break;
      }
    }

    return text;
  };
};

export default new Converter();
