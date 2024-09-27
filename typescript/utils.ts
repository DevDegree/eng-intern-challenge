export function splitBraille(input: string) {
  return input.match(/.{1,6}/g) || [];
}

export function isValidBraille(input: string) {
  return /^[O.]*$/.test(input) && input.length % 6 === 0;
}

export function isUpperCase(string: string) {
  return /^[A-Z]*$/.test(string);
}

export function isNumber(input: string) {
  return !isNaN(parseInt(input));
}

export function getKeyByValue(object: Record<string, string>, value: string) {
  return Object.keys(object).find((key) => object[key] === value);
}
