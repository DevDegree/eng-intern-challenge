import { ENGLISH_TO_BRAILLE, NUMBER_TO_BRAILLE } from "./legends";

function isUppercaseCharacter(character: string) {
  return /^[A-Z]$/.test(character);
}

function isNumericCharacter(character: string) {
  return /^[0-9]$/.test(character);
}

export function translateEnglishToBraille(englishString: string) {
  let translation = "";
  let numberMode = false;

  for (let idx = 0; idx < englishString.length; idx += 1) {
    const character = englishString[idx];

    if (isUppercaseCharacter(character)) {
      translation += ENGLISH_TO_BRAILLE["capitalPrefix"];
      translation += ENGLISH_TO_BRAILLE[character.toLowerCase()];
      continue;
    }

    if (isNumericCharacter(character)) {
      if (!numberMode) {
        numberMode = true;
        translation += ENGLISH_TO_BRAILLE["numberPrefix"];
      }

      translation += NUMBER_TO_BRAILLE[Number(character)];
      continue;
    }

    if (character === " ") numberMode = false;

    translation += ENGLISH_TO_BRAILLE[character];
  }

  return translation;
}
