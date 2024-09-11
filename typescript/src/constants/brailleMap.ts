import type { BrailleMap } from '../types';

export const brailleMap: BrailleMap = {
  brailleToEnglishAlphabets: {
      "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
      "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
      "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
      "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
      "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
      "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "number"
  },

  brailleToEnglishDigits: {
      "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
      "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
  },

  englishAlphabetsToBraille: {} as Record<string, string>,
  englishDigitsToBraille: {} as Record<string, string>
};

// Initialize englishAlphabetsToBraille
brailleMap.englishAlphabetsToBraille = Object.fromEntries(
  Object.entries(brailleMap.brailleToEnglishAlphabets).map(([k, v]) => [v, k])
);

// Initialize englishDigitsToBraille
brailleMap.englishDigitsToBraille = Object.fromEntries(
  Object.entries(brailleMap.brailleToEnglishDigits).map(([k, v]) => [v, k])
);