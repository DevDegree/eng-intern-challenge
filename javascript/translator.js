let capital = false
let num = false

let text = process.argv.slice(2);

text = text.join(' ')
main(text.toString())

function main(text) {

    var type 

    const getType = (text) => {

        //check if only O and .
        return (/^[O.]+$/.test(text) === false) ? 'english' : 'braille'
    }
    
    type = getType(text)
    console.log(translate(text, type))
}

function translate(text, type) {

    var translation = ''

    for (let i = 0; i < text.length; i++) {
    
        //english --> braille
        if (type === 'english') {
            
            if (text.charAt(i) === '\s')
                console.log("whitespace")
            translation += getConversion(text.charAt(i), type)
        }
        //braille --> english
        else {
            var brailleCharacters = ''

            //get the next six characters
            for (let c = 0; c < 6; c++) {
                brailleCharacters += text.charAt(i+c)
            }    

            translation += getConversion(brailleCharacters, type)
            
            i+=5
        }
    }
    
    return translation
}

//determine the character conversion
function getConversion(text, type) {

    var translation = ''
    var translationData

    //loop through data to get respective translation
    const getTranslationData = () => {

        let result

        for (let c in translationData) {
            if (text == c) {

                if (capital == true) {
                    capital = false //reset 
                    result = translationData[c].toUpperCase()
                }
                else if (num == true) {
                    result = (translationData[c])
                }
                else {
                   
                    temp = (translationData[c])
                    result = temp
                }
            }
        }
        return result
    }

    //english --> braille
    if (type == 'english') {

        //check if capital
        if (/^[A-Z]$/.test(text)) {
            translation += '.....O'
            text = text.toLowerCase()
        }

        //if it is a number
        if (/^\d$/.test(text)) {

            //check if previous value was not a number
            if (num == false) {
                translation += '.O.OOO'
                num = true 
            }
            
            translationData = {
                '1': 'O.....', '2': 'O.O...', '3': 'OO....',
                '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
                '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',  
                '0': '.OOO..'
            }
            translation += getTranslationData()
        }
        //if it a regular text
        else { 

            num == false //reset

            translationData = {
                'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
                'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
                'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',  
                'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
                'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
                's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
                'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
                'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
                '.': '..OO.O', ',': '..O...', '?': '..O.OO',
                '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
                '-': '....OO', '/': '.O..O.', '<': '.OO..O',
                '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
            }
            translation += getTranslationData()
        } 
    }
    //braille --> english
    else {

        //if the next character is a capital return nothing
        if (text == '.....O') {
            capital = true
            return ''
        }

        if (text == '.O.OOO') {
            num = true
            return ''
        }
                
        if (num == true && text == '\s')
            num = false //reset

        //change the data set if the value is a number
        if (num == true) {
            translationData = {
                'O.....': '1', 'O.O...': '2', 'OO....': '3',
                'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
                'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
                '.OOO..': '0'
            }
        }
        else {
            translationData = {
                'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 
                'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 
                'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', 
                '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
                'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
                'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', 
                '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 
                'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
                'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ',
                '..OO.O': '.', '..O...': ',', '..O.OO': '?',
                '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
                '....OO': '-', '.O..O.': '/', '.OO..O': '<',
                'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
            }
        }
        translation += getTranslationData()
    }

    return translation
}