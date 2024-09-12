/* Ryan Chan Shopify Engineering Internship Challenge Submission 30/08/2024 */


/* -------- Global mapping for braille to char and reverse -------- */

// Braille to letter mapping 
const brailleToChar: { [key: string]: string } = {
    '100000': 'a', '101000': 'b', '110000': 'c', '110100': 'd', '100100': 'e',
    '111000': 'f', '111100': 'g', '101100': 'h', '011000': 'i', '011100': 'j',
    '100010': 'k', '101010': 'l', '110010': 'm', '110110': 'n', '100110': 'o',
    '111010': 'p', '111110': 'q', '101110': 'r', '011010': 's', '011110': 't',
    '100011': 'u', '101011': 'v', '011101': 'w', '110011': 'x', '110111': 'y',
    '100111': 'z', '000000': ' '
};

// Braille to number mapping 
const brailleToNum: { [key: string]: string } = {
    '100000': '1', '101000': '2', '110000': '3', '110100': '4', '100100': '5',
    '111000': '6', '111100': '7', '101100': '8', '011000': '9', '011100': '0',
}

// Reverse mapping from character/number to Braille binary pattern
const charToBraille: { [key: string]: string } = Object.fromEntries(
    Object.entries(brailleToChar).map(([key, value]) => [value, key])
);

const numToBraille: { [key: string]: string } = Object.fromEntries(
    Object.entries(brailleToNum).map(([key, value]) => [value, key])
);


/* -------- Helper functions -------- */ 

// Function to decide whether to translate to Braille or to English
function isBraille(input: string): boolean {

    // Check if input length is less than 6 (not valid Braille)
    if (input.length < 6) return false;

    // Check if first 6 characters are `.` or `0`
    const firstSixChars = input.slice(0, 6);
    return /^[.O]{6}$/.test(firstSixChars);
}

// Function to translate English to Braille
function translateToBraille(input: string): string {
    let brailleResult = '';
    let index = 0;
    let isNumber = false;

    // Iterate over input string processing 1 character at a time
    while (index < input.length) {

        // Extract character at current index 
        const char = input.charAt(index);
 
        if (!isNaN(parseInt(char, 10)) && char.trim() !== '' && !isNumber) { // Check if character is first number
            brailleResult += '.O.OOO'
            isNumber = true;

            const newChar = numToBraille[char].replace(/1/g, 'O').replace(/0/g, '.')
            brailleResult += newChar;
        } else if (char === char.toUpperCase() && char !== ' ' && !isNumber) {  // Check if character is uppercase
            brailleResult += '.....O'

            const newChar = charToBraille[char.toLowerCase()].replace(/1/g, 'O').replace(/0/g, '.')
            brailleResult += newChar;
        } else {
            // Reset isNumber flag if space encountered
            if (char === ' ') isNumber = false; 
            
            const newChar = isNumber ? numToBraille[char] : charToBraille[char];
            brailleResult += newChar.replace(/1/g, 'O').replace(/0/g, '.');
        }
        
        index++;
    } 

    return brailleResult;
}

// Function to translate Braille to English 
function translateToEnglish(input: string): string {

    // Convert input to binary string of `1` and `0`
    const binaryString = input
        .replace(/\./g, '0')
        .replace(/O/g, '1');

    let englishResult = '';
    let index = 0;
    let isCapital = false;
    let isNumber = false;

    // Iterate over binary string processing chunks of 6 characters
    while (index + 6 <= binaryString.length) {

        // Extract 1 braille character
        const brailleValue = binaryString.slice(index, index + 6);

        if (brailleValue === '000001') {
            isCapital = true
        } else if (brailleValue === '010111') {
            isNumber = true
        } else {
            if (brailleValue === '000000') isNumber = false;

            const newChar = isNumber ? brailleToNum[brailleValue] : brailleToChar[brailleValue];

            if (isCapital) {
                englishResult += newChar.toUpperCase();
                isCapital = false;
            } else {
                englishResult += newChar;
            }
        }

        index += 6;
    }

    return englishResult;
}


/* -------- Main program -------- */ 

function main() {
    // Capture command line arguments (excluding the first two default ones)
    const args = process.argv.slice(2);
    const input = args.join(' ');

    if(isBraille(input)) console.log(translateToEnglish(input));
    else console.log(translateToBraille(input));

    return;
}


// Execute the main function
main();