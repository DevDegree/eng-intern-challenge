const translation = {
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
    'caps': '.....O',
    'decimal': '.O...O',
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
    ')': '.O.OO.',
    ' ': '......',
};

const numeric_translations = {
    'numeric': '.O.OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

// map the braille back to the english characters and numbers 
reverseTranslation = Object.fromEntries(
    Object.entries(translation).map(([key, value]) => [value, key])
);

reverseNumeric = Object.fromEntries(
    Object.entries(numeric_translations).map(([key, value]) => [value, key])
);

// used to seperate the string by sixes corresponding with braille
function getChars(braille){
    let charset = [];
    for (let i = 0; i < braille.length; i += 6) {
        charset.push(braille.slice(i, i + 6));
    }
    return charset;
}

// Determine if the string is english or braille. If the string is a multiple of six, check if the first six characters map to a braille code.
// If these are true then the string is braille. Otherwise it is english
function getLanguage(str){

    if(str.length % 6 === 0){
        let charset = getChars(str);
        if (charset[0] in reverseTranslation || charset[0] in reverseNumeric){
            return 'braille';
        }
    }

    return 'english';
}

// Utility function to check if the character is a number
function isNumber(char) {
    return !isNaN(char) && !isNaN(parseFloat(char));
}

//Main function
function translate(str)
{
    let result = '';
    let language = getLanguage(str);
    if(language === 'english'){ // english to braille
        let onNumber = false;
        for (let char of str){

             if(isNumber(char)){
                
                if(onNumber === false){
                    onNumber = true;
                    result += numeric_translations['numeric'];
                }
                
                result += numeric_translations[char];
             }else{
                onNumber = false
             }
            
            // Use regex to check if the alphabet is upper or lowercase to properly decode to braille
            if (char.match(/^[a-z ]$/)){
                // get the corresponsing braille
                result += translation[char]
            }else if (char.match(/^[A-Z]$/)){
                result += translation['caps'];
                char = char.toLowerCase();
                result += translation[char];
            }
            
        }
    }else{ // braille to english
        let result = '';
        let charset = getChars(str);
        let onNumber = false;
        let numFollows = false;
        let capOn = false;

        for (let braille of charset){
            // We first check if we are expecting letters(using caps) or numbers as some numbers and letters overlap in braille code
            if (braille in reverseTranslation && reverseTranslation[braille] === 'caps'){
                capOn = true;
                continue;
            }else if (braille in reverseNumeric && capOn === false){
                onNumber = true;
                if (reverseNumeric[braille] === 'numeric'){
                    numFollows = true;
                    continue;
                }
            }else if(braille in reverseTranslation && reverseTranslation[braille] === ' '){
                onNumber = false;
                numFollows = false;
            }

            if (onNumber && numFollows){
                result += reverseNumeric[braille];
            }else{
                if(capOn){
                    result += reverseTranslation[braille].toUpperCase();
                    capOn = false;
                }else{
                    result += reverseTranslation[braille];
                }
            }
        }
        return result;
    }
    return result;
}

module.exports = {translate};

if (require.main === module) {
    const args = process.argv.slice(2).join(' ');
    console.log(translate(args));
}

