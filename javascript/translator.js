const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

const reverseBrailleDict = Object.fromEntries(Object.entries(brailleDict).map(([k, v]) => [v, k]));

const capitalIndicator = '.....O'; 
const numberIndicator = '.O.OOO';  

function isBraille(text) {
    const hasCapitalO = /O/.test(text); 
    const hasDot = /\./.test(text);     
    const isDivisibleBySix = text.length % 6 === 0;  
    
    return hasCapitalO && hasDot && isDivisibleBySix;
}

function brailleToEnglish(brailleInput) {
    const patternLength = 6;
    let result = "";
    let isCap = false;
    let isNum = false;
  
    for (let i = 0; i < brailleInput.length; i += patternLength) {
      const brailleCode = brailleInput.substring(i, i + patternLength);
  
      if (brailleCode === capitalIndicator) {
      
        isCap = true;
        continue; 
      } else if (brailleCode === numberIndicator) {
        
        isNum = true;
        continue; 
      } else if (brailleCode === "......") {
       
        isNum = false; 
        result += " ";
        continue;
      }
  
      let decodedChar = reverseBrailleDict[brailleCode] || "?";
  
      if (isNum) {
        if (decodedChar >= 'a' && decodedChar <= 'i') {
          decodedChar = String.fromCharCode(decodedChar.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
        } else if (decodedChar === 'j') {
          decodedChar = '0';
        }
        result += decodedChar; 
      } else if (isCap && decodedChar !== ' ') {
        decodedChar = decodedChar.toUpperCase(); 
        isCap = false; 
        result += decodedChar;
      } else {
        result += decodedChar;
      }
    }
  
    return result;
  }

function englishToBraille(englishInput) {
    let result = "";
    let inNumberSequence = false;
  
    for (const char of englishInput) {
        if (char === " ") {
            result += "......"; 
            inNumberSequence = false;
        } else if (char >= "A" && char <= "Z") {
            result += capitalIndicator;
            result += brailleDict[char.toLowerCase()] || "......";
            inNumberSequence = false;
        } else if (char >= "0" && char <= "9") {
            if (!inNumberSequence) {
                result += numberIndicator;
                inNumberSequence = true;
            }
            result += brailleDict[char];
        } else {
            result += brailleDict[char] || "......";
            inNumberSequence = false;
        }
    }
  
    return result;
}

function main() {
    if (process.argv.length !== 3) {
        console.error("Usage: node translator.js <text>");
        return;
    }

    const inputText = process.argv[2].trim();

    if (isBraille(inputText)) {
        console.log(brailleToEnglish(inputText));
    } else {
        console.log(englishToBraille(inputText));
    }
}

main();