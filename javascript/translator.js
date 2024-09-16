//made the Bidirectional map to speed up letter lookup
class BiDirectionalMap {
    constructor() {
        this.keyToValue = new Map();
        this.valueToKey = new Map();
    }

    set(key, value) {
        if (this.keyToValue.has(key) || this.valueToKey.has(value)) {
            throw new Error('Already exists');
        }
        this.keyToValue.set(key, value);
        this.valueToKey.set(value, key);
    }
    getValue(key) {
        return this.keyToValue.get(key);
    }
    getKey(value) {
        return this.valueToKey.get(value);
    }
}

const brailleToEnglishMap = new BiDirectionalMap();
const brailleToNumberMap = new BiDirectionalMap();

brailleToEnglishMap.set('.....O', '*') //Capital follows
brailleToEnglishMap.set('.O...O', '**') //Decimal follows
brailleToEnglishMap.set('.O.OOO', '***') //Number follows
brailleToEnglishMap.set('O.....', 'a')
brailleToEnglishMap.set('O.O...', 'b')
brailleToEnglishMap.set('OO....', 'c')
brailleToEnglishMap.set('OO.O..', 'd')
brailleToEnglishMap.set('O..O..', 'e')
brailleToEnglishMap.set('OOO...', 'f')
brailleToEnglishMap.set('OOOO..', 'g')
brailleToEnglishMap.set('O.OO..', 'h')
brailleToEnglishMap.set('.OO...', 'i')
brailleToEnglishMap.set('.OOO..', 'j')
brailleToEnglishMap.set('O...O.', 'k')
brailleToEnglishMap.set('O.O.O.', 'l')
brailleToEnglishMap.set('OO..O.', 'm')
brailleToEnglishMap.set('OO.OO.', 'n')
brailleToEnglishMap.set('O..OO.', 'o')
brailleToEnglishMap.set('OOO.O.', 'p')
brailleToEnglishMap.set('OOOOO.', 'q')
brailleToEnglishMap.set('O.OOO.', 'r')
brailleToEnglishMap.set('.OO.O.', 's')
brailleToEnglishMap.set('.OOOO.', 't')
brailleToEnglishMap.set('O...OO', 'u')
brailleToEnglishMap.set('O.O.OO', 'v')
brailleToEnglishMap.set('.OOO.O', 'w')
brailleToEnglishMap.set('OO..OO', 'x')
brailleToEnglishMap.set('OO.OOO', 'y')
brailleToEnglishMap.set('O..OOO', 'z')
brailleToEnglishMap.set('......', ' ')
brailleToEnglishMap.set('..OO.O', '.')
brailleToEnglishMap.set('..O...', ',')
brailleToEnglishMap.set('..O.OO', '?')
brailleToEnglishMap.set('..OOO.', '!')
brailleToEnglishMap.set('..OO..', ':')
brailleToEnglishMap.set('..O.O.', ';')
brailleToEnglishMap.set('....OO', '-')
brailleToEnglishMap.set('.O..O.', '/')
brailleToEnglishMap.set('O.O..O', '(')
brailleToEnglishMap.set('.O.OO.', ')')

brailleToNumberMap.set('.....O', '*') //Capital follows
brailleToNumberMap.set('.O...O', '**') //Decimal follows
brailleToNumberMap.set('.O.OOO', '***') //Number follows
brailleToNumberMap.set('O.....', '1')
brailleToNumberMap.set('O.O...', '2')
brailleToNumberMap.set('OO....', '3')
brailleToNumberMap.set('OO.O..', '4')
brailleToNumberMap.set('O..O..', '5')
brailleToNumberMap.set('OOO...', '6')
brailleToNumberMap.set('OOOO..', '7')
brailleToNumberMap.set('O.OO..', '8')
brailleToNumberMap.set('.OO...', '9')
brailleToNumberMap.set('.OOO..', '0')
brailleToNumberMap.set('......', ' ')
brailleToNumberMap.set('..OO.O', '.')
brailleToNumberMap.set('..O...', ',')
brailleToNumberMap.set('..O.OO', '?')
brailleToNumberMap.set('..OOO.', '!')
brailleToNumberMap.set('..OO..', ':')
brailleToNumberMap.set('..O.O.', ';')
brailleToNumberMap.set('....OO', '-')
brailleToNumberMap.set('.O..O.', '/')
brailleToNumberMap.set('.OO..O', '<')
brailleToNumberMap.set('O..OO.', '>')
brailleToNumberMap.set('O.O..O', '(')
brailleToNumberMap.set('.O.OO.', ')')

function brailleDecoder(str){
    var result = ""; 
    var isCapitalized = false;
    var numberMap = false;
    var currentMap = brailleToEnglishMap;

    for(let i = 0; i < str.length; i+= 6){
        let curr = str.slice(i, i+6);
        if(currentMap.getValue(curr) === '*'){
            isCapitalized = true;
            continue
        }
        if(currentMap.getValue(curr) === '***'){
            numberMap = true;
            currentMap = brailleToNumberMap;
            continue
        }

        if(currentMap.getValue(curr) === ' '){
            numberMap = false;
            currentMap = brailleToEnglishMap;
        }
        
        if (numberMap) {
            result += currentMap.getValue(curr);
        } else {
            let value = currentMap.getValue(curr)
            result += isCapitalized ? value.toUpperCase() : value;
            isCapitalized = false;
        }
    }
    return result
}
function brailleEncoder(str){
    let result = "";
    let currentMap = brailleToEnglishMap;

    for(const letter of str){
        const isCapitalized = letter === letter.toUpperCase() && letter !== letter.toLowerCase();
        const isNumber = !isNaN(letter) && letter.trim() !== '';

        if(isCapitalized){
            if (currentMap !== brailleToEnglishMap) {
                currentMap = brailleToEnglishMap;
            }
            result += currentMap.getKey('*'); 
            result += currentMap.getKey(letter.toLowerCase());
        }
        else if(letter === ' '){
            if (currentMap !== brailleToEnglishMap) {
                currentMap = brailleToEnglishMap;
            }
            result += currentMap.getKey(' ');
        }
        else if(isNumber){
            if (currentMap !== brailleToNumberMap) {
                result += brailleToNumberMap.getKey('***');
                currentMap = brailleToNumberMap;
            }
            result += currentMap.getKey(letter);
        }
        else{
            if (currentMap !== brailleToEnglishMap) {
                currentMap = brailleToEnglishMap;
            }
            result += currentMap.getKey(letter);
        }
    }
    return result;
}


const originalStatement = process.argv.slice(2);
const regex = /^[O.]*$/;

//To find if the arguments passed are in braille
if(regex.test(originalStatement[0])){
    let finalRes = brailleDecoder(originalStatement[0])//I'm assuming the braille will be fully typed in braille so no ' ' in the submission
    console.log(finalRes);
}
else{
    let englishStatement = originalStatement.join(" ");
    let finalRes = brailleEncoder(englishStatement)
    console.log(finalRes);
}
