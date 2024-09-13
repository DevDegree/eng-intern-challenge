// The character mappings from English to Braille.
const brailleLetters = {
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
}

//Baille Numbers
const brailleNumbers = {
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
};

//Special braille characters
const brailleSpecial = {
    space: '......', 
    capital: '.....O',
    number: '.O.OOO',
    decimal: '.O...O',  
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
};

//function to flip a maps keys and values.
const flip = (data) => {
    return Object.entries(data).map(([key, value]) => [value, key]);
}

//Flip all three mappings above.
const flippedBrailleLetters = flip(brailleLetters);
const flippedBrailleNumbers = flip(brailleNumbers);
const flippedBrailleSpecial = flip(brailleSpecial);

//Check if the sequence is braille
const isBraille = (str) => {
    return /^[O.]+$/.test(input);
}

//Translate English to Braille
//reversing the mappings should have been done first but doesnt make a difference in the end
const englishToBraille = (eng) => {
    let result = '';
    let numberSequence = false; //boolean to see if its a number sequence

    //Loop through each char of 'str' and perform a check to see which mappings are appropriate.
    for(let char of eng) {
        if(char === ' ') { // for spaces ' '.
            result += brailleSpecial.space; 
        } else if (/[A-Z]/.test(char)) { //check if it is an uppercase, add the prefix and character
            result += brailleSpecial.capital + brailleLetters[char.toLowerCase()];
        } else if (/[a-z]/.test(char)) { // For lowercase letters
            result += brailleLetters[char];
        } else if(/[1-9]/.test(char)) {
            if(!numberSequence) { // if it isnt a number make it a number
                result += brailleSpecial.number; //prefix
                numberSequence = true;
            }
            result += brailleNumbers[char]; // append the character
        } else if(brailleSpecial[char]) { // Existance check 
            result += brailleSpecial[char];
            numberSequence = false; //Exit after you see 
        }
    }

    return result.trim(); // Make sure the output is a clean string.
}



const brailleToEnglish = (braille) => {
    let result = '';
    let capitalSequence = false; // For handling Capital sequences
    let numberSequence = false; // for handling number like before

    // Trim and remove any extra spaces between symbols
    braille = braille.replace(/\s+/g, '').trim();

    for(let i = 0; i < braille.length; i+=6) { //in chunks of 6
        const symbol = braille.substr(i,i + 6); // The full 6 digit braille character

        // Check if it is a number sequence.
        if(symbol === brailleSpecial.number) {
            numberSequence = true; // In number sequence mode!
            continue; //Go to next iteration and see what the next character is
        }

        // Check if it is Capital letter
        if(symbol === brailleSpecial.capital){
            capitalSequence = true; // Captial sequence activated.
            continue;
        }

        // Check for space character.
        if(symbol === brailleSpecial.space) {
            result += ' '; // Add space
            capitalSequence = false;
            numberSequence = false; // Turn off both sequences as space will end a sequence.
        }

        let translated; //A character that can potentially be translated from the 3 mappings.
        
        // If we are in a number sequence.
        if(isNumber) {
            translated = flippedBrailleNumbers[symbol];
            if(translated){ //To check for undefines or valid translations
                result += translated;
                continue; // Go out of the loop and check for next symbol.
            }
        }

        // if it is still capitalizing
        if (isCapital && translated) {
            translated = translated.toUpperCase();
            isCapital = false; 
        }

        // if it isnt translated it must be a special character
        if (!translated) {
            translated = flippedBrailleSpecial[symbol];
        }

        // For undefined entries 
        if (!translated) {
            console.error(`Unrecognized Braille symbol: '${symbol}'`);
            continue;
        }

        result += translated; //When the dust settles append the translated character!
        
    }

    return result; // output
}

//Put it all together in a 'main' function 'translate';
const translate = (input) => {
    if(isBraille(input)) {
        return brlToEng(input);
    } else {
        return engToBrl(input);
    }
}

if (require.main === module) {
    const input = process.argv.slice(2).join(' ');  // Get the command-line arguments (Abc 123 xYz)
    const result = translate(input);  
    console.log(result);  
}

