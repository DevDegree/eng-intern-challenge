let cap = false;
let num = false;

let braille = false;
let output = "";
function translator() {
    var args = process.argv.slice( 2 ).join( " " );
    if ( inputValidator( args ) ) {
        brailleInput( args );
        braille = true;
    } else englishInput( args );
}

translator();

function inputValidator( input ) {
    for ( let i = 0; i < input.length; i++ ) {
        if ( input[i] != "O" && input[i] != "." ) return false;
    }
    braille = true;
    return true;
}

function indicator( char ) {
    if ( !braille && !num ) {
        const ascii = char.charCodeAt( 0 );
        if ( ascii >= 48 && ascii <= 57 ) {
            num = true;
            output += ".O.OOO";
            return true;
        }
    }

    if ( braille ) {
        let capital = ".....O";
        let number = ".O.OOO";
        if ( char == capital || char == number ) {
            if ( char == capital ) cap = true;
            if ( char == number ) num = true;
            return true;
        } 
    } else return false;
}

function brailleInput(input ) {
    while ( input ) {
        let char = input.substring( 0, 6 );
        if ( indicator(char ) ) {
            input = input.substring( 6 );
            if ( num ) {
                input = brailleToNumber( input );
                num = false;
            }
        } 
        input = brailleToEnglish( input );
    }
    console.log( output );
}

function englishInput( input ) {
    while ( input ) {
        let char = input.substring( 0, 1 );
        indicator( char );
        if ( num ) {
            input = numberToBraille( input );
            num = false;
        }
        input = englishToBraille( input );
    }
    console.log( output );
}

function brailleToNumber( input ) {
    let word = input;
    let char = word.substring( 0, 6 );
    while (word && char != "......" ) {
        word = word.substring( 6 );
        switch(char ) {
            case "O.....":
                output += "1";
                break;
            case "O.O...":
                output += "2";
                break;
            case "OO....":
                output += "3";
                break;
            case "OO.O..":
                output += "4";
                break;
            case "O..O..":
                output += "5";
                break;
            case "OOO...":
                output += "6";
                break;
            case "OOOO..":
                output += "7";
                break;
            case "O.OO..":
                output += "8";
                break;
            case ".OO...":
                output += "9";
                break;
            case ".OOO..":
                output += "0";
                break;
            default:
                break;
        }
        char = word.substring( 0, 6 );
    }
    return word;
}

function brailleToEnglish( input ) {
    let word = input;
    let letter = "";
    let charBraille = word.substring( 0, 6 );
    
    while ( word && charBraille && !num ) {
        word = word.substring( 6 );
        let compare = charBraille.substring( 0, 4 );
        switch( compare ) {
            case "O...":
                if ( charBraille == "O....." ) letter = "a";
                if ( charBraille == "O...O." ) letter = "k";
                if ( charBraille == "O...OO" ) letter = "u";
                break;
            case "O.O.":
                if ( charBraille == "O.O..." ) letter = "b";
                if ( charBraille == "O.O.O." ) letter = "l";
                if ( charBraille == "O.O.OO" ) letter = "v";
                break;
            case "OO..":
                if ( charBraille == "OO...." ) letter = "c";
                if ( charBraille == "OO..O." ) letter = "m";
                if ( charBraille == "OO..OO" ) letter = "x";
                break;
            case "OO.O":
                if ( charBraille == "OO.O.." ) letter = "d";
                if ( charBraille == "OO.OO." ) letter = "n";
                if ( charBraille == "OO.OOO" ) letter = "y";
                break;
            case "O..O":
                if ( charBraille == "O..O.." ) letter = "e";
                if ( charBraille == "O..OO." ) letter = "o";
                if ( charBraille == "O..OOO" ) letter = "z";
                break;
            case "OOO.":
                if ( charBraille == "OOO..." ) letter = "f";
                if ( charBraille == "OOO.O." ) letter = "p";
                break;
            case "OOOO":
                if ( charBraille == "OOOO.." ) letter = "g";
                if ( charBraille == "OOOOO." ) letter = "q";
                break;
            case "O.OO":
                if ( charBraille == "O.OO.." ) letter = "h";
                if ( charBraille == "O.OOO." ) letter = "r";
                break;
            case ".OO.":
                if ( charBraille == ".OO..." ) letter = "i";
                if ( charBraille == ".OO.O." ) letter = "s";
                break;
            case ".OOO":
                if ( charBraille == ".OOO.." ) letter = "j";
                if ( charBraille == ".OOOO." ) letter = "t";
                if ( charBraille == ".OOO.O" ) letter = "w";
                break;
            default:
                letter = " ";
                break;
        }
        if ( cap ) {
            letter = letter.toUpperCase();
            cap = false;
        }
        output += letter;
        charBraille = word.substring( 0, 6 );
        indicator( charBraille );
    }
    return word;
}

