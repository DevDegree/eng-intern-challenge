const englishToBrailleMap= {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
  }
  
  const brailleToEnglishMap = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OOO...': 'd',
    'O..O..': 'e',
    'OO.O..': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OOO.O.': 'n',
    'O..OO.': 'o',
    'OO.OO.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OOO.OO': 'y',
    'O..OOO': 'z',
  };
  
  const brailleToNumberMap = {
    '.OOO..': '0',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
  };
  
  const numberFollowsBraille = '.O.OOO';
  const uppercaseFollowsBraille = '.....O';
  const spaceBraille = '......';
  
  
  
  /**  
    Function to parse braille to english:
    * @param {string} brailleString
    * @return {string} 
    
    */
  function parseBrailleToEnglish(brailleString) {
    let englishString = '';
    let isUpperCaseFollows = false;
    let isNumberFollows = false;
    for (let i = 0; i < brailleString.length; i += 6) {
      const brailleCharacter = brailleString.slice(i, i + 6);
      if (brailleCharacter === uppercaseFollowsBraille) {
        isUpperCaseFollows = true;
      } else if (brailleCharacter === numberFollowsBraille ){
        isNumberFollows = true;
      } else if (brailleCharacter === spaceBraille) {
        isNumberFollows = false;
        englishString += ' ';
      } else {
        let translatedBraille = brailleToEnglishMap[brailleCharacter];
        if (isNumberFollows) {
          translatedBraille = brailleToNumberMap[brailleCharacter];
        }
        if (isUpperCaseFollows) {
          translatedBraille = translatedBraille?.toUpperCase();
          isUpperCaseFollows = false;
        }
        englishString += translatedBraille;
      }
    }
    return englishString;
  }
  
  /**  
    Function to parse english to Braille:
    * @param {string} englishString
    * @return {string} 
    */
  
  function parseEnglishToBraille(englishString) {
    let brailleString = '';
    let inNumber = false;
    for (let character of englishString) {
      if (character === " ") {
        brailleString += spaceBraille;
        inNumber = false;
    } else if (character.toUpperCase() !== character ){
            brailleString += englishToBrailleMap[character];
  
    } else if(character<='9' && character >='0' ){
      if (!inNumber) {
          brailleString += numberFollowsBraille;  
          inNumber = true;
      }
      brailleString += englishToBrailleMap[character]
    } else {
      brailleString += uppercaseFollowsBraille + englishToBrailleMap[character.toLowerCase()]; 
  
    }}
  
    return brailleString;
    
  }
  
  
  /**  
    Function to detect a braille string 
    * @param {string} string
    * @return {boolean} 
    */
  function isBraille(string) {
    var divisibleBy6 = string.length % 6 === 0; 
    var containsBrailleOnly = /[O.]/.test(string); 
    return divisibleBy6 && containsBrailleOnly; 
  }
  
  
  // Getting and preparing arguments for parsing
  
  const args = process.argv.slice(2); 
  const input = args.join(' '); 
  
  // Parse string using the correct function (Braille -> English or vice versa )
  
  if (isBraille(input)){
    console.log(parseBrailleToEnglish(input)); 
  } else {
    console.log(parseEnglishToBraille(input)); 
  }
  
  
  
  
    