export function isText(textToTranslate) {
  return !/^[.O]*$/.test(textToTranslate);
}

function isUpper(char) {
  return char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90;
}

function isNumber(char) {
  return char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57;
}
