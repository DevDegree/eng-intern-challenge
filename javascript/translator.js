const brailleAlphabet = {
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
    " ": "......",
  };
  
  const brailleNumbers = [
    ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."
  ];
  const brailleCapitalSymbol = ".....O";
  const brailleNumberSymbol = ".O.OOO";
  const brailleEmptySpace = "......";
  const BRAILLE_SIZE = 6;
  
  const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([char, braille]) => [braille, char])
  );
  const reverseBrailleNumbers = Object.fromEntries(
    brailleNumbers.map((braille, index) => [braille, String(index)])
  );
  
  function englishToBraille(text) {
    let result = "";
    let isNumberMode = false;
  
    for (const char of text) {
      if (!isNaN(char) && char !== " ") {
        if (!isNumberMode) {
          result += brailleNumberSymbol;
          isNumberMode = true;
        }
        result += brailleNumbers[Number(char)];
        continue;
      }
  
      if (isNumberMode && char !== " ") {
        isNumberMode = false; 
      }
      
      if (char === " ") {
        result += brailleEmptySpace;
        isNumberMode = false;
        continue;
      }
  
      if (char === char.toUpperCase()) {
        result += brailleCapitalSymbol;
      }
  
      result += brailleAlphabet[char.toLowerCase()] || "";
    }
  
    return result;
  }
  
  function brailleToEnglish(brailleText) {
    let result = "";
    let isCapitalMode = false;
    let isNumberMode = false;
  
    for (let i = 0; i < brailleText.length; i += BRAILLE_SIZE) {
      const currentBraille = brailleText.slice(i, i + BRAILLE_SIZE);
  
      if (currentBraille === brailleCapitalSymbol) {
        isCapitalMode = true;
        continue;
      }
  
      if (currentBraille === brailleNumberSymbol) {
        isNumberMode = true;
        continue;
      }
  
      if (currentBraille === brailleEmptySpace) {
        result += " ";
        isNumberMode = false;
        continue;
      }
  
      if (isNumberMode) {
        result += reverseBrailleNumbers[currentBraille] || "";
      } else {
        let translatedChar = reverseBrailleAlphabet[currentBraille] || "";
        if (isCapitalMode) {
          translatedChar = translatedChar.toUpperCase();
          isCapitalMode = false;
        }
        result += translatedChar;
      }
    }
  
    return result;
  }
  
  const input = process.argv.slice(2).join(" ");
  
  if (!input) {
    console.error("Please provide an input to translate.");
    process.exit(1);
  }
  
  const isBraille = /^[O\.]+$/.test(input);
  
  console.log(isBraille ? brailleToEnglish(input) : englishToBraille(input));
  