function numberToBraille( input ) {
    let word = input;
    let char = word.substring( 0, 1 );
    while ( word && char != " " ) {
        word = word.substring( 1 );
        switch( char ) {
            case "1":
                output += "O.....";
                break;
            case "2":
                output += "O.O...";
                break;
            case "3":
                output += "OO....";
                break;
            case "4":
                output += "OO.O..";
                break;
            case "5":
                output += "O..O..";
                break;
            case "6":
                output += "OOO...";
                break;
            case "7":
                output += "OOOO..";
                break;
            case "8":
                output += "O.OO..";
                break;
            case "9":
                output += ".OO...";
                break;
            case "0":
                output += ".OOO..";
                break;
            default:
                break;
        }
        char = word.substring( 0, 1 );
    }
    num = false;
    return word;
}

function englishToBraille( input ) {
    let word = input;
    
    let letter = word.substring( 0, 1 );
    
    while ( word ) {
        let braille = "";
        if ( num ) word = numberToBraille( word );
        else {
            word = word.substring( 1 );
            if ( letter == letter.toUpperCase() && letter != " " ) {
                output += ".....O";
                letter = letter.toLowerCase();
            }
        }
        
        switch( letter ) {
            case "a": case "k": case "u":
                braille = "O...";
                if ( letter == "a" ) braille += "..";
                if ( letter == "k" ) braille += "O.";
                if ( letter == "u" ) braille += "OO";
                break;
            case "b": case "l": case "v":
                braille = "O.O.";
                if ( letter == "b" ) braille += "..";
                if ( letter == "l" ) braille += "O.";
                if ( letter == "v" ) braille += "OO";
                break;
            case "c": case "m": case "x":
                braille = "OO..";
                if ( letter == "c" ) braille += "..";
                if ( letter == "m" ) braille += "O.";
                if ( letter == "x" ) braille += "OO";
                break;
            case "d": case "n": case "y":
                braille = "OO.O";
                if ( letter == "d" ) braille += "..";
                if ( letter == "n" ) braille += "O.";
                if ( letter == "y" ) braille += "OO";
                break;
            case "e": case "o": case "z":
                braille = "O..O";
                if ( letter == "e" ) braille += "..";
                if ( letter == "o" ) braille += "O.";
                if ( letter == "z" ) braille += "OO";
                break;
            case "f": case "p":
                braille = "OOO.";
                if ( letter == "f" ) braille += "..";
                if ( letter == "p" ) braille += "O.";
                break;
            case "g": case "q":
                braille = "OOOO";
                if ( letter == "g" ) braille += "..";
                if ( letter == "q" ) braille += "O.";
                break;
            case "h": case "r":
                braille = "O.OO";
                if ( letter == "h" ) braille += "..";
                if ( letter == "r" ) braille += "O.";
                break;
            case "i": case "s":
                braille = ".OO.";
                if ( letter == "i" ) braille += "..";
                if ( letter == "s" ) braille += "O.";
                break;
            case "j": case "t": case "w":
                braille = ".OOO";
                if ( letter == "j" ) braille += "..";
                if ( letter == "t" ) braille += "O.";
                if ( letter == "w" ) braille += ".O";
                break;
            default:
                if ( letter == " " ) braille = "......";
                break;
        }
        output += braille;
        letter = word.substring( 0, 1 );
        indicator( letter );
    }
    return word;
}
