//create 2 functions

//translate english -> braille

//translate braille -> english.
//how to know if we need to run this function?

//this function checks if the string entered is english or braille.
function natureOfString(str){
    let isEnglish = false
    if (str.length < 6){
        //for sure it is an english string, because braille is atleast 6 char no matter what
        isEnglish = true;
    }
    else{
        //if it's not less than 6 then check the actual characters for english alphabet
        for(let i = 0; i<6; i++){ //no need to look at the entire string, just look at the first 6 characters is enough.
            if(str[i] !== "O" && str[i]!=="."){ //if you got a letter other than "O" or "." then you're not writing braille, you're writing english.
                isEnglish = true;
            }
        }
    }
    return isEnglish;
}
// console.log(natureOfString("OOO..I"))

// 1     10
// 100   1000
// 10000 100000


//helper function that takes a braille matrix and finds which english letter it corresponds to.
function computeEngLetter(str){
    let value = 0
    for(let i = 0; i<str.length; i++){
        if (str[i] === "O"){
            value += 1 * Math.pow(10,str.length - 1 - i);    //Math.pow(base, exponent)
        }
    } //OOOOOO
   // console.log(value);
   return value;
}

//will be necessary when translating
function flipString(str){
    // const arr = Array.from(str)
    let newstr = "";
    for(let i = str.length-1; i>-1; i--){
      newstr += str[i];
    }
    return newstr;
}
// console.log(flipString("HELLO"));

function convertBrailToNumber(str){
    let newStr = ""
    for(let i = 0; i<str.length; i++){
        if(str[i] === "O"){// the letter O not zero
            newStr += "1"
        }else{ //if str[i] === "."
            newStr += "0"
        }
    }
    return newStr;
}
// console.log(convertBrailToNumber("...O"))


//for eng -> braille
//converts number into brail, so 1011 becomes O.OO
function convertBrailledigits(str){
    let newStr = ""
    for(let i = 0; i<str.length; i++){
        if(str[i] === "1"){
            newStr += "O"
        }else{ //if str[i] === "0"
            newStr += "."
        }
    }
    return newStr;
}

function isUpperCase(lett) {
    return lett === lett.toUpperCase();
}


//just to help me copy paste all of the thing below because im too lazy to write it all
// const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// for(let i = 0; i<26; i++){
//     console.log(`engLetters[${i}] = \"${alphabet[i].toLowerCase()}\"`)
// }

//computeEngLetter("O...OO")
const engLetters = new Array(111111)
//now we translate
engLetters[0] = " "; //space character
engLetters[1] = "a"
engLetters[101] = "b"
engLetters[11] = "c"
engLetters[1011] = "d"
engLetters[1001] = "e"
engLetters[111] = "f"
engLetters[1111] = "g"
engLetters[1101] = "h"
engLetters[110] = "i"
engLetters[1110] = "j"
engLetters[10001] = "k"
engLetters[10101] = "l"
engLetters[10011] = "m"
engLetters[11011] = "n"
engLetters[11001] = "o"
engLetters[10111] = "p"
engLetters[11111] = "q"
engLetters[11101] = "r"
engLetters[10110] = "s"
engLetters[11110] = "t"
engLetters[110001] = "u"
engLetters[110101] = "v"
engLetters[101110] = "w"
engLetters[110011] = "x"
engLetters[111011] = "y"
engLetters[111001] = "z"

//To test translation from braille to english
//Bonjour = "101 11001 11011 1110 11001 110001 11101"
// const myMessage = "...O.O OO..O OO.OO OOO. OO..O OO...O OOO.O"
// const arr = myMessage.split(" ");
// // console.log(arr);
// let decryptedMessage ="";
// for (crypt of arr){
//     const num = computeEngLetter(crypt);
//     // console.log(num);
//     decryptedMessage += engLetters[num];
// }
// console.log(decryptedMessage);




//Now onto translating from english to braille
const EngToBrArr = new Array(26);
const EngToBrArrIndexReference = new Array(26);
// const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// for(let i = 0; i<26; i++){
//     console.log(`EngToBrArr[${i}] = \"${alphabet[i].toLowerCase()}\"`)
//     // console.log(`EngToBrArrIndexReference[${i}] = ${engLetters.indexOf(alphabet[i])}`)
// }

EngToBrArr[0] = "a"
EngToBrArr[1] = "b"
EngToBrArr[2] = "c"
EngToBrArr[3] = "d"
EngToBrArr[4] = "e"
EngToBrArr[5] = "f"
EngToBrArr[6] = "g"
EngToBrArr[7] = "h"
EngToBrArr[8] = "i"
EngToBrArr[9] = "j"
EngToBrArr[10] = "k"
EngToBrArr[11] = "l"
EngToBrArr[12] = "m"
EngToBrArr[13] = "n"
EngToBrArr[14] = "o"
EngToBrArr[15] = "p"
EngToBrArr[16] = "q"
EngToBrArr[17] = "r"
EngToBrArr[18] = "s"
EngToBrArr[19] = "t"
EngToBrArr[20] = "u"
EngToBrArr[21] = "v"
EngToBrArr[22] = "w"
EngToBrArr[23] = "x"
EngToBrArr[24] = "y"
EngToBrArr[25] = "z"
EngToBrArr[26] = " "

