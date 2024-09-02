/* This file would store functions that are used in multiple places of the code */

export const getConvertedChar = (char: string, brailMap: Map<string, string>): string => {
  return brailMap.get(char) ?? "";
};
