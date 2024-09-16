const ENGLISH_LETTER_TO_BRAILLE = {
  // Letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', 

  // Spaces
  ' ': '......',
};

const NUMBER_TO_BRAILLE = {
  // Numbers
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
  '8': 'O.OO..', '9': '.OO...', '0': '.O....', 

}

const BRAILLE_TO_ENGLISH_LETTER = Object.fromEntries(
  Object.entries(ENGLISH_LETTER_TO_BRAILLE).map(([key, value]) => [value, key])
);

const BRAILLE_TO_NUMBER = Object.fromEntries(
  Object.entries(NUMBER_TO_BRAILLE).map(([key, value]) => [value, key])
);

function isBraille(input) {
  return /^[O.]+$/.test(input) && input.length % 6 == 0;
}