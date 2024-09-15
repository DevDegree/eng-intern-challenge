// --HELPER METHODS START--

function isBraille(text){
    const pattern = /[^O.]/
    if(pattern.test(text)){
        // There is a character that is not 0 or .
        return false
    }else{
        if(text.length % 6 !== 0){
            // The input is not set into blocks of 6 as is required
            return false
        }else{
            return true
        }
    }
}

//Get input from the terminal
const {argv} = require('node:process');
const originalMsg = argv[2];

// Determine if the code is Braille
if(isBraille(originalMsg)){
    // TODO: translate msg to English
}else{
    // TODO: transtlate msg to Braille
}

// Current output is just whether msg is braille or not
console.log(isBraille(originalMsg));