const braille_dict = {
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
    'cap': '.....O',  
    'num': '.O.OOO',  
    'space': '......'  
}

const reverseBrailleDict = {
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
    '.....O': 'cap', 
    '......': ' ',   
    '.0.000': 'num'  
};

function englishToBraille(text){
    let result='';
    let isNum=false;
    for(let char of text){
        if(char===' '){
            result+=braille_dict['space'];
            isNum=false;
        }
        else if(char.toUpperCase()!==char){
            result+=braille_dict[char];
        }else if(char>='0' && char<='9'){
            if (!isNum) {
                result += braille_dict['num'];  
                isNum = true;
            }
            result += braille_dict[char];
        }
        else{
            result+=braille_dict['cap'] + braille_dict[char.toLowerCase()];
        }
    }
    return result;
}

function brailleToEnglish(braille) {
    let result='';
    let isNum=false;
    let isCap=false;
    for(let i=0;i<braille.length;i+=6){
        const char = braille.slice(i, i + 6);
        if(char===braille_dict['space']){
            result+=' ';
            isNum=false;
            isCap=false;
        }else if(char===braille_dict['cap']){
            isCap=true;
        }else if(char===braille_dict['num']){
            isNum=true;
        }else{
            let translatedChar = reverseBrailleDict[char];

            if (isNum) {
                translatedChar = convertBrailleNumberToDigit(translatedChar);
            }

            if (isCap) {
                translatedChar = translatedChar.toUpperCase();  
                isCap = false;  
            }

            result += translatedChar;
        }
        
    }
    
    return result; 
}

function convertBrailleNumberToDigit(letter) {
    const numberMapping = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    };
    return numberMapping[letter] || letter;  
}

function isBraille(text) {
    return text.length % 6 === 0 && /^[O.]+$/.test(text);
}

const input = process.argv.slice(2).join(' ');  

if (isBraille(input)) {
    console.log(brailleToEnglish(input));
} else {
    console.log(englishToBraille(input));
}

