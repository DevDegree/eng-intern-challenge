
//A dictionary which holds all the alphabets as keys and braile code as values
const Brailetoalphabetssymbols = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    'Capital': '.....O', 'Space': '......', 'Number': '.O.OOO'
}

//A dictionary which holds all the numbers and corresponding braile codes
const Brialetonumbersymbols = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}


//A function to convert given text string to braile 
function AlphabetToBraile(text) {
    let finalresult = ''
    let innumbermode = false

    //Every words of a sentence are being split 
    let words = text.split(" ")
    words.forEach((word, index) => {
        let brailleword = ''
        innumbermode = false

        //Every letters of a word are being split and being converted into braile characters.
        letters = word.split("")
        letters.forEach(character => {
            if (isNaN(character)) {
                if (character === character.toUpperCase()) {
                    brailleword += Brailetoalphabetssymbols['Capital'] + Brailetoalphabetssymbols[character.toLowerCase()]
                }
                else {
                    brailleword += Brailetoalphabetssymbols[character.toLowerCase()]
                }
            }
            else {
                if (!innumbermode) {
                    brailleword += Brailetoalphabetssymbols['Number'] + Brialetonumbersymbols[character]
                    innumbermode = true
                }
                else {
                    brailleword += Brialetonumbersymbols[character]
                }

            }
        });
        if (index < words.length - 1) {
            brailleword += Brailetoalphabetssymbols['Space']
        }

        finalresult += brailleword
    });
    console.log(finalresult.toString())
}


//A function to convert the given braile string to alphabet or number values.
function BraileToAlphabet(braile) {
    let alphabetkeys = Object.keys(Brailetoalphabetssymbols)
    let numberkeys = Object.keys(Brialetonumbersymbols)
    let finalresult = ''
    let capitalflag = false
    let numberflag = false

    //Separates the entire brailetext into fragments with 6 characters each and then checks accordingly.
    let brailchunks = braile.match(/.{1,6}/g)
    brailchunks.forEach(chunk => {
        let alphabet = alphabetkeys.find(i => Brailetoalphabetssymbols[i] == chunk)
        if (alphabet === 'Space') {
            numberflag = false
            finalresult += " "
        }
        else if (alphabet === 'Capital') {
            capitalflag = true
        }
        else if (alphabet === 'Number') {
            numberflag = true
        }
        else {
            if (capitalflag) {
                finalresult += alphabet.toUpperCase()
                capitalflag = false;
            }
            else if (numberflag) {
                let number = numberkeys.find(i => Brialetonumbersymbols[i] == chunk)
                finalresult += number
            }
            else {
                finalresult += alphabet;
            }

        }
    });
    console.log(finalresult.toString())
}

//A sample text to check the application.
let inputtext = 'Abc 123 xYz'

//This function here determines whether the given string is an input text or a braile code and then invokes the conversion function accordingly.
function ConvertToOppositeForm(input) {
    if (input.includes('O') && input.includes('.')) {

        if (BrailleCodeValidator(inputtext)) {
            try {
                BraileToAlphabet(input)
            }
            catch (ex) {
                console.log("Please enter the proper braile code")
            }
        }
        else {
            console.log("Please enter a proper braille code")
        }

    }
    else {
        try {
            AlphabetToBraile(input)
        }
        catch (ex) {
            console.log("An error occured while converting to braille ", ex.message)
        }

    }

}

//This function here validates the braille code before passing it as an argument in the ConvertToOpposite function. 
function BrailleCodeValidator(Code) {
    let validchars = ['O', '.']
    Code.split().forEach(element => {
        if (!validchars.includes(element)) {
            return false
        }
    });

    if (Code.split("").length % 6 !== 0) {
        return false
    }

    return true
}

ConvertToOppositeForm(inputtext)


