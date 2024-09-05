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

const brailleToEnglish = (val) => {
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

const englishToBraille = (val) => {
    let output = '';
    let valArr = val.split('')
    let inputArr = [];
    let capitalize = false;
    let number = false;
    let decimal = false;

    for(let i = 0; i < valArr.length; i += 6){
        let chunk = valArr.slice(i, i + 6);
        inputArr.push(chunk.join(''));
    }

    console.log(inputArr)

    for(let m = 0; m < inputArr.length; m++){
        for(const key in brailleAlphabet){
            if(brailleAlphabet[key] == inputArr[m]){
                if(capitalize){
                    output += key.toUpperCase();
                    capitalize = false;
                }else if(number){
                    
                }

                if(key == 'capital'){
                    capitalize = true;
                }else if(key == 'number'){
                    number = true;
                }else if(key == 'decimal'){
                    decimal = true;
                }
            }
        }
    }
}

if(inputString){
    let output;

    output = englishToBraille(inputString)
    // console.log(output)

    // if(output == 'Abc 123'){
    //     console.log('passed')
    // }
    
    // output = brailleToEnglish(inputString)
    // console.log(output)

    // if(output == '.O.OOOOO.O..O.O...'){
    //     console.log('passed')
    // }
}