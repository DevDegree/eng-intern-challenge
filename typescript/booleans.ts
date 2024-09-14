import { Braille } from "./types";
import { utilityMap } from "./objects";

export function isUtility(str: Braille) {
  return (
    str === utilityMap.capitalize ||
    str === utilityMap.number ||
    str === utilityMap.space
  );
}

export function isNumber(str: string) {
  return /[0-9]/.test(str);
}

export function isBraille(str: string): boolean {
  if (str.length % 6 !== 0) {
    return false;
  }

  for (let char of str) {
    if (!(char == "O" || char == ".")) {
      return false;
    }
  }

  return true;
}
