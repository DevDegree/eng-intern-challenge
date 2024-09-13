// Dictionary Alphabet & Numbers
const alphabet = {
    number: '.O.OOO',
    capital: '.....O',
    decimal: '.O...O',
    a: 'O.....',
    b: 'O.O...',
    c: 'OO....',
    d: 'OO.O..',
    e: 'O..O..',
    f: 'OOO...',
    g: 'OOOO..',
    h: 'O.OO..',
    i: '.OO...',
    j: '.OOO..',
    k: 'O...O.',
    l: 'O.O.O.',
    m: 'OO..O.',
    n: 'OO.OO.',
    o: 'O..OO.',
    p: 'OOO.O.',
    q: 'OOOOO.',
    r: 'O.OOO.',
    s: '.OO.O.',
    t: '.OOOO.',
    u: 'O...OO',
    v: 'O.O.OO',
    w: '.OOO.O',
    x: 'OO..OO',
    y: 'OO.OOO',
    z: 'O..OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    space: '......'
};
 
const numbers = {
    1: 'O.....',
    2: 'O.O...',
    3: 'OO....',
    4: 'OO.O..',
    5: 'O..O..',
    6: 'OOO...',
    7: 'OOOO..',
    8: 'O.OO..',
    9: '.OO...',
    0: '.OOO..'
};

// Function to translate to Braille
function englishToBraille(input){
    let count = 0;
    let translatedText = '';
    for(let i=0; i<input.length; i++){
        let char = input[i];

        // check upper case
        if (!!char.match(/[A-Z]/)){
            translatedText += alphabet.capital;
            count= 0;
        }
        char = char.toLowerCase();
        if(!!char.match(/^[a-zA-Z.,!?]+$/)){
            count = 0;
            translatedText+= alphabet[`${char}`];
    }
        else if(!!char.match(/\d/) ) {
            if(count == 0){
                translatedText += alphabet.number;
                translatedText += numbers[`${char}`];
                count++;
            }
            else{
            translatedText += numbers[`${char}`];
            }
        }
        else if( char = ' ' ){
        translatedText += alphabet.space;
    }  
        
    }
 return translatedText;
};

// Helper function to find a matching Braille character
const findCharacter = (braille, dict) => {
    for (const key in dict) {
        if (dict[key] === braille) {
            return key;
        }
    }
    return null;
};

function splitAndJoinString(input) {
    let result = '';
    for (let i = 0; i < input.length; i += 6) {
      result += input.slice(i, i + 6) + " "; // Adding space between each chunk
    }
    return result.trim(); // Trim the extra space at the end
}
// Function to translate to English
function brailleToEnglish(inputBraille) {
    const input = inputBraille.split(' ');
    // console.log(input);
    let result = '';
    let isNumber = false;
    let isCapital = false;

    for (let i = 0; i < input.length; i++) {
        const currentBraille = input[i];

        if (currentBraille === alphabet.number) {
            isNumber = true;
            continue;
        } else if (currentBraille === alphabet.capital) {
            isCapital = true;
            continue;
        } else if (currentBraille === alphabet.space) {
            result += ' ';
            isNumber = false;  // Reset number mode on space
            continue;
        }
        let character;

        // Handle numbers if number flag is active
        if (isNumber) {
            character = findCharacter(currentBraille, numbers);
            if (!character) {
                // If not a number, disable number mode
                isNumber = false;
                // Handle the character as a letter or punctuation
                character = findCharacter(currentBraille, alphabet);
            }
        } else {
            // Handle regular letters and punctuation
            character = findCharacter(currentBraille, alphabet);
            
        }

        // Handle capital letters
        if (isCapital && character && character.length === 1) {
            character = character.toUpperCase();
            isCapital = false;
        }

        // Append the character
        if (character) {
            result += character;
        } else {
            result += '?'; // Unknown 
        }
    }

    return result;
};

// Function to identify braille or english input
function translator(userInput){
    const isBraille = /^[O.]+$/.test(userInput);
    const isEnglish = /^[a-zA-Z0-9\s.,!?]+$/.test(userInput);
    let text;
    
    if (isBraille) {
        let sliceToSixes = splitAndJoinString(userInput);
        text = brailleToEnglish(sliceToSixes); 
        return text;
    } else if (isEnglish) {
        text = englishToBraille(userInput);
        return text;
    } else {
        return 'Unknown input';
    } 
};

// Command line argument handler
const args = process.argv.slice(2);
// Check if there are any arguments
if (args.length > 0) {
  const concatenatedString = args.join(' ');
  const cmdInput = concatenatedString;
  console.log(translator(cmdInput));
} else {
  console.log('No string provided.');
}



