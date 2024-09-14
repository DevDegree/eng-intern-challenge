/**
 * 1. Check if space
 * 2. Check if number
 * 3. Check letter case
 */

import { isNumber } from "./booleans";
import { letters, numbers, utilityMap } from "./objects";
import { Braille } from "./types";

function translateCharacter(
  char: string,
  isNumberSequence: boolean
): {
  output: Braille | `${Braille}${Braille}`;
  isNumberSequence: boolean;
} {
  if (char == " ") {
    return { output: utilityMap.space, isNumberSequence: false };
  }

  if (isNumber(char)) {
    if (isNumberSequence) {
      return { output: numbers[char], isNumberSequence: true };
    }

    return {
      output: `${utilityMap.number}${numbers[char]}`,
      isNumberSequence: true,
    };
  }

  if (char.toUpperCase() == char) {
    return {
      output: `${utilityMap.capitalize}${letters[char.toLowerCase()]}`,
      isNumberSequence: false,
    };
  }

  return { output: letters[char], isNumberSequence: false };
}

export default function englishTranslator(input: string) {
  let output = "";
  let isNumberSequence = false;
  for (let char of input) {
    let result = translateCharacter(char, isNumberSequence);
    output += result.output;
    isNumberSequence = result.isNumberSequence;
  }
  return output
}
