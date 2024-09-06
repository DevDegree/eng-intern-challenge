
const { braille_alphabet_dict, braille_num_dict, braille_symbols_dict, braille_precursor_dict } = require('./constants')
const { isBrailleCheck, splitEverySixChars, getKeyFromDict, getValueFromDict } = require('./utils')

const arg = process.argv.slice(2);



const isBraille = isBrailleCheck(arg)

function translate() {
    let output = "";
    let numberMode = false;
    let capitalMode = false;
    if (isBraille) {
        const english_translation_array = [];
        // Split into chunks of 6 characters
        const braille_array = splitEverySixChars(arg[0]);
    
        for (let braille of braille_array) {
            if (numberMode) {
                // When in numberMode, use the braille_num_dict until a space is encountered
                const number = getKeyFromDict(braille, braille_num_dict);
                if (number) {
                    english_translation_array.push(number);
                    continue;
                }                
                numberMode = false;

            }
            if (capitalMode) {
                // When in capitalMode, convert the letter to uppercase
                const letter = getKeyFromDict(braille, braille_alphabet_dict);
                if (letter) {
                    english_translation_array.push(letter.toUpperCase());
                }                
                capitalMode = false;
                continue;
            }

            const isPrecursor = getKeyFromDict(braille, braille_precursor_dict);
    
            if (isPrecursor) {
                switch(isPrecursor) {
                    case "capital follows":
                        capitalMode = true;
                        continue;
                    case "number follows":
                        numberMode = true;
                        continue;
                    case "space":
                        english_translation_array.push(" ");
                        numberMode = false;
                        capitalMode = false;
                        break;
                }

            } else {
                const isAlphabet = getKeyFromDict(braille, braille_alphabet_dict);
                const isSymbol = getKeyFromDict(braille, braille_symbols_dict);
    
                // Bug here where o and > can be confused
                if (isAlphabet) {
                    english_translation_array.push(isAlphabet)
                } else if (isSymbol) {
                    english_translation_array.push(isSymbol)
                }
            }
            // handle translation of braille to english here
        }
        output = english_translation_array.join("");
        return output
    } else {
        // handle alphabet to braille translation here.
        const braille_translation_array = [];
        const english_array = arg;
        
        for (let word of english_array) {
            const wordArray = word.split('');
            for (let character of wordArray) {
                if (!isNaN(parseInt(character))) {
                    // Only include number follows once until a space is encountered
                    !numberMode && braille_translation_array.push(getValueFromDict("number follows", braille_precursor_dict))
                    numberMode = true;
                    // Handle numbers
                    numberMode && braille_translation_array.push(getValueFromDict(character, braille_num_dict));
                } else if (character === character.toUpperCase()) {
                    // Handle capital letters
                    braille_translation_array.push(getValueFromDict("capital follows", braille_precursor_dict));
                    braille_translation_array.push(getValueFromDict(character.toLowerCase(), braille_alphabet_dict));
                } else {
                    // Handle lowercase letters and symbols
                    const symbol = getValueFromDict(character, braille_symbols_dict);
                    if (symbol) {
                        braille_translation_array.push(symbol);
                    } else {
                        braille_translation_array.push(getValueFromDict(character, braille_alphabet_dict));
                    }
                }
            }
            numberMode = false
            braille_translation_array.push(getValueFromDict("space", braille_precursor_dict))
        }
        output = braille_translation_array.slice(0, -1).join("");
        return output
    }
}

const translatedText = translate();
console.log(translatedText)