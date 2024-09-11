export type Choice = {
  name: string;
  value: string;
}

export type BrailleToEnglish = Record<string, string>;
export type EnglishToBraille = Record<string, string>;

export type BrailleMap = {
  brailleToEnglishAlphabets: BrailleToEnglish;
  brailleToEnglishDigits: BrailleToEnglish;
  englishAlphabetsToBraille: EnglishToBraille;
  englishDigitsToBraille: EnglishToBraille;
};