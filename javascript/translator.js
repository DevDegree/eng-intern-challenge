const {
  braille_alphabet_dict,
  braille_num_dict,
  braille_symbols_dict,
  braille_precursor_dict,
} = require("./constants");
const {
  isBrailleCheck,
  splitEverySixChars,
  getValueFromDict,
  getKeyFromDict,
  isSymbolInDict,
} = require("./utils");

const arg = process.argv.slice(2);

// First, check if the input is Braille or English
const isBraille = isBrailleCheck(arg);

/**
 * This is the main function for the command-line application that translates Braille to English and vice versa.
 * @returns {string} - Returns the translated string in Braille or English
 */
function translate() {
  let output = "";
  let numberMode = false;
  let capitalMode = false;

  if (isBraille) {
    // Translate Braille to English
    const english_translation_array = [];

    // Split into chunks of 6 characters
    const braille_array = splitEverySixChars(arg[0]);

    for (let braille of braille_array) {
      // 1. When in numberMode, use the braille_num_dict until a space is encountered
      if (numberMode) {
        const number = getValueFromDict(braille, braille_num_dict);
        if (number) {
          english_translation_array.push(number);
          continue;
        }
        numberMode = false;
      }

      // 2. When in capitalMode, convert the letter to uppercase
      if (capitalMode) {
        const letter = getValueFromDict(braille, braille_alphabet_dict);
        if (letter) {
          english_translation_array.push(letter.toUpperCase());
        }
        capitalMode = false;
        continue;
      }

      //   3. Check if it is a precursor
      const isPrecursor = getValueFromDict(braille, braille_precursor_dict);
      if (isPrecursor) {
        switch (isPrecursor) {
          case "capital follows":
            capitalMode = true;
            continue;
          case "number follows":
            numberMode = true;
            continue;
          case "space":
            english_translation_array.push(" ");
            numberMode = false;
            capitalMode = false;
            break;
        }
      } else {
        const isAlphabet = getValueFromDict(braille, braille_alphabet_dict);
        const isSymbol = getValueFromDict(braille, braille_symbols_dict);

        // There is a bug here where o and > can be confused
        if (isAlphabet) {
          // 4. Translate Alphabet
          english_translation_array.push(isAlphabet);
        } else if (isSymbol) {
          // 5. Translate Symbol
          english_translation_array.push(isSymbol);
        }
      }
    }

    output = english_translation_array.join("");

    return output;
  } else {
    // Translate English to Braille
    const braille_translation_array = [];
    const english_array = arg;

    for (let word of english_array) {
      const wordArray = word.split("");
      for (let character of wordArray) {
        // 1. Handle numbers
        if (!isNaN(parseInt(character))) {
          // Only include "number follows" once until a space is encountered
          !numberMode &&
            braille_translation_array.push(
              getKeyFromDict("number follows", braille_precursor_dict)
            );
          numberMode = true;

          numberMode &&
            braille_translation_array.push(
              getKeyFromDict(character, braille_num_dict)
            );
        } else if (isSymbolInDict(character)) {
          // 2. Handle symbols
          const symbol = getKeyFromDict(character, braille_symbols_dict);
          if (symbol) {
            braille_translation_array.push(symbol);
          }
        } else if (character === character.toUpperCase()) {
          // 3. Handle capital letters
          braille_translation_array.push(
            getKeyFromDict("capital follows", braille_precursor_dict)
          );
          braille_translation_array.push(
            getKeyFromDict(character.toLowerCase(), braille_alphabet_dict)
          );
        } else {
          // 4. Handle lowercase letters
          getKeyFromDict(character, braille_alphabet_dict) &&
            braille_translation_array.push(
              getKeyFromDict(character, braille_alphabet_dict)
            );
        }
      }
      numberMode = false;
      //   5. Add a space after every word
      braille_translation_array.push(
        getKeyFromDict("space", braille_precursor_dict)
      );
    }
    // 6. Remove the space at the end of the sentence
    output = braille_translation_array.slice(0, -1).join("");
    return output;
  }
}

const translatedText = translate();
console.log(translatedText);
