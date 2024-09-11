/**
 * Developer: Florence Yuen 
 * Project name: Braille Translator 
 * Description: Determines if arguments passed into program (string) should be translated to English or Braille
 * 
*/

// Declare index signature for braille
type Braille = { [key: string]: string };

// Declare constant of all letters mapping to braille values
const LettersToBraille: Braille = {
    a: "0.....",
    b: "0.0...",
    c: "00....",
    d: "00.0...",
    e: "0..0..",
    f: "000...",
    g: "0000..",
    h: "0.00..",
    i: ".00...",
    j: ".000..",
    k: "0...0.",
    l: "0.0.0.",
    m: "00..0.",
    n: "00.00.",
    o: "0..00.",
    p: "000.0.",
    q: "00000.",
    r: "0.000.",
    s: ".00.0.",
    t: ".0000.",
    u: "0...00",
    v: "0.0.00",
    w: ".000.0",
    x: "00..00",
    y: "00.000",
    z: "0..000",
    '.': "..00.0",
    ',': "..0...",
    '?':"..0.00",
    '!': "..000.",
    ':': "..00..",
    '-': "..0.0.",
    '/': ".0..0.",
    '<': ".00..0",
    '>': "0..00.",
    '(': "0.0..0",
    ')': ".0.00.",
    ' ': "......"
};

// Declare special Braille cases
const capitalFollows = ".....0";
const numberFollows = ".0.000";

const NumbersToBraille: Braille = {
    1: "0.....",
    2: "0.0...",
    3: "00....",
    4: "00.0..",
    5: "0..0..",
    6: "000...",
    7: "0000..",
    8: "0.00..",
    9: ".00...",
    0: ".000.."
}

const BRAILLE_CHAR_SIZE = 6;

// Creates reverse map for mapping the braille into letters
const BrailleToLetters = Object.fromEntries(
    Object.entries(LettersToBraille).map(([key, value]) => [value, key])
);

const BrailleToNumbers = Object.fromEntries(
    Object.entries(NumbersToBraille).map(([key, value]) => [value, key])
);
// Object.fromEntries(reverseLettersToBraille);

// const for getting command line argument input string
const inputString = process.argv.slice(2).join(' ');

// Set whether to convert to braille or english 
function setTranslationType(stringToTranslate: string){
    if (isBraille(stringToTranslate)){
        console.log("Translating from braille to english");
        console.log (brailleToEnglish(stringToTranslate));
    }
    else{
        console.log("Translating from english to braille");
        console.log(englishToBraille(stringToTranslate));
    }
}

// /**
//  * @param stringToTranslate: input string to be determined if is in braille or english
//  * Iterates through and determines if original string is in english or braille (if string only contains '.' or '0')
//  */
// function isBraille(stringToTranslate: string): Boolean{
//     let splitString = stringToTranslate.split(' ');
//     console.log(splitString);

//     // Use RegExp test() function to test if string matches '.' or '0'
//     let regexp: RegExp = /^[0.]{6}$/; // If matches any of the enclosed characters (0 or .) and is 6 characters long, $: to the end of the input

//     // Iterate through each group of letters to test if matches pattern
//     // Returns true if every substring contains 6 '.' or '0' 
//     return splitString.every(word => regexp.test(word));
// }

/**
 * @param stringToTranslate: input string to be determined if is in braille or english
 * @return: True if input follows value Braille pattern every substring contains 6 '.' or '0'. Else returns false
 * @abstract: Iterates through and determines if original string is in english or braille (if string only contains '.' or '0') 
 */
function isBraille(stringToTranslate: string): Boolean{
    // Check that input string will only be composed of 6 character long substrings to be Braille
    if((stringToTranslate.length % BRAILLE_CHAR_SIZE) != 0){
        console.log("Not multiple of 6 " + stringToTranslate.length);
        return false;
    }

    console.log ("Valid string length: " + stringToTranslate + "\n");
    // Use RegExp test() function to test if string matches '.' or '0'
    let regexp: RegExp = /^[0.]+$/; // If matches any of the enclosed characters (0 or .), $: to the end of the input
    return regexp.test(stringToTranslate);

    // Iterate through each group of letters to test if matches pattern
    // Returns true if every substring contains 6 '.' or '0' 
    // return splitString.every(word => regexp.test(word));
}

    // // Determine if original string is in english or braille (if corresponding value found in braille values map)
    // iterate through all keys for braille values to see if original string is in english or braille
    // LettersToBraille.forEach(element => {
        
    // });

// Convert original string into braille
function englishToBraille(stringToTranslate: string){
    let translatedString = "";
    let isNumber = false;
    let char;

    // let splitString = stringToTranslate.split(" ");
    // Split input string into substring with length of BRAILLE_CHAR_SIZE (6)
    for( let i = 0; i < stringToTranslate.length; i ++ ){
        char = stringToTranslate[i];

        // If character is a number, set to use the numbers map and add 'number follows' symbol
        if (char >= '0' && char <='9'){
            // Use BrailleToNumbers Map
            // Add 'number follows' symbol for the only at the beginning of the sequence
            if (!isNumber){
                translatedString += numberFollows;
                isNumber = true;
            }
            translatedString += NumbersToBraille[char];
            continue;
        }

        if (char === " "){
            isNumber = false;
        }
        // If character is a capital letter, add 'capital follows' symbol and the translated character in braille
        else if (char === char.toUpperCase()){
            // console.log(char, capitalFollows);
            translatedString += capitalFollows;
            char = char.toLowerCase();
        }

        translatedString += LettersToBraille[char];
    }

    return translatedString;
}

function brailleToEnglish(stringToTranslate: string){
    let useCharMap = true;
    let capitalize = false;
    let translatedString = "";

    let splitString: string[] = [];
    // Split input string into substring with length of BRAILLE_CHAR_SIZE (6)
    for( let i = 0; i < stringToTranslate.length; i += BRAILLE_CHAR_SIZE ){
        splitString.push(stringToTranslate.slice(i, i + BRAILLE_CHAR_SIZE));
    }

    // console.log ("Input string: " + splitString + "\n");

    // Iterate through each substring (which represents an English character), search for matching value in map, and convert into english
    splitString.forEach(brailleSymbol => 
        {
            switch (brailleSymbol){
                // If 'number follows' symbol is read, assume all following symbols are numbers until the next 'space' symbol
                case numberFollows:
                    // Use BrailleToNumbers Map
                    useCharMap = false;
                    return;
                // If 'capital follows' symbol is read, the next symbol should be capitalized
                case capitalFollows:
                    // Capitalize next character
                    capitalize = true;
                    return;
                case ' ':
                    useCharMap = true;
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

// function main(){
    const validBrailleInput = ".....00.....0.0...00...........0.0000.....0.0...00....";
    const englishInput = "Hello 000...";
    const invalidBrailleInput = "0.000000 .0";
    const inputTest = "Abc 123 xYz";

    if(!inputString){
        console.error("Invalid input");
    }
    else{
        console.log("String input is: " + inputString + "\n");
        setTranslationType(inputString);
    }

    console.log("\nInput 2: " + englishInput + "\n");
    setTranslationType(englishInput);

    console.log("\nInput 3: " + validBrailleInput + "\n");
    setTranslationType(validBrailleInput);

    console.log ("\nInput 4: " + invalidBrailleInput + "\n");
    setTranslationType(invalidBrailleInput);

    console.log("\nInput 5: " + inputTest + "\n");
    setTranslationType(inputTest);
// }