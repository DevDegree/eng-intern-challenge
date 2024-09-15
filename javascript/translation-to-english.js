import {
  BRAILLE_TO_ENGLISH_MAPPINGS,
  BRAILLE_TO_NUMBERS_MAPPINGS,
  BRAILLE_TO_PUNCTUATION_MAPPINGS,
  CAPITAL_FOLLOWS_CASE,
  DECIMAL_FOLLOWS_CASE,
  NUMBER_FOLLOWS_CASE,
  SPACE_CASE,
} from "./translator-mappings.js";

let current_text_index = 0;
const LENGTH_OF_BRAILLE_CHAR = 6;

function translateBrailleTextToNumber(brailleText) {
  let translateToNumberArray = [];

  for (let i = 0; i < brailleText.length; i = i + LENGTH_OF_BRAILLE_CHAR) {
    const brailleChar = brailleText.substring(i, i + LENGTH_OF_BRAILLE_CHAR);

    if (!BRAILLE_TO_NUMBERS_MAPPINGS.has(brailleChar)) {
      break;
    }

    translateToNumberArray.push(BRAILLE_TO_NUMBERS_MAPPINGS.get(brailleChar));

    current_text_index += LENGTH_OF_BRAILLE_CHAR;
  }

  return translateToNumberArray.join("");
}

function translateToEnglishChar(brailleChar, brailleText) {
  if (brailleChar === SPACE_CASE) {
    return " ";
  }

  if (brailleChar === CAPITAL_FOLLOWS_CASE) {
    const characterToBeCapitalized = BRAILLE_TO_ENGLISH_MAPPINGS.get(brailleText.substring(0, LENGTH_OF_BRAILLE_CHAR));
    current_text_index += LENGTH_OF_BRAILLE_CHAR;

    return characterToBeCapitalized?.toUpperCase();
  }

  if (brailleChar === NUMBER_FOLLOWS_CASE) {
    return translateBrailleTextToNumber(brailleText);
  }

  if (BRAILLE_TO_PUNCTUATION_MAPPINGS.has(brailleChar)) {
    return BRAILLE_TO_PUNCTUATION_MAPPINGS.get(brailleChar);
  }

  return BRAILLE_TO_ENGLISH_MAPPINGS.get(brailleChar);
}

export default function translateToEnglish(brailleText) {
  let translateToEnglishArray = [];

  while (current_text_index < brailleText.length) {
    const brailleChar = brailleText.substring(current_text_index, current_text_index + LENGTH_OF_BRAILLE_CHAR);

    translateToEnglishArray.push(
      translateToEnglishChar(brailleChar, brailleText.slice(current_text_index + LENGTH_OF_BRAILLE_CHAR)
      )
    );

    current_text_index += LENGTH_OF_BRAILLE_CHAR;
  }

  return translateToEnglishArray.join("");
}
