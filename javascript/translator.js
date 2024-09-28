//get maps
const { engToBraille, brailleToEng, brailleToNum, numToBraille, cap, uncap } = require('./maps');

//function to check if the string is braille
function isBraille(str){
    const allowedChars = /^[O.]+$/;
    return allowedChars.test(str);
}

//function to split the string into groups of 6
function splitIntoGroups(str){
    return str.match(/.{1,6}/g)||[];
}

//function to check if the charachter is capital
function isCapital(letter) {
    return letter !== ' ' && letter === letter.toUpperCase() && letter !== letter.toLowerCase();
}

//function to check if the character is a number
function isNumber(char) {
    return /^\d$/.test(char);
}

//function to translate the string
function translate(phrase){

    //create variables and flags for conditions
    let result = "";
    let capitalize = false;
    let numify = false;
    let isNum = true;

    //for braille do this
    if(isBraille(phrase)){

        //split the string
        const chars = splitIntoGroups(phrase);

        //loop through braille symbols
        for(const c of chars){
            //set value to the letter the symbol represents
            let value = brailleToEng[c];

            //if the symbol is indicating a capital set capitalize flag to true and skip the rest of the iteration
            if(value == 'cap'){
                capitalize = true;
                continue;
            }
            //if the symbol is indicating a number set number flag to true and skip the rest of the iteration
            else if(value == 'num'){
                numify = true
                continue;
            }
            //if the symbol is a space then set the number flag to false
            else if(value == ' '){
                numify = false
            }

            //if the preceeding symbol indicated a capital then make the letter a capital and set the capitalize flag to false
            if(capitalize == true){
                value = cap[value];
                capitalize = false;
            }
            //if the number flag is true then add a number
            else if(numify == true){
                value = brailleToNum[c];
            }

            // Handle undefined mapping
            if (value === undefined) {
                return "Invalid Braille input"; 
            }

            //add the letter or number to the result string
            result += value;
        }
        
    }
    
    //if it is english do this
    else{
        //loop through the characters in the string
        for(const char of phrase){
            //create string for value
            let value = "";

            //if the character is a capital then add the capital symbol then the letter
            if(isCapital(char) && !isNumber(char)){
                value = engToBraille['cap'] + engToBraille[uncap[char]];
            }
            //if the character is preceeded by a non number then add the number symbol and the number and set the number flag to false
            else if(isNumber(char) && isNum){
                value = engToBraille['num'] + numToBraille[char];
                isNum = false;
            }
            //if the character is a number preceeded by another number then add the number
            else if(isNumber(char) && !isNum){
                value = numToBraille[char];
            }
            //if the character is a space then add the space and set the number flag to true
            else if(char == ' '){
                value = engToBraille[char];
                isNum = true;
            }
            //if it is any other case then it must be a letter so we add the letter
            else{
                value = engToBraille[char];
            }

             // Handle undefined mapping
             if (value === undefined) {
                return "Invalid Braille input"; 
            }

            result += value;
        }
    }
    //return the final string
    return result;
}

//test the output with the test case
const input = process.argv.slice(2).join(" ");
console.log(translate(input));