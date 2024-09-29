const { translation, numbers, especialCharacters, valuesArray } = require('./letters.js');
const { isLetter, isUpper, isNumber } = require('./utilities.js');

const input  = process.argv.slice(2);
const inputArray = input.join(' ').split('');

const letter = array => {
    return array.map((item, i) => {
        if (isLetter(item)) {
            if (isUpper(item)) {
                return translation.capitalLetterSign + translation[item];
            } else {
                return translation[item.toUpperCase()];
            }
        } else if (isNumber(item)) {
            if (isNumber(inputArray[i - 1])) {
                return numbers[item];
            } else {
                return translation.numberSign + numbers[item];
            }
        } else if (valuesArray.some(char => char === item)){
            const keyChar = especialCharacters[valuesArray.find(char => char === item)];
            return translation[keyChar];
        }
    });
}

const braille = () => {
    const newInputArray = input.join('').match(/.{1,6}/g);
    const values = Object.values(translation);
    const keys = Object.keys(translation);
    const specialValues = Object.values(especialCharacters);
    const specialKeys = Object.keys(especialCharacters);
    let capitalLetter = false;
    let number = false;

    return newInputArray.map(item => {
        const indexKey = values.lastIndexOf(item);
        if (keys[indexKey] === 'capitalLetterSign') {
            capitalLetter = true;
            number = false;
            return '';
        }
        if (keys[indexKey] === 'numberSign') {
            number = true;
            capitalLetter = false;
            return '';
        }
        if (specialValues.some(char => char === keys[indexKey])) {
            const indexSpecial = specialValues.indexOf(keys[indexKey]);
            number = false;
            capitalLetter = false;
            return specialKeys[indexSpecial];
        }
        if (capitalLetter) {
            capitalLetter = false;
            number = false;
            return keys[indexKey];
        }

        if (number) {
            if (item === '.OO...') {
                return 0;
            }
            return indexKey + 1;
        }
        return keys[indexKey].toLowerCase();
    });
}

if (inputArray.some(item => item !== 'O' && item !== '.')) {
    console.log(letter(inputArray).join(''));
} else {
    console.log(braille().join(''));
}
