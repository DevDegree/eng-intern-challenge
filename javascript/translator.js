class BrailleTranslator {
    input; 

    //initializes function with user input
    constructor(input) {
        this.input = input; 
    }

    //checks if the current input is braille or not using regex expression
    isBraille() {
        let pattern = new RegExp('^[O\\. ]+$');  // Allow only "O", ".", and space

        if (pattern.test(this.input)) {
            return true;
        }
        return false;
    }

    //helper function to help search for a non-braille character given a braille string of 6 and a dictionary
    searchKey(dictionary, key) {
        return Object.keys(dictionary).find(value => dictionary[value] == key) || '';
    }

    //translates from braille to english
    transToEnglish() {
        let engText = '';  // Store the resulting English text
        let numbMode = false;  // Track if we are in "number mode"
        let isCap = false;  // Track if the next letter should be capitalized
        let i = 0;  // Index to iterate over Braille input
        
        //retriving dictionaries in braille
        const ALPHABET = BrailleDictionary.getBAlphabet();
        const NUMBERS = BrailleDictionary.getBNumbers();
        const SYMBOLS = BrailleDictionary.getBSymbols();

        // Loop through Braille input in chunks of 6 characters (one Braille symbol)
        while (i < this.input.length) {
            let braille = this.input.substring(i, i + 6);  

            // Check if the current Braille symbol is a space
            if (braille === SYMBOLS['space']) {
                numbMode = false;  // Reset number mode when space is encountered
                engText += " ";  
            // Check if the current Braille symbol is a capital indicator
            } else if (braille === SYMBOLS['capital']) {
                isCap = true;  
            // Check if the current Braille symbol is a number indicator
            } else if (braille === SYMBOLS['number']) {
                numbMode = true;  
            // Handle numbers in Braille
            } else if (numbMode) {
                engText += this.searchKey(NUMBERS, braille);  
            // Handle letters in Braille
            } else {
                let char = this.searchKey(ALPHABET, braille);  
                
                // If capital mode is on, capitalize the letter
                if (isCap) {
                    char = char?.toUpperCase();
                    isCap = false;  
                }

                engText += char;  
            }
            i += 6;  
        }

        return engText;  
    }


    // Method to translate English to Braille
    transToBraille() {
        let btext = '';  // Store the resulting Braille text
        let numbMode = false;  // Track if we are in "number mode"
        
        const ALPHABET = BrailleDictionary.getBAlphabet();  
        const NUMBERS = BrailleDictionary.getBNumbers();  
        const SYMBOLS = BrailleDictionary.getBSymbols();  

        // Loop through each character 
        for (let i = 0; i < this.input.length; i++) {
            let char = this.input[i];
            // Handle spaces
            if (char === " ") {
                numbMode = false; 
                btext += SYMBOLS['space'];  
            // Handle capital letters
            } else if (/^[A-Z]$/.test(char)) {
                // If previously in number mode, add a space before capital letter
                if (numbMode) {
                    btext += SYMBOLS['space'];
                    numbMode = false;
                }
                btext += SYMBOLS['capital'];  
                btext += ALPHABET[char.toLocaleLowerCase()];  // Convert to lowercase Braille
            // Handle numbers
            } else if (/^\d$/.test(char)) {
                // If not already in number mode, add number indicator
                if (!numbMode) {
                    btext += SYMBOLS['number'];
                    numbMode = true;
                }
                btext += NUMBERS[char]; 
            // Handle punctuation
            } else if (SYMBOLS[char]) {
                btext += SYMBOLS[char];  
            // Handle lowercase letters
            } else {
                if (numbMode) {
                    btext += SYMBOLS['space'];
                    numbMode = false;
                }
                btext += ALPHABET[char];  
            }
        }

        return btext; t
    }
    
    // determing right translation direction and perform that translation
    translate() {
        if (this.isBraille()) {  
            return this.transToEnglish();  
        } else {
            return this.transToBraille(); 
        }
    }


}


class BrailleDictionary {

    // Static method to return Braille alphabet mapping (a-z)
    static getBAlphabet() {
        return {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO'
        };
    }
    
    // Static method to get Braille numbers
    static getBNumbers() {
        return {
        '1': 'O.....', 
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..'  
        };
    }
    
    // Static method to get Braille special symbols (capital indicator, number indicator, punctuation, and space)
    static getBSymbols() {
        return {
            'capital': '.....O',
            'number': '.O.OOO',
            'space': '......',
            '.': '..OO.O',
            ',': 'O.....',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': 'OOO...',
            ';': 'O.OOO.',
            '-': '..O...',
            '/': '.O.O.O',
            '<': 'OO.OO.',
            '>': '.OOO.O',
            '(': 'OOO..O',
            ')': 'OOO.O.'
        };
    }
    
}

function main() {
    const input = process.argv.slice(2).join(' '); 

    // Create an instance of BrailleTranslator with the input string
    const translator = new BrailleTranslator(input);

    
    // Perform the translation 
    // Output the translated result
    console.log(translator.translate());

}

main();