EngToBrArrIndexReference[0] = 1
EngToBrArrIndexReference[1] = 101
EngToBrArrIndexReference[2] = 11
EngToBrArrIndexReference[3] = 1011
EngToBrArrIndexReference[4] = 1001
EngToBrArrIndexReference[5] = 111
EngToBrArrIndexReference[6] = 1111
EngToBrArrIndexReference[7] = 1101
EngToBrArrIndexReference[8] = 110
EngToBrArrIndexReference[9] = 1110
EngToBrArrIndexReference[10] = 10001
EngToBrArrIndexReference[11] = 10101
EngToBrArrIndexReference[12] = 10011
EngToBrArrIndexReference[13] = 11011
EngToBrArrIndexReference[14] = 11001
EngToBrArrIndexReference[15] = 10111
EngToBrArrIndexReference[16] = 11111
EngToBrArrIndexReference[17] = 11101
EngToBrArrIndexReference[18] = 10110
EngToBrArrIndexReference[19] = 11110
EngToBrArrIndexReference[20] = 110001
EngToBrArrIndexReference[21] = 110101
EngToBrArrIndexReference[22] = 101110
EngToBrArrIndexReference[23] = 110011
EngToBrArrIndexReference[24] = 111011
EngToBrArrIndexReference[25] = 111001
EngToBrArrIndexReference[26] = 0


//for numbers, i'm doing to use an object

const translationNumbers = {
    1: "000001",
    2: "000101",
    3: "000011",
    4: "001011",
    5: "001001",
    6: "000111",
    7: "001111",
    8: "001101",
    9: "000110",
    0: "001110"
    //made them all strings becuase i dont want to code the logic to not to.
}
// console.log(getKey(translationNumbers, "000001"));
// console.log(translationNumbers[0]);

function isNumber(c) {
    return !isNaN(c);
}
// console.log(isNumber("h"))
// console.log(isNumber("4"))




function translateEngToBr(str){
    let brailMessage = "";
    let firstIterationOfNumber = true;
    
    for (let i = 0; i< str.length; i++){
        let englishLetter = str[i];
        // console.log(englishLetter)
        
        if(englishLetter === " "){
            firstIterationOfNumber = true; //reset because there is a space.
        }
        //lets handle numbers
        if(isNumber(englishLetter) && englishLetter !== " "){
          //were handling numbers now
          //englishLetter is a number
          const brailleNumber = translationNumbers[parseInt(englishLetter)];
        //   console.log("parseInt(englishLetter)", parseInt(englishLetter))
        //   console.log("brailleNumber", brailleNumber)

          const brailNumberText = convertBrailledigits(brailleNumber);
           if(firstIterationOfNumber){
            firstIterationOfNumber = false;
            brailMessage += ".O.OOO";
           }
           brailMessage += brailNumberText;
           continue;
        }
        //for letters
        //let englishLetter = str[i];
        const isCapitalized = isUpperCase(englishLetter);
        englishLetter = englishLetter.toLowerCase();
        const brailleIndex = EngToBrArr.indexOf(englishLetter);
        const brailleNumber = EngToBrArrIndexReference[brailleIndex];

        let prepend = ".".repeat(6 - String(brailleNumber).length)
        const brailLetterwrongFlipped = convertBrailledigits(String(brailleNumber))
        let correctBrailLetter = flipString(prepend + brailLetterwrongFlipped);
        if(isCapitalized && englishLetter !== " "){
            correctBrailLetter = ".....O" + correctBrailLetter;
        }
        brailMessage += correctBrailLetter
    }
    return brailMessage;
}
// console.log(translateEngToBr("Hello world"));
// console.log(translateEngToBr("Hello world 42"));


function getKey(obj, value) {
    for (let key in obj) {
        if (obj[key] === value) {
            return key;
        }
    }
    return null; //hopefully this doesnt ever reach
}



//DONE
//need to add number functionality
function translateBrToEng(str){
    if(str.length % 6 !== 0){
        return "invalid braille string, please try again";
    }

    let capitalize = false;
    let decryptedMessage = "";
    let isNumber = false;
    let firstIterationOfNumber = true;
    for (let i = 0; i < str.length; i += 6) {
        const letter = flipString(str.slice(i, i + 6));
        if(letter === "......"){ //if we reach a space, no more dealing with numbers
            isNumber = false;
        }
        if(letter === "OOO.O." || isNumber){
            //we're not dealing with numbers now
            isNumber = true; //let it to true or keep it true;
            if(firstIterationOfNumber === true){ //to skip 1 iteration
                firstIterationOfNumber = false;
                continue
            }
            const brailNumber = convertBrailToNumber(letter); //return 0 and 1 version of the brain. Where O = 1 and 0 = . this returns a string
            const num = getKey(translationNumbers, brailNumber) //returns key representing the number
            const letterNumber = String(num);

            decryptedMessage += letterNumber;
            continue;
        }
        
        //if it's a letter
        const num = computeEngLetter(letter);

        if(num === 100000){ //100000 represents capital follows.
            capitalize = true;
            continue //no need to add anything, skip current iteration
        }

        if(capitalize){
            decryptedMessage += engLetters[num].toUpperCase();
            capitalize = false; //set it back to false
        }
        else{
            decryptedMessage += engLetters[num];
        }
    }
    // console.log(decryptedMessage)
}
// translateBrToEng(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
// translateBrToEng(".O.OOOOO.O..O.O..............OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");




if (!process.argv[2]){
    return "Please enter a valid String";
}else{
    const tempArr = process.argv.slice(2);
    const userString = tempArr.join(" ");
    if(natureOfString(process.argv[2])){ //if it returns true, it means the string is english
       console.log(translateEngToBr(userString));
    }else{
        console.log(translateBrToEng(userString));
    }
}
 



