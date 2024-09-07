const readline = require("node:readline");

// Datasets for mapping english alphanumeric characters to braille symbols
const charMap = {
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
};

const numberMap = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  O: ".OOO..",
}

// Map to determine if it is a follows symbol, [number follows, capital follows]
const brailleSymbolMap = [".O.OOO", ".....O"];

// RegEx to check if the string contains only brailler characters
const brailleSymbolRegEx = /^[O.]+$/gi; // Only contains 'O' and '.' => Input is Braille

// RegEx to check if is a number
const regExpIsNumber = /^\d+$/;

// Output variable
let outputString;

// Set 'follows' symbol flags for braille characters
function setBrailleFollowsFlags(brailleSymbol, isNextNumber, isNextCapital) {
  switch (true) {
    // If is space follows braille symbol
    case brailleSymbol === "......":
      // Unset isNextNumber because space denotes following symbol is not a number, according to requirements
      if (isNextNumber === true) isNextNumber = false;
      break;

    // If is number follows space symbol
    case brailleSymbol === ".O.OOO":
      isNextNumber = true;
      break;

    // If is captial follows capital symbol
    case brailleSymbol === ".....O":
      isNextCapital = true;
      break;

    default:
      break;
  }
  // Return updated flag values
  return { isNextNumber, isNextCapital };
}

// Determine if the next Braille character is a follows symbol, uses isBrailleSymbol map
function isBrailleSymbol (brailleChar) {
  return brailleSymbolMap.includes(brailleChar);
}

// Converts a Braille Character to English Alphanumeric based on maps
function convertCharBrailleToAlphaNumeric (symbolMap, character) {
  return Object.keys(symbolMap).find(
    (brailleValue) => symbolMap[brailleValue] === character
  );
}

// Convert Braille characters to english character based on flags
function convertBrailleSymbolToEng(brailleChar, isNextCapital, isNextNumber) {
  let convertedEngChar = "";

  switch (true) {
    // If braille symbol of space, return ' ' space
    case brailleChar === "......":
      convertedEngChar = " ";
      break;

    // If is a number, convert using the numberMap
    case isNextNumber === true:
      convertedEngChar = convertCharBrailleToAlphaNumeric(numberMap, brailleChar);
      break;
    
    // If is a captial letter, convert using the charMap and transform to uppercase
    case isNextCapital === true:
      convertedEngChar = convertCharBrailleToAlphaNumeric(charMap,brailleChar).toUpperCase();
      // Update the capital flag to false
      isNextCapital = false;
      break;

    // Otherwise, is a lower case alphabet, convert using the charMap
    default:
      convertedEngChar = convertCharBrailleToAlphaNumeric(charMap,brailleChar);
      break;
  }  
  // Return output and update capital flag
  return { convertedEngChar, isNextCapital };
}

function translateBrailleStringToEng(inputString) {
  // Flags denoting 'follows' symbols for Braille chars
  let isNextCapital = false; // Captial Follows
  let isNextNumber = false; // Number Follows
  
  // Variable to store Eng characters after conversion
  let returnString = [];
  
  // Iterate over the Braille string, six characters at a time => six chars = one braille symbol
  for( let i = 0; i < inputString.length/6; i ++){
    const substr = inputString.substring(i*6, (i*6) + 6);
    
    // Update the flags for the next symbol => to determine if is capital or is number
    const updatedFlags = setBrailleFollowsFlags(substr, isNextNumber, isNextCapital);
    isNextCapital = updatedFlags.isNextCapital;
    isNextNumber = updatedFlags.isNextNumber;
    
    // Convert value if it is not a follows symbol, => is an alphabet, numeric, or space symbol
    if(!isBrailleSymbol(substr)) {
      const updatedDataAndFlag = convertBrailleSymbolToEng(substr, isNextCapital, isNextNumber);
      // Push the converted char to the variable
      returnString.push(updatedDataAndFlag.convertedEngChar);
      // Update the 'capital follows' symbol flag
      isNextCapital = updatedDataAndFlag.isNextCapital;
    }
  }
  return returnString.join("");
}

// Returns the next Braille 'follows' symbol if conditions are met, otherwise nothing
function getNextBrailleSymbol(char, prevChar = null) {
  let nextBrailleSymbol = '';

  switch (true) {
    // If next character is capital, return 'capital follows' symbol
    case char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90:
      nextBrailleSymbol = ".....O";
      break;

    // If next character is number & previous char was not a number, return 'number follows' symbol
    case regExpIsNumber.test(char) &&
      prevChar !== null &&
      regExpIsNumber.test(prevChar) === false:
      nextBrailleSymbol = ".O.OOO";
      break;

    // If next character is a space, return 'space' symbol
    case char === " ":
      nextBrailleSymbol = "......";

    // Else, don't return any symbol
    default:
      break;
  }
  return nextBrailleSymbol;
}

// Converts English alphanumeric to Braille equivalent
function convertCharEngToBraille (character) {  
  // If is an alphabet
  if(character.match(/[a-z]/i)){
    return charMap[`${character.toLowerCase()}`];
  } 
  // If is a number
  else if(character.match(/^\d+$/)){
    return numberMap[`${character}`];
  } 
}

// Convert English string to Braille
function translateEngStringToBraille (inputString) {
  let returnStringBraille = [];
  let previousChar = "";
  
  // Iterate over the characters in the string
  inputString.split("").forEach((char) => {
    // Conditionally add Braille 'follows' symbol
    returnStringBraille.push(getNextBrailleSymbol(char, previousChar));
    // Convert English Alpha Numeric Character to Braille
    returnStringBraille.push(convertCharEngToBraille(char));
    // Set current character as previous character
    previousChar = char;
  });
  // Outputs the string
  return returnStringBraille.join("");
}

// Main Function: Convert text based on input
function convertToEnglishOrBraille(inputString) {
  // Is Braille String, Convert To English Alphanumeric
  if (inputString.match(brailleSymbolRegEx)) {
    // Check if string length is multiple of 6 => valid Braille Expression (6 chars per braille symbol)
    if (inputString.length % 6 === 0) {
      return translateBrailleStringToEng(inputString);
    } else {
      // Input braille string is invalid
      console.log("Braille input is invalid");
    }
  }
  // Is English String, convert to Braille
  else {
    return translateEngStringToBraille(inputString);
  }
}

// Call the main function based on the input mode
// Uses command line arguments if present
if (process.argv[2]) {
  outputString = convertToEnglishOrBraille(process.argv.slice(2).join(", "));
  // Outputs the result
  console.log(outputString);
}
// Else asks user to enter the text via console
else {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.question(``, (inputString) => {
    outputString = convertToEnglishOrBraille(`${inputString}`);
    // Outputs the result
    console.log(outputString);
    rl.close();
  });
}
