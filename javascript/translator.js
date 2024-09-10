// Braille cypher
const alphaCypher = {
    alpha: {
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
        'z': 'O..OOO',
        'SPACE': '......',
    },
    number: {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',
    },
    special: {
        'CAP': '.....O',
        'NUM': '.O.OOO',
    }
  };

// To avoid looking up the same values over and over
// But also to make it easier to read, flip the cypher
function flipCypher(cypher) {
    const flipped = {};
    for (let category in cypher) {
        flipped[category] = {};
        for (let key in cypher[category]) {
            flipped[category][cypher[category][key]] = key;
        }
    }
    return flipped;
}

// Check if the input is braille
function isBraille(input) {
    return /^[.O]+$/.test(input);
}

// Convert braille to english
function brailleToEnglish(input, brailleCypher) {
    let result = '';
    let flag = '';

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);
        console.log('brailleChar', brailleChar);

         // Check for a flag (that the last char was "special")
         if (flag) {
            if (flag === "NUM") {
                // If you have an active NUM flag, check for a space (to turn off the flag) or get a number
                if (brailleChar == alphaCypher.alpha.SPACE) {
                    result += ' ';
                    flag = null;
                } else {
                    result += brailleCypher.number[brailleChar];
                }
                
            } else if (flag === "CAP") {
                // If you have an active CAP flag, capitalize this character
                let lowerCase = brailleCypher.alpha[brailleChar];
                result += lowerCase.toUpperCase();
                flag = null;
            }
        } else{
            switch (brailleChar) {
                //is a NUM flag for the next 6 characters
                case alphaCypher.special.NUM:
                    console.log('NUM');
                    flag = "NUM";
                    break;
                //is a CAP flag for the next 6 characters
                case alphaCypher.special.CAP:
                    console.log('CAP');
                    flag = "CAP";
                    break;
                //is a space
                case alphaCypher.alpha.SPACE:
                    console.log('space');
                    result += ' ';
                    break;
                //is a letter
                default:
                    console.log(brailleCypher.alpha[brailleChar]);
                    result += brailleCypher.alpha[brailleChar];
            }
        }
    }
    return result;
}

// Convert english to braille
function englishToBraille(input) {
    //console.log('englishToBraille', input);
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const char = input[i];
        result += alphaCypher[char];
    }
    return result;
}




// Get all command-line arguments and join them into a single string
const input = process.argv.slice(2).join(' ');
console.log("input", input);

// check if the input is braille
if (isBraille(input)) {    
    // create the braille cypher
    const brailleCypher = flipCypher(alphaCypher);
    result = brailleToEnglish(input, brailleCypher);
    console.log("is Braille for: ", result);
} else {
    console.log("is not Braille");
    //result = englishToBraille(input)
    //console.log("is English for: ", result);
}
