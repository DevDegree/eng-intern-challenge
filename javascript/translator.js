//class that keeps track of the space and capitalize actions
class TokenModifier {
    static Capitalize = new TokenModifier(0b000001)
    static Number = new TokenModifier(0b010111)

    // find the token modifier that matches the value
    static GetModifierForToken(rawValue) {
        for (let tokenModifier in TokenModifier) {
            if (TokenModifier[tokenModifier].rawValue == rawValue) {
                return TokenModifier[tokenModifier]
            }
        }

        return null;
    } 
    
    constructor(value) {
        this.rawValue = value;
    }


    // makes sure that after the first usage of Capitalize and after a space the value is no longer a number
    ShouldExpire(rawValue, modifierTickCount) {
        if (this == TokenModifier.Number) {
            return Offsets[rawValue] == -64; // -64 is the offset value of space
        }
        return this == TokenModifier.Capitalize && modifierTickCount > 0;
    }
}

//class that keeps track of all the tokens
class Token {
    constructor(value, tokenModifier) {
        this.value = value;
        this.tokenModifier = tokenModifier;
    }

    // return the character corresponding to the value of token
    GetCharacter() {
        let baseChar = 'a'.charCodeAt(0) - 1;
        if (this.tokenModifier == null) return String.fromCharCode(baseChar + Offsets[this.value]);
        switch (this.tokenModifier) {
            case TokenModifier.Capitalize:
                return String.fromCharCode(64 + Offsets[this.value]);  // 'A' = 65
            case TokenModifier.Number:
                return Offsets[this.value] % 10;  
            default:
                return String.fromCharCode(baseChar + Offsets[this.value]);
        }
    }
}

// Fixed Offset values for Braille to English characters
let Offsets = {
    0b000000: -64, // ' '
    0b100000: 1,   // 'a'
    0b101000: 2,   // 'b'
    0b110000: 3,   // 'c'
    0b110100: 4,   // 'd'
    0b100100: 5,   // 'e'
    0b111000: 6,   // 'f'
    0b111100: 7,   // 'g'
    0b101100: 8,   // 'h'
    0b011000: 9,   // 'i'
    0b011100: 10,  // 'j'
    0b100010: 11,  // 'k'
    0b101010: 12,  // 'l'
    0b110010: 13,  // 'm'
    0b110110: 14,  // 'n'
    0b100110: 15,  // 'o'
    0b111010: 16,  // 'p'
    0b111110: 17,  // 'q'
    0b101110: 18,  // 'r'
    0b011010: 19,  // 's'
    0b011110: 20,  // 't'
    0b100011: 21,  // 'u'
    0b101011: 22,  // 'v'
    0b011101: 23,  // 'w'
    0b110011: 24,  // 'x'
    0b110111: 25,  // 'y'
    0b100111: 26,  // 'z'
    0b001101: -50,   // '.'
};

// convert Braille to English
function translateToEnglish(input){
    if (input.length % 6 != 0) {
        return "Invalid Braille string length.";
    }
    
    const rawTokens = input.match(/.{6}/g)
    
    let tokens = []
    let currModifier = null; 
    let modifierTickCount = 0;
    
    // Convert 'O' and '.' to binaryToken
    for(let i = 0; i < rawTokens.length; i++) {
        let tokenStr = rawTokens[i];

        // braille to binary
        let binaryToken = 0b000000
        for(let j = 0; j < tokenStr.length; j++) {
            if (tokenStr[j] === 'O'){
                binaryToken |= 1 << (5 - j); 
            }
        }
        
        // purge modifier if needed
        if (currModifier != null && currModifier.ShouldExpire(binaryToken, modifierTickCount++)) {
            currModifier = null;
            modifierTickCount = 0;
        }

        // consume modifier
        let newModifier = TokenModifier.GetModifierForToken(binaryToken)
        if (newModifier != null) {
            modifierTickCount = 0;
            currModifier = newModifier;
            continue;
        }

        // create token
        tokens.push(new Token(binaryToken, currModifier))
    }

    // join all the characters from the array into string 
    return tokens.map((token) => token.GetCharacter()).join('');;
}

// find key based on value
function findKeyOf(char){
    return Object.keys(Offsets).find(key => Offsets[key] == char)
}

// convert binary to braille
function convertFromBinaryToBraille(value){
    let brailleStr = "";
    for(let j = 0; j < 6; j++) {
        brailleStr += (value & 1 << (5 - j)) > 0 ? 'O' : '.'; 
    }
    return brailleStr;
}

//convert English to Braille
function translateToBraille(input){
    let baseChar = 'a'.charCodeAt(0) - 1;
    let braille = "";
    var currentMod = null;

    //Convert each character to braille
    for(let i = 0; i < input.length; i++){
        let char = input[i];
        let charCode = char.charCodeAt(0);
        let binaryPattern = ""
        
        // process number
        let charNum = parseInt(char);
        if (!isNaN(charNum)){
            if (currentMod != TokenModifier.Number) {
                braille += convertFromBinaryToBraille(TokenModifier.Number.rawValue)
            }
            
            currentMod = TokenModifier.Number;
            charNum = charNum == 0 ? 10 : charNum;
            binaryPattern = findKeyOf(charNum);
        } 
        // process uppercase
        else if (charCode >= 65 && charCode <= 90) {
            braille += convertFromBinaryToBraille(TokenModifier.Capitalize.rawValue)
            currentMod = TokenModifier.Capitalize;
            binaryPattern = findKeyOf(charCode - ('A'.charCodeAt(0) - 1));
        } 
        // process lower and space
        else {
            currentMod = null;
            binaryPattern = findKeyOf(charCode - baseChar);
        }
        
        // construct braille from binary
        braille += convertFromBinaryToBraille(binaryPattern)
    }

    return braille
}

// detect if the output is english or braille
function detectInputType(input) {
    return input.match(/^[O.]+$/) ? 'braille' : 'english';
}

// Main function to handle translation
function main() {
     const input = process.argv.slice(2).join(' ');
     const inputType = detectInputType(input);

     console.log(inputType === 'english'? translateToBraille(input) : translateToEnglish(input));
}

 main();