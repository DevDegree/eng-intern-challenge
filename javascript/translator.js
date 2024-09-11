const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',

    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......',
};

const brailleNumDict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
}

const englishDict = Object.fromEntries(
    Object.entries(brailleDict).map(([key, val]) => [val, key]),
);

const englishNumDict = Object.fromEntries(
    Object.entries(brailleNumDict).map(([key, val]) => [val, key]),
);


const brailleToEnglish = (userInput) => {
    let output = '';
    let capitalize = false;
    let isNumber = false;

    try {
        for (let i = 0; i < userInput.length; i += 6){
            const brailleChar = userInput.slice(i, i + 6);
            
            if (englishDict.hasOwnProperty(brailleChar)){
                const englishChar = englishDict[brailleChar];

                if (englishChar === 'capital_follows'){
                    capitalize = true;
                } else if (englishChar === 'number_follows'){
                    isNumber = true;
                } else if (englishChar === ' '){
                    output += englishChar;
                    isNumber = false;
                } else{

                    if (isNumber){
                        if(englishNumDict.hasOwnProperty(brailleChar)){
                            output += englishNumDict[brailleChar]
                        }
                    } else {
                        output += capitalize ? englishChar.toUpperCase() : englishChar;
                        capitalize = false;
                    }
                }
            }
            else {
                output += 'unknown input'
            }
        }
    } catch (error) {
        console.error(error);
    }

    return output === '' ? 'invalid input' : output;


};

const englishToBraille = (userInput) => {
    let output = '';
    let isNumberSequence = false;
    const capitalChar = brailleDict['capital_follows'];
    const numberChar = brailleDict['number_follows'];

    try {
        for (let i = 0; i < userInput.length; i++){
            const englishChar = userInput.slice(i, i + 1);
            const lowerCaseEnglishChar = englishChar.toLowerCase();

            if (brailleDict.hasOwnProperty(lowerCaseEnglishChar) || brailleNumDict.hasOwnProperty(englishChar)){

                if (/^[A-Z]$/.test(englishChar)){
                    output += capitalChar;
                    output += brailleDict[lowerCaseEnglishChar];
                } else if (/^[0-9]$/.test(englishChar)){
                    if (!isNumberSequence){
                        output += numberChar;
                        isNumberSequence = true;
                    }
                    output += brailleNumDict[englishChar];

                } else if (lowerCaseEnglishChar === ' '){
                        output += brailleDict[lowerCaseEnglishChar];
                        isNumberSequence = false;
                } else {
                    output += brailleDict[lowerCaseEnglishChar];
                
                }

            }
            else {
                output += 'unknown input'
            }
        }
    } catch (error) {
        console.error(error);
    }

    return output === '' ? 'invalid input' : output;


};


const translator = () => {

    let output = null;
    const userInput = process.argv.slice(2).join(' ');
    const isBraille = /^[O.]+$/.test(userInput);

    if (isBraille){
        output = brailleToEnglish(userInput);
        console.log(output);
    } else {
        output = englishToBraille(userInput);
        console.log(output);
    }

};

translator();