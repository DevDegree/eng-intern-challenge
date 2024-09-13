const input = "Abc 123 xYz";

const brailleMap = {
  a: "100000",
  b: "101000",
  c: "110000",
  d: "110100",
  e: "100100",
  f: "111000",
  g: "111100",
  h: "101100",
  i: "011000",
  j: "011100",
  k: "100010",
  l: "101010",
  m: "110010",
  n: "110110",
  o: "100110",
  p: "111010",
  q: "111110",
  r: "101110",
  s: "011010",
  t: "011110",
  u: "100011",
  v: "101011",
  w: "011101",
  x: "110011",
  y: "110111",
  z: "100111",
  " ": "000000",

  // Numbers & symbols
  1: "100000",
  2: "101000",
  3: "110000",
  4: "110100",
  5: "100100",
  6: "111000",
  7: "111100",
  8: "101100",
  9: "011000",
  0: "011100",
  number: "010111",
  capital: "000001",
  ".": "001101",
  ",": "001000",
  "?": "001011",
  "!": "001110",
  ";": "001010",
  ":": "001100",
  "-": "000011",
  "(": "101001",
  ")": "010110",
  "/": "010010",
  ">": "100110",
  "<": "011001",
};

const reversedBrailleMap = Object.entries(brailleMap).reduce(
  (acc, [key, value]) => {
    acc[value] = key;
    return acc;
  },
  {}
);

function isBraille(input) {
    return /^[.O\s]{6}([.O\s]{6})*$/g.test(input.trim());
}

function brailleToText(brailleInput) {
    // Ensure input is a string
    if (typeof brailleInput !== 'string') {
      throw new TypeError('Input must be a string');
    }
  
    // Handle edge cases (e.g., empty string)
    if (brailleInput.length === 0) {
      return '';
    }
  
    let result = '';
    let isCapital = false;
    let isNumberSequence = false;
  
    for (let i = 0; i < brailleInput.length; i += 6) {
      const block = brailleInput.slice(i, i + 6);
  
      if (block.length < 6) {
        break;
      }
  
      const binaryPattern = block
        .split('')
        .map(dot => dot === 'O' ? '1' : '0')
        .join('');
  
      if (binaryPattern === brailleMap['capital']) {
        isCapital = true;
        continue;
      }
  
      if (binaryPattern === brailleMap['number']) {
        isNumberSequence = true;
        continue;
      }
  
      const char = reversedBrailleMap[binaryPattern] || '';
  
      if (isNumberSequence && char.match(/[a-j]/)) {
        const number = '1234567890'['abcdefghij'.indexOf(char)];
        result += number;
      } else {
        result += isCapital ? char.toUpperCase() : char.toLowerCase();
        isCapital = false;
      }
  
      if (char === ' ') {
        isNumberSequence = false;
      }
    }
  
    return result;
}


function textToBraille(textInput) {
    // Ensure input is a string
    if (typeof textInput !== 'string') {
      throw new TypeError('Input must be a string');
    }
  
    // Handle edge cases (e.g., empty string)
    if (textInput.length === 0) {
      return '';
    }
  
    let result = '';
    let inNumberSequence = false;
  
    for (const char of textInput) {
      if (char.match(/[0-9]/)) {
        if (!inNumberSequence) {
          result += brailleMap['number'];
          inNumberSequence = true;
        }
        result += brailleMap[char];
      } else {
        inNumberSequence = false;
  
        if (char === char.toUpperCase() && char >= 'A' && char <= 'Z') {
          result += brailleMap['capital'];
        }
  
        const brailleChar = brailleMap[char.toLowerCase()];
        result += brailleChar || '000000';
      }
    }
  
    // Convert binary to Braille characters
    return result.split('').map(bit => bit === '1' ? 'O' : '.').join('');
}

function transateBrailleOrText(input) {
    // Ensure input is a string
    if (typeof input !== 'string') {
      throw new TypeError('Input must be a string');
    }
  
    if (isBraille(input)) {
      return brailleToText(input);
    } else {
      return textToBraille(input);
    }
  }

console.log(translateBrailleOrText(input));