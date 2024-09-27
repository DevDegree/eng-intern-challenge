const brailleCharacters = {
    // Alphabet
    A: "O.....",
    B: "O.O...",
    C: "OO....",
    D: "OO.O..",
    E: "O..O..",
    F: "OOO...",
    G: "OOOO..",
    H: "O.OO..",
    I: ".OO...",
    J: ".OOO..",
    K: "O...O.",
    L: "O.O.O.",
    M: "OO..O.",
    N: "OO.OO.",
    O: "O..OO.",
    P: "OOO.O.",
    Q: "OOOOO.",
    R: "O.OOO.",
    S: ".OO.O.",
    T: ".OOOO.",
    U: "O...OO",
    V: "O.O.OO",
    W: ".OOO.O",
    X: "OO..OO",
    Y: "OO.OOO",
    Z: "O..OOO",
  
    // Special symbols
    capitalFollows: ".....O",
    decimalFollows: ".O...O",
    numberFollows: ".O.OOO",
    space: "......",
  };
  
  // Numbers (1-0)
  const brailleNumbers = {
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO..",
  };
  
  // Reverse mapping: brailleCharacters
  const englishCharacters = {};
  for (const [key, value] of Object.entries(brailleCharacters)) {
    englishCharacters[value] = key;
  }
  
  // Reverse mapping: brailleNumbers
  const englishNumbers = {};
  for (const [key, value] of Object.entries(brailleNumbers)) {
    englishNumbers[value] = key;
  }
  
  module.exports = {brailleCharacters, brailleNumbers, englishCharacters, englishNumbers}