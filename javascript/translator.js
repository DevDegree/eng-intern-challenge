const brailleAlphabet = {
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
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
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

const input = process.argv.slice(2);
const inputString = input.join(' ');

const isNumber = (val) => {
    return !isNaN(parseInt(val)) && isFinite(val)
}

const isDecimal = (val) => {
    return !isNaN(parseFloat(val)) && isFinite(val)
}

const brailToEnglish = (val) => {
    let output = '';

    let inputArr = val.split('');
    console.log(inputArr);

    for(let i = 0; i < inputArr.length; i++){
        //if the letter is uppercase
        if(inputArr[i] == inputArr[i].toUpperCase() && inputArr[i] != ' ' && /^[a-zA-Z]+$/.test(inputArr[i])){
            output += brailleAlphabet['capital'];
        }
        //if the letter is a number
        else if(isNumber(inputArr[i])){
            if(i == 0 || (i-1 > 0 && !isNumber(inputArr[i-1]))){
                output += brailleAlphabet['number']
            }
        }
        //if the letter is a decimal
        else if(isDecimal(inputArr[i])){
            if(i == 0 || (i-1 >= 0 && !isDecimal(inputArr[i-1]))){
                output += brailleAlphabet['decimal']
            }
        }

        output += brailleAlphabet[inputArr[i].toLowerCase()]
    }
    return output
}


if(inputString){
    let output;

    output = brailToEnglish(inputString)
    console.log(output)

    if(output == 'Abc 123'){
        console.log('passed')
    }
    
    // output = brailToEnglish(inputString)
    // console.log(output)

    // if(output == '.O.OOOOO.O..O.O...'){
    //     console.log('passed')
    // }
}