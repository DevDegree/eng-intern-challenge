let charToBraille_Map = new Map([
    ['a', 'O.....'],
    ['b', 'O.O...'],
    ['c', 'OO....'],
    ['d', 'OO.O..'],
    ['e', 'O..O..'],
    ['f', 'OOO...'],
    ['g', 'OOOO..'],
    ['h', 'O.OO..'],
    ['i', '.OO...'],
    ['j', '.OOO..'],
    ['k', 'O...O.'],
    ['l', 'O.O.O.'],
    ['m', 'OO..O.'],
    ['n', 'OO.OO.'],
    ['o', 'O..OO.'],
    ['p', 'OOO.O.'], 
    ['q', 'OOOOO.'], 
    ['r', 'O.OOO.'], 
    ['s', '.OO.O.'], 
    ['t', '.OOOO.'],
    ['u', 'O...OO'], 
    ['v', 'O.O.OO'], 
    ['w', '.OOO.O'], 
    ['x', 'OO..OO'], 
    ['y', 'OO.OOO'],
    ['z', 'O..OOO'], 
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
    ['space', '......'],
    ['capital', '.....O'],
    ['number', '.O.OOO'],
]);

let brailleToChar_Map = new Map([
    ['O.....', 'a'], 
    ['O.O...', 'b'], 
    ['OO....', 'c'], 
    ['OO.O..', 'd'], 
    ['O..O..', 'e'],
    ['OOO...', 'f'], 
    ['OOOO..', 'g'], 
    ['O.OO..', 'h'], 
    ['.OO...', 'i'], 
    ['.OOO..', 'j'],
    ['O...O.', 'k'], 
    ['O.O.O.', 'l'], 
    ['OO..O.', 'm'], 
    ['OO.OO.', 'n'], 
    ['O..OO.', 'o'],
    ['OOO.O.', 'p'], 
    ['OOOOO.', 'q'], 
    ['O.OOO.', 'r'], 
    ['.OO.O.', 's'], 
    ['.OOOO.', 't'],
    ['O...OO', 'u'], 
    ['O.O.OO', 'v'], 
    ['.OOO.O', 'w'], 
    ['OO..OO', 'x'], 
    ['OO.OOO', 'y'],
    ['O..OOO', 'z'], 
    ['......', 'space'],
    ['.....O', 'capital'],
    ['.O.OOO', 'number']
]);

let brailleToNumber_map = new Map([
    ['O.....', '1'], 
    ['O.O...', '2'], 
    ['OO....', '3'], 
    ['OO.O..', '4'], 
    ['O..O..', '5'],
    ['OOO...', '6'], 
    ['OOOO..', '7'], 
    ['O.OO..', '8'], 
    ['.OO...', '9'], 
    ['.OOO..', '0']
]);

    let isBraille = (text) => {
        //return true if input text contains only 'O' space and '.'
        return (/^[O. ]+$/.test(text));
    }

let convertToBraille = (inputText) => {
    let resultText = '';
    let isNumber = false;

    for(let char of inputText){
        //check if the current character is an alphabet letter
        if (char === ' '){
            isNumber = false;
            resultText += charToBraille_Map.get('space');
        } else if (char >= '0' && char <= '9'){
            if (!isNumber){
                resultText += charToBraille_Map.get('number');
                isNumber = true;
            }
            resultText += charToBraille_Map.get(char);
        } else {
            if (char === char.toUpperCase() && char.toLowerCase() !== char.toUpperCase()){
                resultText += charToBraille_Map.get('capital');
            }
            resultText += charToBraille_Map.get(char.toLowerCase());
        }
    }
    return resultText;
}

let convertToEnglish = (inputText) => {
    let resultText = '';
    let brailleChar = [];
    let isCapital = false;
    let isNumber = false;

    // Push every 6 brailleText as an element into array
    for (let i = 0; i < inputText.length; i += 6){
        brailleChar.push(inputText.substring(i, i + 6));
    }

    // For each one braille character, convert into an alphabet character
    for (let char of brailleChar){
        let currChar = brailleToChar_Map.get(char);

        if (currChar === 'capital'){
            isCapital=true;
            continue;
        }else if (currChar === 'number'){
            isNumber=true;
        }else if (currChar === 'space'){
            resultText += ' ';
            isNumber = false;
            continue;
        }
        if (isNumber){
            resultText += brailleToNumber_map.get(char);
        }
        if (isCapital){
            resultText += currChar.toUpperCase();
            isCapital = false;
        }else{
            resultText += currChar;
        }
    }
    return resultText;
}

let convert = (inputText) => {
    if (isBraille(inputText)){
        return convertToEnglish(inputText);
    }else{
        return convertToBraille(inputText);
    }
}

// Get params as args and convert and print
const args = process.argv.slice(2).join(' ');
console.log(convert(args));