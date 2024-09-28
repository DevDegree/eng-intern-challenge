// Initializes the map of characters
const characters: Map<string, string> = new Map([
    ["a", "O....."],
    ["b", "O.O..."],
    ["c", "OO...."],
    ["d", "OO.O.."],
    ["e", "O..O.."],
    ["f", "OOO..."],
    ["g", "OOOO.."],
    ["h", "O.OO.."],
    ["i", ".OO..."],
    ["j", ".OOO.."],
    ["k", "O...O."],
    ["l", "O.O.O."],
    ["m", "OO..O."],
    ["n", "OO.OO."],
    ["o", "O..OO."],
    ["p", "OOO.O."],
    ["q", "OOOOO."],
    ["r", "O.OOO."],
    ["s", ".OO.O."],
    ["t", ".OOOO."],
    ["u", "O...OO"],
    ["v", "O.O.OO"],
    ["w", ".OOO.O"],
    ["x", "OO..OO"],
    ["y", "OO.OOO"],
    ["z", "O..OOO"],
    ["capitalFol", ".....O"], // Indicates uppercase letter
    ["decimalFol", ".O...O"], // Indicates decimal point
    ["numberFol", ".O.OOO"], // Indicates numbers mode
    [".", "..OO.O"], // Braille for dot
    [",", "..O..."], // Braille for comma
    ["?", "..O.OO"], // Braille for question mark
    ["!", "..OOO."], // Braille for exclamation mark
    [":", "..OO.."], // Braille for colon
    [";", "..O.O."], // Braille for semicolon
    ["-", "....OO"], // Braille for hyphen
    ["/", ".O..O."], // Braille for slash
    ["space", "......"] // Braille for space
]);

// Initializes the map of numbers
const nums: Map<number, string> = new Map([
    [0, ".OOO.."],
    [1, "O....."],
    [2, "O.O..."],
    [3, "OO...."],
    [4, "OO.O.."],
    [5, "O..O.."],
    [6, "OOO..."],
    [7, "OOOO.."],
    [8, "O.OO.."],
    [9, ".OO..."],
]);

// Stores process arguments
const processArgs: string[] = process.argv.splice(2); 

// Stores user input as string
const userInput: string = processArgs.join(" ");

// Checks if input is in braille
const isBraille: boolean = /^[\.O]+$/.test(userInput);

if (isBraille) {
    /*
        chars - array of braille characters
        translatedChars - array of characters translated from braille to english ones
        isPushingNumbers & isNextCapital - booleans controlling the flow of translating numbers and uppercase letters
    */

    let chars: string[] = userInput.match(/.{6}/g); // Splits the input into groups of six (braille chars)
    let translatedChars: string[] = []; // Stores the translated characters
    let isPushingNumbers: boolean = false; // Flag to indicate if numbers are being processed
    let isNextCapital: boolean = false; // Flag to indicate if the next character should be uppercase

    chars.forEach((brailleCharacter: string) => {
        // if the following character indicates number mode, switch to numbers
        if (brailleCharacter === characters.get("numberFol")) {
            isPushingNumbers = true; // Set flag to true for number mode
            return;
        }

        // if the char is space - stop printing numbers and add space
        if (brailleCharacter === characters.get("space")) {
            isPushingNumbers = false; // Reset number mode on space
            translatedChars.push(" "); // Add space to output
            return;
        }

        // if in number mode and character is decimal, add a dot
        if (isPushingNumbers) {
            if (brailleCharacter === characters.get("decimalFol")) {
                translatedChars.push("."); // Add decimal point to output
                isPushingNumbers = false; // Reset number mode
            } else {
                translatedChars.push(translateNum(brailleCharacter, isBraille)); // Translate number
            }
            return;
        }

        // if the following char indicates Capitalized, switch mode for next char
        if (brailleCharacter === characters.get("capitalFol")) {
            isNextCapital = true; // Set flag for next character to be uppercase
            return;
        }

        // if previous char indicated that this one is capitalized, convert to uppercase
        if (isNextCapital) {
            let translatedCharInUpper: string = translateChar(brailleCharacter, isBraille).toUpperCase(); // Translate and capitalize
            translatedChars.push(translatedCharInUpper); // Add capitalized char to output
            isNextCapital = false; // Reset flag
            return;
        }

        // if the character is just a lowercase letter - print it
        translatedChars.push(translateChar(brailleCharacter, isBraille)); // Translate and add to output
    });

    console.log(translatedChars.join("")); // Output translated string
}

if (!isBraille) {
    let chars: string[] = Array.from(userInput); // Convert input string to array of characters
    let translatedChars: string[] = []; // Stores the translated Braille characters
    let isPushingNumbers: boolean = false; // Flag for number processing

    chars.forEach((item: string, index: number) => {
        // check if character is number using regular expression
        let isNumber: boolean = /\d/.test(item); // Check if character is a number

        if (isNumber) { 
            if (!isPushingNumbers) {
                translatedChars.push(characters.get("numberFol")); // Start number mode
                isPushingNumbers = true; // Set flag for number mode
            }
            translatedChars.push(translateNum(item, isBraille)); // Translate number and add to output
            return;
        }

        if (item === " ") {
            translatedChars.push(characters.get("space")); // Add Braille for space
            isPushingNumbers = false; // Reset number mode
            return;
        }

        if (isPushingNumbers && item === ".") {
            translatedChars.push(characters.get("decimalFol")); // Add Braille for decimal
            isPushingNumbers = false; // Reset number mode after decimal
            return;
        }

        if (item === item.toUpperCase() && item !== item.toLowerCase()) {
            translatedChars.push(characters.get("capitalFol")); // Add Braille for capital
            translatedChars.push(translateChar(item.toLowerCase(), isBraille)); // Translate to lowercase for lookup
            return;
        }

        translatedChars.push(translateChar(item, isBraille)); // Translate normal character and add to output
    });

    console.log(translatedChars.join("")); // Output Braille string
}

// Function to translate numbers from Braille to English or vice versa
function translateNum(num: string | number, isBraille: boolean): string {
    if (isBraille) {
        for (const [number, brailleString] of nums) {
            if (brailleString === num) {
                return number.toString(); // Return the English number if Braille is given
            }
        }
    } else {
        return nums.get(Number(num)); // Return Braille for the given English number
    }
}

// Function to translate characters from Braille to English or vice versa
function translateChar(char: string, isBraille: boolean): string {
    if (isBraille) {
        for (const [character, brailleString] of characters) {
            if (brailleString === char) {
                return character; // Return English character if Braille is given
            }
        }
    } else {
        return characters.get(char); // Return Braille for the given English character
    }
}
