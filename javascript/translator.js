// Create a translation dictionary for char to braille
const charToBrailleDict = require('./utilities/characterToBrailleDictionary.json')

// Function to translate English to Braille
function englishToBraille(input) {
    const letterCheck = /^[A-Za-z]+$/
    const numberCheck = /^[0-9]+$/
    let result = '';
    let inNumberMode = false;

    for (let char of input) {
        //Check for capital
        if (letterCheck.test(char)) {
            if(char === char.toUpperCase()) result += charToBrailleDict['capital']
            char = char.toLowerCase();
            result += charToBrailleDict[char]
        }
        //Check for number
        if (numberCheck.test(char)) {
            if (!inNumberMode) {
                result += charToBrailleDict['number']
                inNumberMode = true;
            }
            result += charToBrailleDict[char]
        } else {
            inNumberMode = false;
        }
        //Check for spaces
        if(char === ' ') {
            result += charToBrailleDict['space']
        }
    }

    console.log(result)
};

/**
 * The first item (argv[0]) will be the path to node itself, and the second item (argv[1]) will be the path to your script code.
 * 
 * process.argv is an array and the first two items are:
 * [0]: path to the node
 * [1]: path to the script code (ex. node translate)
 * 
 * by using slice(2) I eliminate these two items and instead focus on the third item, which is the array of the sentence
 * ex. Hello world would come up as ["Hello", "world"]
 * that's why join(' ') is needed to combine the two
 */
const input = process.argv.slice(2).join(' ')

return englishToBraille(input)