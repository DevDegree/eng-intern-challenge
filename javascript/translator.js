
// Map with English as keys and corresponding Braille values
const alphaEnglishKeys = new Map([
    ['a', 'O.....'], ['b', 'O.O...'], ['c', 'OO....'], ['d', 'OO.O..'], ['e', 'O..O..'],
    ['f', 'OOO...'], ['g', 'OOOO..'], ['h', 'O.OO..'], ['i', '.OO...'], ['j', '.OOO..'],
    ['k', 'O...O.'], ['l', 'O.O.O.'], ['m', 'OO..O.'], ['n', 'OO.OO.'], ['o', 'O..OO.'],
    ['p', 'OOO.O.'], ['q', 'OOOOO.'], ['r', 'O.OOO.'], ['s', '.OO.O.'], ['t', '.OOOO.'],
    ['u', 'O...OO'], ['v', 'O.O.OO'], ['w', '.OOO.O'], ['x', 'OO..OO'], ['y', 'OO.OOO'],
    ['z', 'O..OOO'], [' ', '......'], ['capitalF', '.....O'], ['numberF', '.O.OOO']
]);


// Map for numbers containing English as keys and corresponding Braille values
const numEnglishKeys = new Map([
    ['1', 'O.....'], 
    ['2', 'O.O...'], 
    ['3', 'OO....'], 
    ['4', 'OO.O..'],
    ['5', 'O..O..'], 
    ['6', 'OOO...'], 
    ['7', 'OOOO..'], 
    ['8', 'O.OO..'], 
    ['9', '.OO...'],
    ['0', '.OOO..'],
]);

// Maps with Braille as keys and corresponding English character (swapped value <--> keys in previous maps)

const alphaBrailleKeys = new Map ( Array.from(alphaEnglishKeys, ([key, value]) => [value, key]) ) 

const numBrailleKeys = new Map ( Array.from(numEnglishKeys, ([key, value]) => [value, key]));

/* This function determines if given string is either in English or Braille */
function getInputType(str){
    if (str.length % 6 === 0 && containsOnlyBraille(str)) 
        {
        return 'braille';
        } 
    else 
        {
        return 'english';
        }
}

/* This function determines if all characters in given string is composed of only a series of 'O' and '.'  */
function containsOnlyBraille(str) {
    for (let i = 0; i < input.length; i++) {
        if (str[i] !== 'O' && str[i] !== '.') 
            {
            return false;
            }
    }
    return true;
}
/* This function converts a given string from Braille to English */
function brailleToEnglish(str) {
    let capitalActive = false;
    let numberActive = false;
    let final= ''
    
    for(let i = 0 ; i < str.length ; i+=6){
        let currentChar = str.slice(i,i+6);
        if (currentChar === alphaEnglishKeys.get('capitalF') ) {
            capitalActive = true;
        } else if(currentChar === alphaEnglishKeys.get('numberF'))
        {
            numberActive = true;
        } else if(currentChar === alphaEnglishKeys.get(' ') && numberActive)
        {
            numberActive = false; 
            final += ' ';
        }

        else 
        {
            let englishCurrentChar = alphaBrailleKeys.get(currentChar);
            if (numberActive) 
                {
                    
                    englishCurrentChar = numBrailleKeys.get(currentChar);
                
            }

            if (capitalActive) 
                {
                englishCurrentChar = englishCurrentChar.toUpperCase();
                capitalActive = false; 
            }

            final += englishCurrentChar;
        }
    }

    console.log(final)
    
}
/* This function converts a given string from English to Braille */
function englishToBraille(str) {
    let final = '';
    let numberActive = false;
    for(let i = 0; i < str.length ; i++){
        let currentEnglishChar = str.charAt(i);
        if(currentEnglishChar === currentEnglishChar.toUpperCase() && currentEnglishChar !== ' ' && ! (currentEnglishChar >= '0' && currentEnglishChar <= '9'))
        {
            final += alphaEnglishKeys.get('capitalF') + alphaEnglishKeys.get(currentEnglishChar.toLowerCase());
        } else if (currentEnglishChar >= '0' && currentEnglishChar <= '9'){
            if(!numberActive)
            {
                numberActive = true;
                final += alphaEnglishKeys.get('numberF') + numEnglishKeys.get(currentEnglishChar);
                continue;
            }
            final += numEnglishKeys.get(currentEnglishChar);
        } else {
            if(currentEnglishChar === ' ' && numberActive){
                numberActive = false;
            }
            final += alphaEnglishKeys.get(currentEnglishChar);
        }

    }

    console.log(final);
    
}


/* This function serves as the main program by identifying the input type then translates the string from either Braille -> English or English -> Braille */

function runTranslator(str){
    let inputType = getInputType(str);
    switch (inputType) {
        case 'braille':
            brailleToEnglish(str);

            break;

        case 'english':
            englishToBraille(str);
            break;
    
        default:
            break;
    }
    
};

process.argv.shift()
process.argv.shift()
input = process.argv.join(" ")
runTranslator(input)


