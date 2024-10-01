function isBraille(input) {
  for (let char of input) {
    if (char !== "." && char !== "O") {
      return false;
    }
  }

  return true;
}

function isChar(str) {
  if (str.length !== 1) {
    throw new Error("'char' must be a single character string!");
  }
  return true;
}

function isNumber(char) {
  if (isChar(char)) {
    return !isNaN(parseFloat(char))
  }
}

function isSpace(char) {
  if (isChar(char)) {
    return char === " ";
  }
}

function isCapital(char) {
  if (isChar(char)) {
    return char.toUpperCase() === char;
  }
}

function invertObject(obj) {
  return Object.entries(obj).reduce((acc, [key, val]) => {
    acc[val] = key;
    return acc;
  }, {})
}

module.exports = {
  isBraille,
  isChar,
  isNumber,
  isSpace,
  isCapital,
  invertObject
}