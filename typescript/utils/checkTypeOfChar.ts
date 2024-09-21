export function isUpperCase(char: string) {
  const charCode = char.charCodeAt(0);
  return (charCode >= 65 && charCode <= 90);
}

export function isNumber(char: string) {
  const charCode = char.charCodeAt(0);
  return (charCode >= 48 && charCode <= 57);
}
