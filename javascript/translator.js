//Declare a map to store the values of the braile codes
const braile = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ' : "......",
    'capital' : ".....O", 'number' : '.O.OOO'
};

const braileN = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
};

//Translate the english input to braile
function toBraile(input) {
    var result = "";
    var number = false;

    //Loop through each character of the input
    for (let i = 0; i < input.length; i++) {
        let char = input[i];
        
        //If a space is detected, reset the flag for checking a number and add the braile for space
        if (char === ' ') {
            result += braile[' '];
            number = false;
        }
        //If a number is detected
        else if (!isNaN(char)) {
            //If this character is the first number detected, print the braile for number follows and set the number flag to true
            if (!number) {
                result += braile['number'];
                number = true;
            }

            //Add the braile for this number character
            result += braileN[char];
        }
        else {
            //Set the number flag to false
            number = false;
            
            //If a upper case letter was detected, print the braile for capital follows
            if (char === char.toUpperCase()) {
                result += braile['capital'];
            }
            
            //Add the braile for this alphabet character
            result += braile[char.toLowerCase()];
        }
    }

    return result;
}

//Function to translate braile to english
function toEnglish(input) {
    var result = "";
    var strs = [];

    //Loop through every six character and store every braile string as a sub string in the array strs
    for (let i = 0; i < input.length; i += 6) {
        let subStr = input.substring(i, i + 6);
        strs.push(subStr);
    }

    //Flags for checking capital and number
    let capital = false;
    let number = false;

    //Loop through each braile string found
    for (let i = 0; i < strs.length; i++) {
        //If the braile for space follows is found, add a space and set the flags to false
        if (strs[i] == braile[' ']) {
            result += ' ';
            capital = false;
            number = false;
        }
        //If the braile for capital follows is found, set the flag for capital true
        else if (strs[i] == braile['capital']) {
            capital = true;
            number = false;
        }
        //If the braile for number follows is found, set the flag for number true
        else if (strs[i] == braile['number']) {
            number = true;
            capital = false;
        }
        else {
            //If the flag for number is true, then add the number for the specified number to the final string            
            if (number) {
                let char = Object.keys(braileN).find(key => braileN[key] == strs[i]);
                result += char;
            }
            else {
                let char = Object.keys(braile).find(key => braile[key] == strs[i]);

                //Check if the flag for capital to print either an upper case or lower case letter
                if (capital) {
                    result += char.toUpperCase();
                    capital = false;
                }
                else {
                    result += char;
                }
            }
        }
    }

    return result;
}

main();

function main() {
    //Get the input from the command line
    let input = process.argv.slice(2).join(" ");

    //Check if the input only contains O and .
    if ( /^[O.]+$/.test(input)) {
        //Check if the braile input has the correct length
        if (input.length % 6 != 0) 
            console.error("Braile input does not have the proper length");
        else
            console.log(toEnglish(input));
    }
    else {
        //Check if the input only contains letters, numbers and spaces
        if (!/[^a-zA-Z0-9\s]/.test(input))
            console.log(toBraile(input));
        else   
            console.error("Improper input found");
    }
}