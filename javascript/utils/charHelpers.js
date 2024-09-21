export function isEnglish(textToTranslate) {
  return !/^[.O]*$/.test(textToTranslate);
}

export function isUpper(char) {
  return char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90;
}

export function isNumber(char) {
  return char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57;
}

export function chunkString(input, chunkSize = 6) {
  const result = [];
  for (let i = 0; i < input.length; i += chunkSize) {
    result.push(input.substring(i, i + chunkSize));
  }
  return result;
}
