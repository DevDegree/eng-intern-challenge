const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 

    'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',

    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......',
};

const englishDict = Object.fromEntries(
    Object.entries(brailleDict).map(([key, val]) => [val, key]),
);


const brailleToEnglish = (userInput) => {
    let output = '';
    let capitalize = false;

    try {
        for (let i = 0; i < userInput.length; i += 6){
            const brailleChar = userInput.slice(i, i + 6);
            
            if (englishDict.hasOwnProperty(brailleChar)){
                const char = englishDict[brailleChar];

                if (char === 'capital_follows'){
                    capitalize = true;
                } else{
                    output += capitalize ? char.toUpperCase() : char;
                    capitalize = false;
                }
            }
            else {
                output += 'unknown'
            }
        }
    } catch (error) {
        console.error(error);
    }

    return output === '' ? 'invalid input' : output;


};

// const englishToBraille = (userInput) => {

// };


const translator = () => {

    const userInput = process.argv.slice(2).join(' ');

    const isBraille = /^[O.]+$/.test(userInput);

    if (isBraille){
        let output = brailleToEnglish(userInput);
        console.log(output);
    }
    // } else {
    //     // englishToBraille(userInput);
        
    // }
};

translator();