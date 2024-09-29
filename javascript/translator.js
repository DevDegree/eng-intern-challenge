//by Jethro Cao
//jcao99@my.centennialcollege.ca

//for the convertBraille array function
const brailleChars = [
    'O.....',   //a,1
    'O.O...',
    'OO....',
    'OO.O..',
    'O..O..',
    'OOO...',
    'OOOO..',
    'O.OO..',
    '.OO...',   //i,9
    '.OOO..',   //j,0
    'O...O.',
    'O.O.O.',
    'OO..O.',
    'OO.OO.',
    'O..OO.',
    'OOO.O.',
    'OOOOO.',   //q
    'O.OOO.',
    '.OO.O.',
    '.OOOO.',
    'O...OO',
    'O.O.OO',
    '.OOO.O',
    'OO..OO',
    'OO.OOO',
    'O..OOO',   //z
    '..OO.O',   //.
    '..O...',   //,
    '..O.OO',   //?
    '..OOO.',   //!
    '..OO..',   //:
    '..O.O.',   //;
    '....OO',   //-
    '.O..O.',   // /
    '.OO..O',   // <
    'O..OO.',   // >
    'O.O..O',   // (
    '.O.OO.',   // )
    '......',   // space
    '.....O',   //capital follows
    '.O...O',   //decimal follows
    '.O.OOO',   //number follows
];

//for the convertBraille array later
//matches braille alphabet character or symbol to index
//for alphabet char, symbol char, and follows commands
const brailleToLetter = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '.',
    ',',
    '?',
    '!',
    ':',
    ';',
    '-',
    '/',
    '<',
    '>',
    '(',
    ')',
    ' ',
    'capital follows',  //not printed, mode indicators
    'decimal follows',
    'number follows'
];

//for the convertBraille array later
//matches braille digit to index
const brailleToNumber = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0'
]

const nodeArgs = process.argv;

let argString = "";
let tempString; // temporary string that is used as a temporary variable
let tempChar;   //temporary character for conditional statment checks
let tempIndex;  //temporary value for the index value associated with a character for conversions arrays
let result = ""; //variable for the final string output

let numState = false;   //specifies to convert braille to num mode
let capitalState = false;    //specifies to convert braille to capital

for (let i=2;i<nodeArgs.length;i++){
    argString += nodeArgs[i] + " ";
}
tempString = argString.replace(/[\.O]/g,"");

//assumes braille input has no spaces in input
//the previous loop will insert a space at the end of the braille input
if (tempString == " "){
    //braille input
    argString = argString.replace(/\s/g,"");

    for (let i=0; i<argString.length/6; i++){
        tempString = argString.substring(i * 6, i * 6 + 6);
        tempIndex = brailleChars.findIndex((ele) => tempString == ele);
        tempChar = brailleToLetter[tempIndex];

        if (!numState && !capitalState){
            if (tempChar.length == 1){
                result += tempChar;
            }
            else if (tempChar == 'capital follows'){
                capitalState = true;
            }
            else if (tempChar == 'number follows'){
                numState = true;
            }
            else if (tempChar == 'decimal follows'){
                result += "."
            }
        }
        else{
            if (numState){
                if (tempIndex > 9){
                    numState = false;
                    result += tempChar;
                }
                else if (tempIndex >=0 && tempIndex <= 9){
                    result += brailleToNumber[tempIndex];
                }
            }
            else if(capitalState){
                capitalState = false;
                result += tempChar.toUpperCase();
            }
            
        }
    }
}
else{
    //English input
    argString = argString.substring(0,argString.length-1);
    let regexDigits = /\d/;

    for (let i=0; i<argString.length; i++){
        tempChar = argString[i];

        if (regexDigits.test(tempChar)){
            if (!numState){
                
                numState = true;
                result += brailleChars[brailleToLetter.findIndex((ele)=>ele == 'number follows')];
            }
            result += brailleChars[brailleToNumber.findIndex((ele)=>ele == tempChar)];
        }
        else{
            if (tempChar == '.' && numState){
                result += brailleChars[brailleToLetter.findIndex((ele)=>ele == 'decimal follows')];
            }
            else{
                numState = false;
                if (tempChar != tempChar.toLowerCase()){
                    //if value is capital
                    result += brailleChars[brailleToLetter.findIndex((ele)=>ele == 'capital follows')];
                }
                result += brailleChars[brailleToLetter.findIndex((ele)=>ele == tempChar.toLowerCase())];
            }
        }
    }
}

process.stdout.write(result);
