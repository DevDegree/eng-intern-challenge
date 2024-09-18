const braille_to_alpha_num = {
    "O.....": 'A',
    "O.O...": 'B',
    "OO....": 'C',
    "OO.O..": 'D',
    "O..O..": 'E',
    "OOO...": 'F',
    "OOOO..": 'G',
    "O.OO..": 'H',
    ".OO...": 'I',
    ".OOO..": 'J',
    "O...O.": 'K',
    "O.O.O.": 'L',
    "OO..O.": 'M',
    "OO.OO.": 'N',
    "O..OO.": 'O',
    "OOO.O.": 'P',
    "OOOOO.": 'Q',
    "O.OOO.": 'R',
    ".OO.O.": 'S',
    ".OOOO.": 'T',
    "O...OO": 'U',
    "O.O.OO": 'V',
    ".OOO.O": 'W',
    "OO..OO": 'X',
    "OO.OOO": 'Y',
    "O..OOO": 'Z',
};
const alpha_to_braille = {
}

Object.keys(braille_to_alpha_num).forEach((value)=>{
    alpha_to_braille[braille_to_alpha_num[value]] = value;
})
//console.log(alpha_to_braille);

const capital = ".....O";
const decimal = ".O..O.";
const number = ".O.OOO";

let  numberMode = false;
let capitalMode = false;

function BrailleToAlpha(phrase){
    let ret = "";
    for(let i = 0; i < phrase.length/6;i++){
        let braileSymbol = phrase.substring(i*6, i*6 + 6);
        if(braileSymbol === capital){
            capitalMode = true;
        }else if(braileSymbol == number){
            numberMode = true;
        }else{
            if(braileSymbol === '......'){
                ret = ret + ' ';
                numberMode = false;
                capitalMode = false;
            }
            else if(numberMode){
                //console.log(((braille_to_alpha_num[braileSymbol]).charCodeAt() - 64));
                ret = ret + ((braille_to_alpha_num[braileSymbol]).charCodeAt() - 64)%10;
            }else{
                let letter =  (braille_to_alpha_num[braileSymbol]);
                if (!capitalMode){
                    letter = letter.toLowerCase();
                }
                ret = ret + letter;
                capitalMode = false;
            }
        }
    }
    return ret;
}

function AlphaToBraille(phrase){
    let ret = "";
    let numberMode = false;
    for(let i = 0;i< phrase.length;i++){
        let char = phrase.charAt(i);
        if(char == ' '){
            ret = ret + "......";
            numberMode = false;
        }else{
            if('0' <= char && '9' >= char){
                if(!numberMode){
                    ret += number;
                    numberMode = true;
                }
                if(char == '0') {
                    ret += alpha_to_braille["J"]
                }else{
                    //console.log(parseInt(char - '1') + 65);
                    ret += alpha_to_braille[String.fromCharCode(parseInt(char - '1') + 65)];
                }
            }else{
                if(char.toLowerCase() !== char){
                    ret += capital;
                }
                char = char.toUpperCase();
                ret += alpha_to_braille[char];
            }
        }
    }
    return ret;
}

const args = process.argv.slice(2);
let input = "";
args.forEach((value) => input += " " + value)
input = input.trim();
let alpha = false;
for(let i = 0;i < input.length;i++){
    let char = input.charAt(i);
    if(!(char == '.' || char == 'O'))alpha = true;
}
let ret = "";
if(alpha)ret = AlphaToBraille(input);
else ret = BrailleToAlpha(input);
console.log(ret);