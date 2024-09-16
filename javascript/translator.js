/*ASSUMPTIONS
1) Since the Technical Requirements section under Braille Alphabet mentions 
   only letters, numbers, and spaces, I have not considered other symbols.
2) As per the Technical Requirements, numbers are expected to follow a 
    "Number Follows" symbol and will continue to be interpreted as numbers 
    until a space is encountered, at which point the number mode resets.

*/


function translator(str) {
    if (isBraille(str))
       return brailleToAlpha(str); // Convert Braille to English
    else
       return alphaToBraille(str); // Convert English to Braille
}

function isBraille(str) {
    // Check if the string length is a multiple of 6 and consists only of 'O' and '.'
    return (str.length % 6 === 0) && /^[O.]*$/.test(str);
}

function isEnglish(str) {
    // English Strings must consist only of letters, numbers, and spaces
    return /^[a-zA-Z0-9\s]+$/.test(str);
}

// Function to set mappings for the HashMaps (for brailleAlpha and brailleNum)
function setBrailleMaps(brailleAlpha, brailleNum) {
    // Braille to Alphabet
    brailleAlpha.set('O.....', 'a');
    brailleAlpha.set('O.O...', 'b');
    brailleAlpha.set('OO....', 'c');
    brailleAlpha.set('OO.O..', 'd');
    brailleAlpha.set('O..O..', 'e');
    brailleAlpha.set('OOO...', 'f');
    brailleAlpha.set('OOOO..', 'g');
    brailleAlpha.set('O.OO..', 'h');
    brailleAlpha.set('.OO...', 'i');
    brailleAlpha.set('.OOO..', 'j');
    brailleAlpha.set('O...O.', 'k');
    brailleAlpha.set('O.O.O.', 'l');
    brailleAlpha.set('OO..O.', 'm');
    brailleAlpha.set('OO.OO.', 'n');
    brailleAlpha.set('O..OO.', 'o');
    brailleAlpha.set('OOO.O.', 'p');
    brailleAlpha.set('OOOOO.', 'q');
    brailleAlpha.set('O.OOO.', 'r');
    brailleAlpha.set('.OO.O.', 's');
    brailleAlpha.set('.OOOO.', 't');
    brailleAlpha.set('O...OO', 'u');
    brailleAlpha.set('O.O.OO', 'v');
    brailleAlpha.set('.OOO.O', 'w');
    brailleAlpha.set('OO..OO', 'x');
    brailleAlpha.set('OO.OOO', 'y');
    brailleAlpha.set('O..OOO', 'z');

    // Braille to Number
    brailleNum.set('O.....', '1');
    brailleNum.set('O.O...', '2');
    brailleNum.set('OO....', '3');
    brailleNum.set('OO.O..', '4');
    brailleNum.set('O..O..', '5');
    brailleNum.set('OOO...', '6');
    brailleNum.set('OOOO..', '7');
    brailleNum.set('O.OO..', '8');
    brailleNum.set('.OO...', '9');
    brailleNum.set('.OOO..', '0');
}

// Function to convert Braille to English
function brailleToAlpha(str) {
    let brailleAlpha = new Map(); // Map to store braille to alphabet conversion
    let brailleNum = new Map(); // Map to store braille to number conversion
    setBrailleMaps(brailleAlpha, brailleNum); // Initialize maps with braille conversions

    let mapToUse = brailleAlpha; // Default map is for alphabets
    let output = "";
    let offset = 0;

    // Loop through input string in chunks of 6
    for (let i = 0; i < str.length; i += 6) {
        let substr = str.substring(i, i + 6);

        switch (substr) {
            case '......':
                output += ' '; // Handle space
                mapToUse = brailleAlpha;
                break;
            case '.....O': // Handle Capital Letters
                mapToUse = brailleAlpha;
                offset = 32; // ASCII offset for Capital Letters
                break;
            case '.O.OOO': // Handle Numbers
                mapToUse = brailleNum;
                offset = 0;
                break;
            default:
                let ch = mapToUse.get(substr); // Mapping from the selected map
                output += String.fromCharCode(ch.charCodeAt(0) - offset); // Offset to handle capital letters
                offset = 0; // Reset offset after use
                
        }
    }
    return output; // Return the converted output
}

// Function to set English to Braille mapping
function setAlphaToBrailleMap(toBraille) {
    toBraille.set('SPACE', '......');
    toBraille.set('CAPITAL', '.....O');
    toBraille.set('NUM', '.O.OOO');
    toBraille.set('a', 'O.....');
    toBraille.set('b', 'O.O...');
    toBraille.set('c', 'OO....');
    toBraille.set('d', 'OO.O..');
    toBraille.set('e', 'O..O..');
    toBraille.set('f', 'OOO...');
    toBraille.set('g', 'OOOO..');
    toBraille.set('h', 'O.OO..');
    toBraille.set('i', '.OO...');
    toBraille.set('j', '.OOO..');
    toBraille.set('k', 'O...O.');
    toBraille.set('l', 'O.O.O.');
    toBraille.set('m', 'OO..O.');
    toBraille.set('n', 'OO.OO.');
    toBraille.set('o', 'O..OO.');
    toBraille.set('p', 'OOO.O.');
    toBraille.set('q', 'OOOOO.');
    toBraille.set('r', 'O.OOO.');
    toBraille.set('s', '.OO.O.');
    toBraille.set('t', '.OOOO.');
    toBraille.set('u', 'O...OO');
    toBraille.set('v', 'O.O.OO');
    toBraille.set('w', '.OOO.O');
    toBraille.set('x', 'OO..OO');
    toBraille.set('y', 'OO.OOO');
    toBraille.set('z', 'O..OOO');
    toBraille.set('1', 'O.....');
    toBraille.set('2', 'O.O...');
    toBraille.set('3', 'OO....');
    toBraille.set('4', 'OO.O..');
    toBraille.set('5', 'O..O..');
    toBraille.set('6', 'OOO...');
    toBraille.set('7', 'OOOO..');
    toBraille.set('8', 'O.OO..');
    toBraille.set('9', '.OO...');
    toBraille.set('0', '.OOO..');
}

// Function to convert English to Braille
function alphaToBraille(str) {
    let toBraille = new Map(); // Map to store symbols to Braille conversion
    setAlphaToBrailleMap(toBraille); // Initialize English to Braille map

    let output = "";
    let isNum = false; // Flag to track number mode

    for (let char of str) { // Loop through the input string to convert each character
        switch (char) {
            case ' ':
                output += toBraille.get('SPACE'); // Handle space
                isNum = false; // Reset number mode on space
                break;
            default:
                if (char >= '0' && char <= '9') { // Handle numbers directly
                    if (!isNum) {
                        output += toBraille.get('NUM'); // Add number prefix if not already in number mode
                        isNum = true;
                    }
                    output += toBraille.get(char);
                } else if (char >= 'A' && char <= 'Z') { // Handle capital letters
                    output += toBraille.get('CAPITAL'); // Add capital letter marker
                    output += toBraille.get(char.toLowerCase()); // Convert lowercase equivalent to Braille
                } else {
                    output += toBraille.get(char); // Convert lowercase letters directly
                }
        }
    }
    return output; // Braille Translation
}

// Main function to read input and call translator
function main() {

      // Join all command-line arguments after the first two into a single string
      const input = process.argv.slice(2).join(' ');

      if(!input)
        {
            console.error("Please enter the string to translate");
            process.exit(1);
        }
          // Translate the input and print the result
    try {
        const result = translator(input);
        console.log(result);
    } 
    catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
    }


main();
