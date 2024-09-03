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

//just to help me copy paste all of the thing below because im too lazy to write it all
// const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// for(let i = 0; i<26; i++){
//     console.log(`engLetters[${i}] = \"${alphabet[i]}\"`)
// }

//computeEngLetter("O...OO")
const engLetters = new Array(111111)
//now we translate
engLetters[0] = " "; //space character
engLetters[1] = "A"
engLetters[101] = "B"
engLetters[11] = "C"
engLetters[1011] = "D"
engLetters[1001] = "E"
engLetters[111] = "F"
engLetters[1111] = "G"
engLetters[1101] = "H"
engLetters[110] = "I"
engLetters[1110] = "J"
engLetters[10001] = "K"
engLetters[10101] = "L"
engLetters[10011] = "M"
engLetters[11011] = "N"
engLetters[11001] = "O"
engLetters[10111] = "P"
engLetters[11111] = "Q"
engLetters[11101] = "R"
engLetters[10110] = "S"
engLetters[11110] = "T"
engLetters[110001] = "U"
engLetters[110101] = "V"
engLetters[101110] = "W"
engLetters[110011] = "X"
engLetters[111011] = "Y"
engLetters[111001] = "Z"

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
//     //console.log(`EngToBrArr[${i}] = \"${alphabet[i]}\"`)
//     console.log(`EngToBrArrIndexReference[${i}] = ${engLetters.indexOf(alphabet[i])}`)
// }
EngToBrArr[0] = "A"
EngToBrArr[1] = "B"
EngToBrArr[2] = "C"
EngToBrArr[3] = "D"
EngToBrArr[4] = "E"
EngToBrArr[5] = "F"
EngToBrArr[6] = "G"
EngToBrArr[7] = "H"
EngToBrArr[8] = "I"
EngToBrArr[9] = "J"
EngToBrArr[10] = "K"
EngToBrArr[11] = "L"
EngToBrArr[12] = "M"
EngToBrArr[13] = "N"
EngToBrArr[14] = "O"
EngToBrArr[15] = "P"
EngToBrArr[16] = "Q"
EngToBrArr[17] = "R"
EngToBrArr[18] = "S"
EngToBrArr[19] = "T"
EngToBrArr[20] = "U"
EngToBrArr[21] = "V"
EngToBrArr[22] = "W"
EngToBrArr[23] = "X"
EngToBrArr[24] = "Y"
EngToBrArr[25] = "Z"

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

// function translateEngToBr(str){

// }



function translateBrToEng(str){
    if(str.length % 6 !== 0){
        return "invalid braille string, please try again";
    }
    let decryptedMessage = "";
    for (let i = 0; i < str.length; i += 6) {
        const letter = str.slice(i, i + 6);
        // computeEngLetter(letter);
        decryptedMessage += engLetters[computeEngLetter(letter)];
    }
}
translateBrToEng("123456HELLOOBONJOULALALA")

