const capitalFollows = '.....O';
const decimalFollows = '.O...O';
const numberFollows = '.O.OOO';
const space = '......';

const brailleAlpha = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g',
    'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n',
    'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z'
};

const brailleNumeric = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
};

const brailleCharacters = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OO.O': '!', '..OO..': ':', '..O.O.': ';',
     '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
};

(() => {
    if(process.argv.length <= 2){
        console.log('');
        return;
    }
    const toElements = process.argv.toSpliced(0, 2).join(' ').split('');
    const isBraille = (toElements.length % 6 === 0) && toElements.every(element => element === '.' || element === "O");
    if(isBraille){
        const toString = toElements.join('');
        const toSplit = toString.match(/.{6}/g);
        const translationObject = toSplit.reduce((accumulator, currentValue) => {
            const temp = {...accumulator};
            if(currentValue === space){
                temp.isNumber = false;
                temp.isCapital = false;
                temp.isDecimal = false;
                temp.output += ' ';
            }
            else if(currentValue === capitalFollows){
                temp.isCapital = true;
                temp.isNumber = false;
                temp.isDecimal = false;
            }
            else if(currentValue === decimalFollows){
                temp.isDecimal = true;
                temp.isCapital = false;
            }
            else if(currentValue === numberFollows){
                temp.isCapital = false;
                temp.isDecimal = false;
                temp.isNumber = true;
            }
            else{
                if(temp.isCapital){
                    temp.output += brailleAlpha[currentValue]?.toUpperCase() || brailleCharacters[currentValue] || `(${currentValue} is not in Braille)`;
                    temp.isCapital = false;
                }
                else if(temp.isNumber){
                    temp.output += brailleNumeric[currentValue] || brailleAlpha[currentValue] || brailleCharacters[currentValue] || `(${currentValue} is not in Braille)`
                }
                else{
                    temp.output += brailleAlpha[currentValue] || brailleCharacters[currentValue] || `(${currentValue} is not in Braille)`;
                }
            }
            return temp;
        }, {
            output: '',
            isNumber: false,
            isCapital: false,
            isDecimal: false
        });
        console.log(translationObject.output);
    }
    else{
        const toEnglish = toElements.reduce((accumulator, currentValue, index) => {
            if(currentValue.charCodeAt(0) >= 65 && currentValue.charCodeAt(0) <= 90){
                accumulator.output += `${capitalFollows}${Object.keys(brailleAlpha).find(key => brailleAlpha[key] === currentValue.toLowerCase())}`;
            }
            else if(currentValue.charCodeAt(0) >= 48 && currentValue.charCodeAt(0) <= 57){
                if(accumulator.isNumber){
                    accumulator.output += `${Object.keys(brailleNumeric).find(key => brailleNumeric[key] === currentValue) 
                        || Object.keys(brailleAlpha).find(key => brailleAlpha[key] === currentValue)
                        || Object.keys(brailleCharacters).find(key => brailleCharacters[key] === currentValue) 
                        || `(${currentValue}  has no Braille equivalent)`}`;
                }
                else{
                    accumulator.isNumber = true;
                    accumulator.output += `${numberFollows}${Object.keys(brailleNumeric).find(key => brailleNumeric[key] === currentValue) 
                        || Object.keys(brailleAlpha).find(key => brailleAlpha[key] === currentValue)
                        || Object.keys(brailleCharacters).find(key => brailleCharacters[key] === currentValue) 
                        || `(${currentValue}  has no Braille equivalent)`}`;
                }
            }
            else if(currentValue === ' '){
                accumulator.output += space;
                accumulator.isNumber = false

            }
            else{
                accumulator.output += Object.keys(brailleAlpha).find(key => brailleAlpha[key] === currentValue);
            }
            return accumulator;
        }, {
            output: '',
            isNumber: false
        });
        console.log(toEnglish.output);
    }
})();