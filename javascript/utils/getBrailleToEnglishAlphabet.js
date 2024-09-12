import { englishBrailleAlphabet } from "../constants/englishBrailleAlphabet.js";

export const getBrailleEnglishAlphabet = () => {
  return new Map(
    Object.entries(englishBrailleAlphabet).flatMap(([key, [dot1, dot2]]) => [
      [dot1, key],
      [dot2, key],
    ])
  );
};
