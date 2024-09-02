/**
 * Further optimizations: This code currently reads the entire input string into memory. 
 * For large inputs, we should try to implement a file input stream processing 
 * to only read a chuck of characters into memory. 
 * In this way, we can handle large data efficiently and avoid memory issues.
 */


const brailleToLetterMap = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO":"?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    "O.O..O":"(",
    ".O.OO.":")",
    "......": " ", 
    ".....O":"CAP", //capital follows
    ".O.OOO": "NUM", //number follows
    ".OO..O":"<"
};

const letterToBrailleMap = {};
for (const [braille, letter] of Object.entries(brailleToLetterMap)) {
    letterToBrailleMap[letter] = braille;
}

//exception case: ">" and "o" have the same braille translation
letterToBrailleMap['>'] = "O..OO.";


const brailleToNumberMap = {
    "O.....": "1",  
    "O.O...": "2",  
    "OO....": "3",  
    "OO.O..": "4",  
    "O..O..": "5",  
    "OOO...": "6",  
    "OOOO..": "7",  
    "O.OO..": "8",  
    ".OO...": "9",  
    ".OOO..": "0",  
    ".O...O":".", //decimal follows
    ".OO..O":"<",
    "O..OO.":">",
}

const numberToBrailleMap = {};
for (const [braille, letter] of Object.entries(brailleToNumberMap)) {
    numberToBrailleMap[letter] = braille;
}

/**
 * Translates the given input string from English to Braille or from Braille to English based on the format of the input.
 *
 * @param {string} input - The string to be translated. It can be either in Braille (using 'O' and '.') or in English.
 * @returns {string} - The translated string in either Braille or English.
 */

function translate(input){
    //test if it's braille with regex and also string length is multiple of 6
    const isBraille = /^[O.]+$/.test(input) && input.length % 6 === 0;

    if(isBraille){
        
        return brailleToEnglish(input);

    } else {
        
    
        return englishToBraille(input);

    }

}

/**
 * Translates Braille to English.
 *
 * @param {string} brailleStr - A string of Braille characters
 * @returns {string} - The translated English string.
 */
function brailleToEnglish(brailleStr){
    let result = "";

    isNumber = false;
    isCapital = false;

    //read input in multiples of 6
    for (let i = 0; i < brailleStr.length; i += 6) {
        const brailleChar = brailleStr.slice(i, i + 6); 

        let englishChar = brailleToLetterMap[brailleChar];


        if(englishChar === " "){//is space
            isNumber = false;
            result += " ";
           
        } else if(isNumber){ //is number
            //if decimal, number will be '.'
            englishChar = brailleToNumberMap[brailleChar];
            result += englishChar;
            
        } else {
            if(englishChar === "CAP"){
                isCapital = true;
                

            } else if (englishChar === "NUM"){
                isNumber = true;


            } else { //alphabete 
                if(isCapital){ // capital letters, only the next one is Capital
                    result += englishChar.toUpperCase();
                    isCapital = false;

                } else {
                    result += englishChar;
                }


            }
        }
            

        

    }


    return result;

}


/**
 * Translates English to Braille 
 *
 * @param {string} englishStr - The English string
 * @returns {string} - The translated Braille string
 */
function englishToBraille(englishStr){
    

    let result = "";
    let isNumber = false;



    for (const char of englishStr){
        //if is char is a number
        
        if (char !== ' ' && (!isNaN(char) || isNumber) ) {

            if (!isNumber) {
                //first number
                result+= letterToBrailleMap["NUM"];
                isNumber = true;
            }

            //decimal is handled
            result += numberToBrailleMap[char];
           

        } else {// char is a letter
            
            if(char === ' '){// is space
                isNumber = false;
               
            
            } 

            
            if(/[A-Z]/.test(char)){//check if character is uppercase
                result += letterToBrailleMap["CAP"];
            }
            

            result += letterToBrailleMap[char.toLowerCase()];



        }

    


    }

    return result;


}


//reading input from command line
const args = process.argv.slice(2);

//joing an array of input into one string with space between each word
const inputStr = args.join(' ');

//translate input and get output
const output = translate(inputStr);

//logging output to stdout
console.log(output);

