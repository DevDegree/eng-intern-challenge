export type BrailleSymbol = "O" | ".";
export type BrailleLetter = [BrailleSymbol, BrailleSymbol, BrailleSymbol, BrailleSymbol, BrailleSymbol, BrailleSymbol];
export type BrailleToEnglishMap = { [key: string]: string };
export type EnglishToBrailleMap = { [key: string]: BrailleLetter };
