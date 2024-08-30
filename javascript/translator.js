//
// By Khaled Elshokri, 3rd year Computer Engineering Student.
//

// Single map for Braille-to-English and English-to-Braille translations
const BRAILLE_MAP = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
  'O..OOO': 'z',
  '.....O': 'capital',
  '.O.OOO': 'number',
  '.O...O': 'decimal',
  '......': ' ',
  // Numbers
  '1': 'O.....', '2': 'O.O...', '3': 'OO....' , '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
};

// Function to initialize reverse mappings for English-to-Braille
function initializeEnglishToBrailleMap()
{
  const englishToBraille = {};

  // Init reverse map Loop
  for (const [key, value] of Object.entries(BRAILLE_MAP))
  {
    if (!['capital', 'number', 'decimal', ' '].includes(value))
    {
      englishToBraille[value] = key;
    }
  }

  englishToBraille['capital'] = '.....O';
  englishToBraille['number'] = '.O.OOO';
  englishToBraille[' '] = '......';

  return englishToBraille;
}

const ENGLISH_TO_BRAILLE = initializeEnglishToBrailleMap();

// Check if the input string is in Braille
function isBraille(input)
{
  return input.length % 6 === 0 && [...input].every(char => char === 'O' || char === '.');
}

// Translate Braille to English
function translateBrailleToEnglish(input)
{
  let englishOutput = '';
  let IsNum = false;
  
  // Translation Loop
  for (let i = 0; i < input.length; i += 6)
  {
    let brailleChar = input.slice(i, i + 6);
    
    if (brailleChar === ENGLISH_TO_BRAILLE['capital'])
    {
      i += 6;

      if (i >= input.length) {
        break; // Prevent out-of-bounds error
      }

      brailleChar = input.slice(i, i + 6);
      englishOutput += BRAILLE_MAP[brailleChar].toUpperCase();
    }
    else if (brailleChar === ENGLISH_TO_BRAILLE['number'])
    {
      IsNum = true;
    }
    else if (brailleChar === ENGLISH_TO_BRAILLE[' '])
    {
      IsNum = false;
      englishOutput += ' ';
    }
    else
    {
      if (IsNum)
      {
        englishOutput += Object.keys(BRAILLE_MAP).find(key => BRAILLE_MAP[key] === brailleChar);
      }
      else
      {
        englishOutput += BRAILLE_MAP[brailleChar];
      }
    }
  }
  
  return englishOutput;
}

// Translate English to Braille
function translateEnglishToBraille(input)
{
  let brailleOutput = '';
  let IsNum = 0;

  // Translation Loop
  for (const char of input)
  {
    if (char >= 'A' && char <= 'Z')
    {
      brailleOutput += ENGLISH_TO_BRAILLE['capital'];
      brailleOutput += ENGLISH_TO_BRAILLE[char.toLowerCase()];
    }
    else if (char >= '0' && char <= '9')
    {
      if (IsNum < 1)
      {
        brailleOutput += ENGLISH_TO_BRAILLE['number'];
        brailleOutput += BRAILLE_MAP[char];

        IsNum++;
      }
      else
      {
        brailleOutput += BRAILLE_MAP[char];
      }

    }
    else
    {
      IsNum = false;
      brailleOutput += ENGLISH_TO_BRAILLE[char];
    }
  }
  
  return brailleOutput;
}

// Main function to handle input and translation
function main()
{
    
  if (process.argv.length < 3)
  {
    console.log('Error: Failed to get user input or user input is NULL');
    return;
  }
  
  const input = process.argv.slice(2).join(' ');
  
  if (isBraille(input))
  {
    console.log(translateBrailleToEnglish(input));
  }
  else
  {
    console.log(translateEnglishToBraille(input));
  }
}

main();
