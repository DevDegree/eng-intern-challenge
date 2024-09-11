export function assert(condition: unknown, msg?: string): asserts condition {
  if (!condition)
    throw new Error(`AssertionError: ${msg ?? 'condition is falsy'}`);
}

export function isBraille(str: string) {
  const characters = new Set(str);
  characters.delete('.');
  characters.delete('O');
  return characters.size === 0 && str.length % 6 === 0;
}

export function isCapitalLetter(char: string) {
  return /[A-Z]/.test(char);
}

export function isDigit(char: string) {
  assert(char.length === 1, `char must be a single character, got: "${char}"`);
  return char >= '0' && char <= '9';
}

export function getObjectKeyByValue(
  object: Record<string, string>,
  value: string,
) {
  return Object.keys(object).find((key) => object[key] === value);
}
