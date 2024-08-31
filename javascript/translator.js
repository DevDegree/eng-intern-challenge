// braille dictionary
const brailleDict = new Map([
  ["O.....", "a"],
  ["O.O...", "b"],
  ["OO....", "c"],
  ["OO.O..", "d"],
  ["O..O..", "e"],
  ["OOO...", "f"],
  ["OOOO..", "g"],
  ["O.OO..", "h"],
  [".OO...", "i"],
  [".OOO..", "j"],
  ["O...O.", "k"],
  ["O.O.O.", "l"],
  ["OO..O.", "m"],
  ["OO.OO.", "n"],
  ["O..OO.", "o"],
  ["OOO.O.", "p"],
  ["OOOOO.", "q"],
  ["O.OOO.", "r"],
  [".OO.O.", "s"],
  [".OOOO.", "t"],
  ["O...OO", "u"],
  ["O.O.OO", "v"],
  [".OOO.O", "w"],
  ["OO..OO", "x"],
  ["OO.OOO", "y"],
  ["O..OOO", "z"],
  ["......", " "],
  [".....O", "cap"],
  [".O.OOO", "num"],
]);

// braille number dictionary
const brailleNums = new Map([
  ["O.....", "1"],
  ["O.O...", "2"],
  ["OO....", "3"],
  ["OO.O..", "4"],
  ["O..O..", "5"],
  ["OOO...", "6"],
  ["OOOO..", "7"],
  ["O.OO..", "8"],
  [".OO...", "9"],
  [".OOO..", "0"],
  ["......", " "],
]);

// english dictionary
const engDict = new Map([
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "OO..O."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  ["A", ".....OO....."],
  ["B", ".....OO.O..."],
  ["C", ".....OOO...."],
  ["D", ".....OOO.O.."],
  ["E", ".....OO..O.."],
  ["F", ".....OOOO..."],
  ["G", ".....OOOOO.."],
  ["H", ".....OO.OO.."],
  ["I", ".....O.OO..."],
  ["J", ".....O.OOO.."],
  ["K", ".....OO...O."],
  ["L", ".....OO.O.O."],
  ["M", ".....OOO..O."],
  ["N", ".....OOO.OO."],
  ["O", ".....OO..OO."],
  ["P", ".....OOOO.O."],
  ["Q", ".....OOOOOO."],
  ["R", ".....OO.OOO."],
  ["S", ".....O.OO.O."],
  ["T", ".....O.OOOO."],
  ["U", ".....OO...OO"],
  ["V", ".....OO.O.OO"],
  ["W", ".....O.OOO.O"],
  ["X", ".....OOO..OO"],
  ["Y", ".....OOO.OOO"],
  ["Z", ".....OO..OOO"],
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."],
  [" ", "......"],
]);

// parse input from command line into a single string
const parseInput = () => {
  let inputString = "";
  const len = process.argv.length;
  process.argv.forEach((val, index) => {
    if (index === len - 1) {
      inputString += val;
    } else if (index > 1) {
      inputString += val + " ";
    }
  });
  return inputString;
};

// determine if input string represents braille characters or not
// ASSUMPTION: braille raised dot must be capital "O"
const isBraille = (str) => {
  const braillePattern = /(\.|O){6}/;
  if (str.length % 6 !== 0) {
    return false;
  } else {
    for (let i = 0; i < str.length; i += 6) {
      if (!braillePattern.test(str.slice(i, i + 6))) {
        return false;
      }
    }
  }
  return true;
};

// translate braille string to english
// REQUIRES: string consists of properly formatted braille characters representing a-z, A-Z, 0-9, or space character
const brailleToEng = (str) => {
  let res = "";
  let nextChar = "";
  let isCap = 0;
  let isNum = 0;
  for (let i = 0; i < str.length; i += 6) {
    if (isNum) {
      nextChar = brailleNums.get(str.slice(i, i + 6));
      res += nextChar;
      if (nextChar === " ") {
        isNum = 0;
      }
    } else {
      nextChar = brailleDict.get(str.slice(i, i + 6));
      if (isCap) {
        nextChar = nextChar.toUpperCase(nextChar);
        isCap = 0;
      }
      switch (nextChar) {
        case "cap":
          isCap = 1;
          break;
        case "num":
          isNum = 1;
          break;
        default:
          res += nextChar;
      }
    }
  }
  return res;
};

// translate english string to braille
// REQUIRES: string only includes a-z, A-Z, 0-9, or space characters, and all numbers are followed by either a number or space
const engToBraille = (str) => {
  const cap = ".....O";
  const num = ".O.OOO";
  let numChain = 0;
  let res = "";
  for (const char of str) {
    //console.log(char);
    if (isNum(char) && numChain === 0) {
      numChain = 1;
      res += (num + engDict.get(char));
      //console.log("new number string");
      //console.log(num + engDict.get(char));
    } else {
      res += engDict.get(char);
      if (numChain === 1 && !isNum(char)) {
        numChain = 0;
      }
      //console.log(engDict.get(char));
    }
  }
  return res;
};

const isNum = (char) => !isNaN(parseInt(char));

const main = () => {
  const userString = parseInput();
  const brailleBool = isBraille(userString);
  let translatedString = "";
  if (brailleBool) {
    translatedString = brailleToEng(userString);
  } else {
    translatedString = engToBraille(userString);
  }
  console.log(translatedString);
};

main();
