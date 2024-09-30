const alphaBrailleMap = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  " ": "......"
};

const numberBrailleMap = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO.."
};

const capitalBrailleSymbol = ".....O";

const numberBrailleSymbol = ".O.OOO";

const checkForBraille = (input) => {
  if (input.length % 6 !== 0) return false;

  const brailleCellPattern = /^[O.]{6}$/;

  for (let i = 0; i < input.length; i += 6) {
    const segment = input.slice(i, i + 6);
    if (!brailleCellPattern.test(segment)) {
      return false;
    }
  }

  const containsBoth = /O/.test(input) && /\./.test(input);

  return containsBoth;
};

const getCharacter = (brailleSymbol) => {
  var result = null;
  for (let key in alphaBrailleMap) {
    if (alphaBrailleMap[key] === brailleSymbol) {
      result = key;
      break;
    }
  }
  return result;
};

const getNumber = (brailleSymbol) => {
  var result = null;
  for (let key in numberBrailleMap) {
    if (numberBrailleMap[key] === brailleSymbol) {
      result = key;
      break;
    }
  }
  return result;
};

const convertToBraille = (input) => {
  const upperCaseAlphaRegex = /[A-Z]/;
  const lowerCaseAlphaRegex = /[a-z]/;
  const numberRegex = /[0-9]/;

  var result = "";

  for (let i = 0; i < input.length; i++) {
    let char = input[i];

    if (upperCaseAlphaRegex.test(char)) {
      result = result + capitalBrailleSymbol;
      char = char.toLowerCase();
      result = result + alphaBrailleMap[char];
    } else if (lowerCaseAlphaRegex.test(char)) {
      result = result + alphaBrailleMap[char];
    } else if (numberRegex.test(char)) {
      result = result + numberBrailleSymbol;
      result = result + numberBrailleMap[char];
      i++;
      while (numberRegex.test(input[i])) {
        const nextChar = input[i];
        result = result + numberBrailleMap[nextChar];
        i++;
      }

      if(i >= input.length )
        break;
    
      const nextChar = input[i];
      if (upperCaseAlphaRegex.test(nextChar)) {
        result = result + capitalBrailleSymbol;
        nextChar = nextChar.toLowerCase();
        result = result + alphaBrailleMap[nextChar];
      } else if (lowerCaseAlphaRegex.test(nextChar)) {
        result = result + alphaBrailleMap[nextChar];
      } else {
        const whiteSpace = "......";
        result = result + whiteSpace;
      }
    } else {
      const whiteSpace = "......";
      result = result + whiteSpace;
    }
  }

  console.log(result);
};

const convertToEnglish = (input) => {
  var result = "";
  for (let i = 0; i < input.length; i += 6) {
    const brailleSymbol = input.slice(i, i + 6);

    if (brailleSymbol === capitalBrailleSymbol) {
      i = i + 6;
      const nextSymbol = input.slice(i, i + 6);
      const char = getCharacter(nextSymbol);
      result = result + char.toUpperCase();
    } else if (brailleSymbol === numberBrailleSymbol) {
      i = i + 6;
      var nextSymbol = input.slice(i, i + 6);
      const num = getNumber(nextSymbol);
      result = result + num;
      i += 6;
      while (i < input.length) {
        nextSymbol = input.slice(i, i + 6);
        const num = getNumber(nextSymbol);
        result = result + num;
        i += 6;
      }
    } else {
      const char = getCharacter(brailleSymbol);
      result = result + char;
    }
  }

  console.log(result);
};

const main = () => {
  const input = process.argv.slice(2).join(" ");

  const isBraille = checkForBraille(input);

  if (isBraille) {
    convertToEnglish(input);
  } else {
    convertToBraille(input);
  }
};

main();
