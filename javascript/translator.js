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

const englishToBraille = (val) => {
    let output = '';

    let inputArr = val.split('');
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

const brailleToEnglish = (val) => {
    let output = '';
    let valArr = val.split('')
    let inputArr = [];
    let capitalize = false;
    let number = false;
    let decimal = false;
    let addToOutput = false;

    for(let i = 0; i < valArr.length; i += 6){
        let chunk = valArr.slice(i, i + 6);
        inputArr.push(chunk.join(''));
    }

    for(let m = 0; m < inputArr.length; m++){
        for(const key in brailleAlphabet){
            if(brailleAlphabet[key] == inputArr[m]){

                if(key == 'number'){
                    number = true;
                }else if(key == 'decimal'){
                    decimal = true;
                }else if(key == 'capital'){
                    capitalize = true;
                }else{
                    addToOutput = true;
                }

                if(addToOutput){
                    if(number || decimal){
                        if(isNumber(key) || isDecimal(key)){
                            output += key;
                        }

                        if(number){
                            if(m+1 < inputArr.length && isNumber(brailleAlphabet[inputArr[m+1]])){
                                number = false;
                            }
                        }

                        if(decimal){
                            if(m+1 < inputArr.length && isDecimal(brailleAlphabet[inputArr[m+1]])){
                                decimal = false;
                            }
                        }
                    }else{
                        if(!isNumber(key) && !isDecimal(key)){
                            if(capitalize){
                                output += key.toUpperCase();
                                capitalize = false;
                            }else{
                                output += key;
                            }
                        }
                    }
                    addToOutput = false;
                }
            }
        }
    }
    return output;
}

if(inputString){
    let output;
    let filteredAlphabet = Object.keys(brailleAlphabet).filter(ele => !['capital', 'decimal', 'number', 'o', '.'].includes(ele));
    let englishDetected = false;

    filteredAlphabet.forEach(ele => {
        if(inputString.toLocaleLowerCase().trim().includes(ele)){
            englishDetected = true;
        }
    })

    if(englishDetected){
        output = englishToBraille(inputString)
        englishDetected = false;
    }else{
        output = brailleToEnglish(inputString)
    }


    console.log(output)

}