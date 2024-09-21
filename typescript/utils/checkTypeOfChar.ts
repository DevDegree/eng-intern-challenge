import {EnglsihChar} from '../types/types';

export function isUpperCase(char: EnglsihChar) {
  const charCode = char.charCodeAt(0);
  return (charCode >= 65 && charCode <= 90);
}

export function isNumber(char: EnglsihChar) {
  const charCode = char.charCodeAt(0);
  return (charCode >= 48 && charCode <= 57);
}
