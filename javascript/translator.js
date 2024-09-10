const capitalFollows = '.....0';
const decimalFollows = '.0...0';
const numberFollows = '.0.000';
const space = '......';

const brailleAlpha = {
    '0.....': 'a', '0.0...': 'b', '00....': 'c', '00.0..': 'd', '0..0..': 'e', '000...': 'f', '0000..': 'g',
    '0.00..': 'h', '.00...': 'i', '.000..': 'j', '0...0.': 'k', '0.0.0.': 'l', '00..0.': 'm', '00.00.': 'n',
    '0..00.': 'o', '000.0.': 'p', '00000.': 'q', '0.000.': 'r', '.00.0.': 's', '.0000.': 't', '0...00': 'u',
    '0.0.00': 'v', '.000.0': 'w', '00..00': 'x', '00.000': 'y', '0..000': 'z'
};

const brailleNumeric = {
    '0.....': 1, '0.0...': 2, '00....': 3, '00.0..': 4, '0..0..': 5,
    '000...': 6, '0000..': 7, '0.00..': 8, '.00...': 9, '.000..': 0
};

const brailleCharacters = {
    '..00.0': '.', '..0...': ',', '..0.00': '?', '..00.0': '!', '..00..': ':', '..0.0.': ';',
     '....00': '-', '.0..0.': '/', '.00..0': '<', '0..00.': '>', '0.0..0': '(', '.0.00.': ')'
};

(() => {
    if(process.argv.length <= 2){
        console.log('');
        return;
    }
    const toElements = process.argv.toSpliced(0, 2).join(' ').split('');
    const isBraille = (toElements.length % 6 === 0) && toElements.every(element => element === '.' || element === "0");
    if(isBraille){
        const toString = toElements.join('');
        const toSplit = toString.match(/.{6}/g);
        const translationObject = toSplit.reduce((accumulator, currentValue) => {
            const temp = {...accumulator};
            temp.output += brailleAlpha[currentValue];
            return temp;
        }, {
            output: '',
            isNumber: false,
            isCapital: false
        });

        console.log(translationObject.output);
    }
})();