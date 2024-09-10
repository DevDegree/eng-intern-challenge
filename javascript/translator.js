const capitalFollows = '.....0';
const decimalFollows = '.0...0';
const numberFollows = '.0.000';

const brailleCharacters = {
    
}

(() => {
    if(process.argv.length <= 2){
        console.log('');
        return;
    }
    const toElements = process.argv.toSpliced(0, 2).join(' ').split('');
    const isBraille = (toElements.length % 6 === 0) && toElements.every(element => element === '.' || element === "0");
    if(isBraille){

    }
})();