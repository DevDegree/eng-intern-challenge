const brailleMatrix = {
    'a' : [1,0,0,0,0,0],
    'b' : [1,0,1,0,0,0],
    'c' : [1,1,0,0,0,0],
    'd' : [1,1,0,1,0,0],
    'e' : [1,0,0,1,0,0],
    'f' : [1,1,1,0,0,0],
    'g' : [1,1,1,1,0,0],
    'h' : [1,0,1,1,0,0],
    'i' : [0,1,0,1,0,0],
    'j' : [0,1,1,1,0,0],
    'k' : [1,0,0,0,1,0],
    'l' : [1,0,1,0,1,0],
    'm' : [1,1,0,0,1,0],
    'n' : [1,1,0,1,1,0],
    'o' : [1,0,0,1,1,0],
    'p' : [1,1,1,0,1,0],
    'q' : [1,1,1,1,1,0],
    'r' : [1,0,1,1,1,0],
    's' : [0,1,1,0,1,0],
    't' : [0,1,1,1,1,0],
    'u' : [1,0,0,0,1,1],
    'v' : [1,0,1,0,1,1],
    'w' : [0,1,1,1,0,1],
    'x' : [1,1,0,0,1,1],
    'y' : [1,1,0,1,1,1],
    'z' : [1,0,0,1,1,1],
    '0' : [0,1,1,1,0,0],
    '1' : [1,0,0,0,0,0],
    '2' : [1,0,1,0,0,0],
    '3' : [1,1,0,0,0,0],
    '4' : [1,1,0,1,0,0],
    '5' : [1,0,0,1,0,0],
    '6' : [1,1,1,0,0,0],
    '7' : [1,1,1,1,0,0],
    '8' : [1,0,1,1,0,0],
    '9' : [0,1,1,0,0,0],
    'uppercase' : [0,0,0,0,0,1],
    'decimal' : [0,1,0,0,0,1],
    'number' : [0,1,0,1,1,1],
    '.' : [0,0,1,1,0,1],
    ',' : [0,0,1,0,0,0],
    '?' : [0,0,1,1,1,0],
    '!' : [0,0,1,1,0,0],
    ':' : [0,0,1,1,0,0],
    ';' : [0,0,1,0,1,0],
    '-' : [0,0,0,0,1,1],
    '/' : [0,1,0,0,1,0],
    '<' : [0,1,1,0,0,1],
    '>' : [1,0,0,1,1,0],
    '(' : [1,0,1,0,0,1],
    ')' : [0,1,0,1,1,0],
    'space' : [0,0,0,0,0,0],
}

function transformeBinaryIntoBraille(matrix) {
    let string = '';
    for (let i = 0 ; i <6 ; i ++) {
        if (matrix[i] == 0 ) {
            string += '.';
        }else {
            string += 'O';
        }
    }
    return string;
}

function transformeStringIntoBraille(inputString) {
    string = "";
    next = "";
    for (let i = 0 ; i < inputString.length ; i ++) {
        let char = inputString[i];

        if (char === ' ') {
            numberString = false;
            next = transformeBinaryIntoBraille(brailleMatrix['space']);
            string += next;
        } else if (isNaN(char)) {
            if (char == char.toUpperCase()) {
                next = transformeBinaryIntoBraille(brailleMatrix['uppercase'])
                string+=next;
                next = transformeBinaryIntoBraille(brailleMatrix[char.toLowerCase()]);
                string += next;
            }else {
                next = transformeBinaryIntoBraille(brailleMatrix[char]);
                string += next;
            }
        }else {
            if (!numberString) {
                next = transformeBinaryIntoBraille(brailleMatrix['number']);
                string += next;
                numberString = true;
            }
            next = transformeBinaryIntoBraille(brailleMatrix[char]);
            string += next;
        }
    }
    console.log(string);
    return (string);

}

function transformeBrailleIntoBinary (brail) {
    let array = [];
    for (let i = 0 ; i<6; i ++) {
        if (brail[i] == '.') {
            array.push(0);
        }else {
            array.push(1)
        }
    }
    return array;

}

function findCharByBinary(char, numberString = false) {
    if (numberString) {
        const numberKey = Object.keys(brailleMatrix).find(e => brailleMatrix[e].join('') === char.join('') && '0123456789'.includes(e));
        return numberKey;
    } else {
        const letterKey = Object.keys(brailleMatrix).find(e => brailleMatrix[e].join('') === char.join('') && !'0123456789'.includes(e));
        return letterKey;
    }
}


function transformeBrailleIntoString(array) {
    let string = '';
    let numberString = false;
    let uppercaseNext = false;

    for (let i = 0 ; i < array.length; i ++) {
        let binaryArray = transformeBrailleIntoBinary(array[i])
        let char = binaryArray;

        if (char.join('') === brailleMatrix['number'].join('')) {
            numberString = true;
        } else if (char.join('') === brailleMatrix['space'].join('')) {
            string += ' ';
            numberString = false;
        } else if (char.join('') === brailleMatrix['uppercase'].join('')) {
            uppercaseNext = true;
        } else {
            let foundChar = findCharByBinary(char, numberString);
            if (uppercaseNext) {
                string +=foundChar.toUpperCase();
                uppercaseNext = false;
            } else {
                string+= foundChar;
            }
        }
    }
    console.log(string);
    return string;
}

function isInputBraille(input) {
    if (Array.isArray(input) && !(input.length < 6)) {
        return input.every(row => row.every(char => char === '.' || char === 'O'));
    }
    return false;
}

function processInput(input) {
    if (isInputBraille(input)) {
        return transformeBrailleIntoString(input);
    }else {
        return transformeStringIntoBraille(input);
    }
}


// let input = ("Hello world");
// let input2 = ("42");
// let brailInput = [
//     ['.','O','.','O','O','O'],
//     ['O','.','.','.','.','.'],
//     ['O','.','O','.','.','.'],
//     ['.','.','.','.','.','.'],
//     ['.','.','.','.','.','O'],
//     ['O','.','.','.','.','.'],
//     ['O','.','.','.','.','.']
// ]

let input = process.argv.slice(2).join(' ');



processInput(input);