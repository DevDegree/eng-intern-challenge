/**
 * Developer: Florence Yuen 
 * Language: TypeScript
 * Project name: Braille Translator 
 * Description: Determines if arguments passed into program at runtime (input string) is a valid Braille, where each Braille symbol is a 6 character string consisting of 'O' and '.' reading left to right, or English string.
 * Translates and outputs the string into English or Braille respectively. Able to translate all letters a through z, including capitalization (using a 'capital follows' symbol) as well as other special characters.
 * Braille Alphabet translation also includes the numbers 0 throgh 9, as well as spaces for multiple word translation.
*/

// Declare index signature for braille
type Braille = { [key: string]: string };

// Declare constant of all letters and symbols mapping to corresponding braille values for English to Braille translation
const LettersToBraille: Braille = {
    a: "O.....",
    b: "O.O...",
    c: "OO....",
    d: "OO.O..",
    e: "O..O..",
    f: "OOO...",
    g: "OOOO..",
    h: "O.OO..",
    i: ".OO...",
    j: ".OOO..",
    k: "O...O.",
    l: "O.O.O.",
    m: "OO..O.",
    n: "OO.OO.",
    o: "O..OO.",
    p: "OOO.O.",
    q: "OOOOO.",
    r: "O.OOO.",
    s: ".OO.O.",
    t: ".OOOO.",
    u: "O...OO",
    v: "O.O.OO",
    w: ".OOO.O",
    x: "OO..OO",
    y: "OO.OOO",
    z: "O..OOO",
    '.': "..OO.O",
    ',': "..O...",
    '?': "..O.OO",
    '!': "..OOO.",
    ':': "..OO..",
    '-': "..O.O.",
    '/': ".O..O.",
    '<': ".OO..O",
    '(': "O.O..O",
    ')': ".O.OO.",
    ' ': "......"
};

// Declare constant of all numbers mapping to corresponding Braille values for English to Braille Translation
const NumbersToBraille: Braille = {
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO.."
}

// Declare special Braille cases
const capitalFollows = ".....O";
const numberFollows = ".O.OOO";

// Each Braille symbol is a character string with size 6
const BRAILLE_CHAR_SIZE = 6;

// Creates reverse map for mapping the braille into corresponding letters and symbols for Braille to English translation
const BrailleToLetters = Object.fromEntries(
    Object.entries(LettersToBraille).map(([key, value]) => [value, key])
);

// Creates reverse map for mapping the braille into numbers for Braille to English translation
const BrailleToNumbers = Object.fromEntries(
    Object.entries(NumbersToBraille).map(([key, value]) => [value, key])
);

/**
 * Determines whether to convert to braille or english and outputs the translated output
 * @param stringToTranslate input string value
 */ 
function setTranslationType(stringToTranslate: string): string{
    if (isBraille(stringToTranslate)){
        return brailleToEnglish(stringToTranslate);
    }
    else{
        return englishToBraille(stringToTranslate);
    }
}

/**
 * Iterates through and determines if original string is in english or braille (if string only contains '.' or '0') 
 * @param stringToTranslate input string to be determined if is in braille or english
 * @return True if input follows value Braille pattern every substring contains 6 '.' or '0'. Else returns false 
 */
function isBraille(stringToTranslate: string): Boolean{
    // Check that input string will only be composed of 6 character long substrings to be Braille
    if((stringToTranslate.length % BRAILLE_CHAR_SIZE) != 0){
        return false;
    }

    // Use RegExp test() function to test if string matches '.' or '0'
    let regexp: RegExp = /^[O.]+$/; // If matches any of the enclosed characters (0 or .), $: to the end of the input
    return regexp.test(stringToTranslate);
}

/**
 * Converts the original string into braille
 * @param stringToTranslate input string to be translated into braille
*/
function englishToBraille(stringToTranslate: string){
    let translatedString = "";
    let isNumber = false;
    let char;

    // Split input string into substring with length of BRAILLE_CHAR_SIZE (6)
    for( let i = 0; i < stringToTranslate.length; i ++ ){
        char = stringToTranslate[i];

        // If character is a number, set to use the numbers map and add 'number follows' symbol
        if (char >= '0' && char <='9'){
            // Use BrailleToNumbers Map
            // Add 'number follows' symbol only if at the beginning of the number sequence
            if (!isNumber){
                translatedString += numberFollows;
                isNumber = true;
            }
            translatedString += NumbersToBraille[char];
            continue;
        }

        // Ends the number sequence if the next character is a space
        if (char === " "){
            isNumber = false;
        }
        // If character is a capital letter, add 'capital follows' symbol and the translated character in braille
        else if (/[A-Z]/.test(char)){
            translatedString += capitalFollows;
            char = char.toLowerCase();
        }

        translatedString += LettersToBraille[char];
    }

    return translatedString;
}

/**
 * Converts the original string from Braille into English
 * @param stringToTranslate input string to be translated into English
*/
function brailleToEnglish(stringToTranslate: string){
    let useCharMap = true;
    let capitalize = false;
    let translatedString = "";

    let splitString: string[] = [];
    // Split input string into substring with length of BRAILLE_CHAR_SIZE (6)
    for( let i = 0; i < stringToTranslate.length; i += BRAILLE_CHAR_SIZE ){
        splitString.push(stringToTranslate.slice(i, i + BRAILLE_CHAR_SIZE));
    }

    // Iterate through each substring (which represents an English character), search for matching value in map, and convert into english
    splitString.forEach(brailleSymbol => 
        {
            switch (brailleSymbol){
                // If 'number follows' symbol is read, assume all following symbols are numbers until the next 'space' symbol
                case numberFollows: 
                    useCharMap = false; // Use BrailleToNumbers Map
                    return;
                // If 'capital follows' symbol is read, the next symbol should be capitalized
                case capitalFollows:
                    capitalize = true; // Capitalize next character
                    return;
                case LettersToBraille[' ']:
                    useCharMap = true;
                    translatedString += ' ';
                    return;
                default:
                    let char;

                    // Get corresponding translated symbol for either Letters or Numbers map
                    if(useCharMap){
                        char = BrailleToLetters[brailleSymbol];
                    }
                    else {
                        char = BrailleToNumbers[brailleSymbol];
                    }

                    // Capitalize the character if the previous one was the 'capital follows' symbol
                    if(capitalize){
                        translatedString += char.toUpperCase();
                        capitalize = false;
                    }
                    else{
                        translatedString += char;
                    }
            }
        }
    );

    return translatedString;
}

function main(){
    // const for getting command line argument input string
    const inputString = process.argv.slice(2).join(' ');

    // return error if input string is missing or invalid
    if(!inputString){
        console.error("Invalid input");
        return
    }
    
    // Get the translation and output the translated string
    console.log (setTranslationType(inputString));
}

main();

/**
 * Other input values used for testing
 */
function testInputValues(){
    const validBrailleInput = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....";
    const englishInput = "Hello OOO...";
    const invalidBrailleInput = "O.OOOOO .O";
    const inputTest = "Abc 123 xYz";
    const numberInput = "42";
    const allValues = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789 .,?!:-/<()"

    setTranslationType(englishInput);
    setTranslationType(validBrailleInput);
    setTranslationType(invalidBrailleInput);
    setTranslationType(inputTest);
    setTranslationType(numberInput);
    setTranslationType(allValues);
}