const BRAILLE_TO_ENGLISH_LOWER = {
    "O.....": "a","O.O...": "b","OO....": "c","OO.O..": "d","O..O..": "e","OOO...": "f","OOOO..": "g",
    "O.OO..": "h",".OO...": "i",".OOO..": "j","O...O.": "k","O.O.O.": "l","OO..O.": "m","OO.OO.": "n",
    "O..OO.": "o","OOO.O.": "p","OOOOO.": "q","O.OOO.": "r",".OO.O.": "s",".OOOO.": "t","O...OO": "u",
    "O.O.OO": "v",".OOO.O": "w","OO..OO": "x", "OO.OOO": "y","O..OOO": "z","......": " ",
  };
  
  const BRAILLE_TO_ENGLISH_NUMS = {
    "O.....": "1","O.O...": "2",
    "OO....": "3","OO.O..": "4",
    "O..O..": "5","OOO...": "6",
    "OOOO..": "7","O.OO..": "8",
    ".OO...": "9",".OOO..": "0",
  };
  
  const BRAILLE_TO_ENGLISH_SYMBOLS = {
    "..OO.O": ".", "..O...": ",","..O.OO": "?", "..OO..": "!", "..O.O.": ":","..O..O": ";",
    "...O..": "-","..O..O": "/","...O.O": "<","...OO.": ">","...OOO": "(","..O..O": ")",
    "......": " ",".....O": "CAP", ".O.OOO": "NUM",  "..OOO.": "DEC", 
  };
  
const ENGLISH_TO_BRAILLE_LOWER = Object.fromEntries(
    Object.entries(BRAILLE_TO_ENGLISH_LOWER).map(([k, v]) => [v, k])
  );
  
  const ENGLISH_TO_BRAILLE_NUMS = {
    1: "O.....",2: "O.O...",
    3: "OO....",4: "OO.O..",
    5: "O..O..",6: "OOO...",
    7: "OOOO..",8: "O.OO..",
    9: ".OO...",0: ".OOO..",
  };
  
  const ENGLISH_TO_BRAILLE_SYMBOLS = {
    ".": "..OO.O",",": "..O...","?": "..O.OO","!": "..OO..",
    ":": "..O.O.",";": "..O..O","-": "...O..","/": "..O..O",
    "<": "...O.O",">": "...OO.","(": "...OOO",")": "..O..O",
    CAP: ".....O",NUM: ".O.OOO",DEC: "..OOO."," ": "......",
  }
  
    
    //basic function
    function translateToEnglish(inputText)
    {
        return "Inside translate to english";
    }
    
    //basic function
    function translateToBraille(inputText)
    {
        return "Inside translate to braille";
    }


    function main() {
    const inputArgs = process.argv.slice(2);
    
    //for user input
    if (inputArgs.length < 1) {
      return;
    }
  
    const inputText = inputArgs.join(" ");
  
    // regex to check if it is braille or not
    if (/^[O. ]+$/.test(inputText)) {
      const translatedText = translateToEnglish(inputText);
      console.log(translatedText);
    } else {
      const translatedText = translateToBraille(inputText);
      console.log(translatedText);
    }
  }
  
  main();