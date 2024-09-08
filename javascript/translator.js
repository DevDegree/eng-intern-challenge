//Parse arguments from command line to String variable
const inputString = process.argv.slice(2).join(' ');


//Main Function 
let isBraille = determineLanguage(inputString);
var output;

if(isBraille) {
    //braille to english function
    output = englishToBraille(inputString);
}
else {
    //english to braille function
    //output = function return
}


//Determine if string is braille or english
function determineLanguage(inputString) {
    const charArray = inputString.split("");
    //const charSet = new Set();
    //const setIter = charSet.values();

    // for(var i=0;i<charArray.length;i++) {
    //     charSet.add(charArray[i]);
    // }

    var currentChar;
    for(var i=0;i<charArray.length;i++) {
        currentChar = charArray[i];
        if(currentChar != "O" && currentChar != ".") {
            return false;
        }
    }

    return true;
}

function englishToBraille(inputString) {
    const englishChars = inputString.split("");
    var currentChar;
    var i=0;

    while(i<englishChars.length) {
        currentChar = englishChars[i];
        console.log(currentChar);
    }
}