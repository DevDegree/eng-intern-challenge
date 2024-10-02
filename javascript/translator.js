// Mapped Letters to its Braille, the same Braille is used for lower case alphabet too
const englishToBraille = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO"
};

// Mapped Braille to its English Letter, the same Braille is used for lower case alphabet too
const brailleToEnglish = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
};


// Mapped numbers to its Braille.
const numberToBraille = {
    "1": "O.....",  
    "2": "O.O...",  
    "3": "OO....",  
    "4": "OO.O..",  
    "5": "O..O..",  
    "6": "OOO...",  
    "7": "OOOO..",  
    "8": "O.OO..",  
    "9": ".OO...",  
    "0": ".OOO.."   
};

// Mapped braille to its number
const brailleToNumber = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
};


const specialFormat = {
    "capital": ".....O",
    "number": ".O.OOO",
    "space":"......"
};


const brailleLength = 6;

function translateToBraille(input){
    let output = "";
    let isNumber = false; 
    // check input length if divisible by 6, since each braille character's length is 6 and uses regex to see if it consists of only "O"/"."
    if (input.length%brailleLength === 0 && /^[O.]+$/.test(input)){
        for (let i = 0; i < input.length; i+=brailleLength){
            let braille = input.substring(i,i+brailleLength);
            if(braille === specialFormat["space"]){
                isNumber = false;
                output += " ";
            }
            else if(braille === specialFormat["capital"]){
                i+=6;
                braille = input.substring(i,i+brailleLength);
                output += brailleToEnglish[braille];
            }
            else if(braille === specialFormat["number"]){
                isNumber = true;
            }
            else{ // if no space showed up, then it would continue using numbers instead of letters
                if(isNumber){
                    output+=brailleToNumber[braille];
                }
                else{
                    output+=brailleToEnglish[braille].toLowerCase();
                }
            }
        }
        
    }
    else{
    for(let char of input){
        if(char === " "){
            output += specialFormat["space"];
            isNumber = false;
        }
        else if(!isNaN(char)){ //if a number
            if(!isNumber){
                output += specialFormat["number"]
                isNumber = true;
            }
            output +=  numberToBraille[char];
        }
        else if(char === char.toUpperCase()){ //if Capital
            output += specialFormat["capital"] + englishToBraille[char.toUpperCase()]; 
        }
        else{
            output+= englishToBraille[char.toUpperCase()]; 
            
        }
        }
    }
    console.log(output);
    return output;
}

const input = process.argv.slice(2).join(" ");
translateToBraille(input);

