import { BRAILE_SPECIAL_CHARS_MAP, BRAILLE_MAP, BRAILLE_TO_NUMBERS_MAP, ENGLISH_TO_BRAILLE_MAP } from "./constants";

const CAPFOLLOWS = '.....O';
const DECIMALFOLLOWS = '.O...O';
const NUMFOLLOWS = '.O.OOO';
const SPACE = '......';

const translateBrailleToEnglish = (braille: string): string => {
  let translated = '';
  let capitalFollows = false;
  let numberFollows = false;

  for (let i = 0; i < braille.length; i += 6) {
    const char = braille.substring(i, i + 6);

    // Check for follow characters
    if (char === CAPFOLLOWS) {
      capitalFollows = true;
      continue;
    } else if (char === NUMFOLLOWS) {
      numberFollows = true;
      continue;
    } else if (char === DECIMALFOLLOWS) {
      translated += '.';
      continue;
    }

    // Capital letter case
    if (capitalFollows) {
      translated += ENGLISH_TO_BRAILLE_MAP[char].toUpperCase();
      capitalFollows = false;
      continue;
    }

    // Number follow case
    if (numberFollows) {
      if (char === SPACE) {
        translated += ' ';
        numberFollows = false;
        continue;
      } else if (char in BRAILE_SPECIAL_CHARS_MAP) {
        translated += BRAILE_SPECIAL_CHARS_MAP[char];
      } else {
        translated += BRAILLE_TO_NUMBERS_MAP[char];
      }
      continue;
    }

    // Normal case
    if (char === SPACE) {
      translated += ' ';
    } else if (char in BRAILE_SPECIAL_CHARS_MAP) {
      translated += BRAILE_SPECIAL_CHARS_MAP[char];
    } else {
      translated += BRAILLE_MAP[char];
    }
  }

  return translated;
};

const translateEnglishToBraille = (english: string): string => {
  let translated = '';
  let numberFollows = false;

  for (let i = 0; i < english.length; i++) {
    const char = english[i];
    
    if (char >= '0' && char <= '9') {
      if (!numberFollows) {
        translated += NUMFOLLOWS;
        numberFollows = true;
      }
      translated += ENGLISH_TO_BRAILLE_MAP[char];
    } else if (char.trim() === '') {
      translated += SPACE;
      numberFollows = false; 
    } else if (char === '.') {
      translated += DECIMALFOLLOWS;
    } else if (char.match(/[A-Z]/)) { 
      if (numberFollows) {
        translated += SPACE;
        numberFollows = false; 
      }
      translated += CAPFOLLOWS + ENGLISH_TO_BRAILLE_MAP[char.toLowerCase()];
    } else { 
      if (numberFollows) {
        translated += SPACE;
        numberFollows = false; 
      }
      translated += ENGLISH_TO_BRAILLE_MAP[char];
    }
  }

  return translated;
};

const isInputBraille = (input: string): boolean => {
  return input.split('').every(char => char === 'O' || char === '.') && input.length % 6 === 0;
}

const args = process.argv.slice(2);

if (isInputBraille(args[0])){
  const translation = translateBrailleToEnglish(args[0]);
  console.log(translation);
}
else {
  let translation = '';
  for (let i = 0; i < args.length; i++) {
    translation += translateEnglishToBraille(args[i]);
    if(i !== args.length - 1) translation += SPACE;
  }
  console.log(translation);
}