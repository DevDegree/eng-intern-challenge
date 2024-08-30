const brailleMap = {
    'a': 'O.....', 'A': '.....OO.....',
    'b': 'O.O...', 'B': '.....OO.O...',
    'c': 'OO....', 'C': '.....OOO....',
    'd': 'OO.O..', 'D': '.....OOO.O..',
    'e': 'O..O..', 'E': '.....OO..O..',
    'f': 'OOO...', 'F': '.....OOOO...',
    'g': 'OOOO..', 'G': '.....OOOOO..',
    'h': 'O.OO..', 'H': '.....OO.OO..',
    'i': '.OO...', 'I': '.....O.OO...',
    'j': '.OOO..', 'J': '.....O.OOO..',
    'k': 'O...O.', 'K': '.....OO...O.',
    'l': 'O.O.O.', 'L': '.....OO.O.O.',
    'm': 'OO..O.', 'M': '.....OOO..O.',
    'n': 'OO.OO.', 'N': '.....OOO.OO.',
    'o': 'O..OO.', 'O': '.....OO..OO.',
    'p': 'OOO.O.', 'P': '.....OOOO.O.',
    'q': 'OOOOO.', 'Q': '.....OOOOOO.',
    'r': 'O.OOO.', 'R': '.....OO.OOO.',
    's': '.OO.O.', 'S': '.....O.OO.O.',
    't': '.OOOO.', 'T': '.....O.OOOO.',
    'u': 'O...OO', 'U': '.....OO...OO',
    'v': 'O.O.OO', 'V': '.....OO.O.OO',
    'w': '.OOO.O', 'W': '.....O.OOO.O',
    'x': 'OO..OO', 'X': '.....OOO..OO',
    'y': 'OO.OOO', 'Y': '.....OOO.OOO',
    'z': 'O..OOO', 'Z': '.....OO..OOO',
    ' ': '......', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...',
};

const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([k, v]) => [v, k])
);

const alphabetToNumberMap = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0',
}

const isBraille = (input) => {
    // Check if the input consists entirely of "O" and "." characters and its length is a multiple of 6
    return /^[O.]+$/.test(input);
}

const translator = (input) => {
    if (isBraille(input)) {
        console.log(input);
        return translateToEnglish(input);
    } else {
        console.log(input);
        return translateToBraille(input);
    }
}

const translateToEnglish = (input) => {
    let res = '';
    let i = 0;
    let isNumber = false;
    while(i < input.length){
        let currBraille = input.slice(i, i+6);
        let currEnglish = reverseBrailleMap[currBraille];
        if(currBraille === '.O.OOO'){
            isNumber = true;
            i += 6;
            continue;
        }

        if(currBraille === '.....O'){
            let capBraille = input.slice(i, i + 12);
            if(reverseBrailleMap[capBraille]){
                console.log(capBraille + " -> " + reverseBrailleMap[capBraille]);
                res += reverseBrailleMap[capBraille];
                i += 12;
                continue;
            }
        }
        console.log(currBraille + " -> " + currEnglish);

        if(currBraille === '......'){
            res += currEnglish;
            isNumber = false;
            i +=6;
            continue;
        }
        if(isNumber && currEnglish >= 'a' && currEnglish <= 'j'){
            res += alphabetToNumberMap[currEnglish];
            i += 6;
            continue;
        }
        res += currEnglish;
        i += 6;
    }
    return res;
}

const translateToBraille = (input) => {
    let res = "";
    let isNumber = false;
    for(let char of input){
        if(char === ' '){
            isNumber = false;
        }
        else if(!isNaN(char) && !isNumber){
            res += '.O.OOO';
            isNumber = true;
        }else if(isNaN(char)){
            isNumber = false;
        }
        res += brailleMap[char];
    }
    return res;
}
const input = process.argv.slice(2).join(' ');
console.log(translator(input));