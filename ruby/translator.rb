ENGLISH_TO_BRAILLE = {
  characters: {
    'a' => "O.....", 'b' => "O.O...", 'c' => "OO....", 'd' => "OO.O..",
    'e' => "O..O..", 'f' => "OOO...", 'g' => "OOOO..", 'h' => "O.OO..",
    'i' => ".OO...", 'j' => ".OOO..", 'k' => "O...O.", 'l' => "O.O.O.",
    'm' => "OO..O.", 'n' => "OO.OO.", 'o' => "O..OO.", 'p' => "OOO.O.",
    'q' => "OOOOO.", 'r' => "O.OOO.", 's' => ".OO.O.", 't' => ".OOOO.",
    'u' => "O...OO", 'v' => "O.O.OO", 'w' => ".OOO.O", 'x' => "OO..OO",
    'y' => "OO.OOO", 'z' => "O..OOO", 'capital' => ".....O"
  },
  numbers: {
    '0' => ".....O", '1' => "O.....", '2' => "O.O...", '3' => "OO....",
    '4' => "OO.O..", '5' => "O..O..", '6' => "OOO...", '7' => "OOOO..",
    '8' => "O.OO..", '9' => ".OO...", 'number' => ".O.OOO"
  },
  special_chars: {
    ',' => ".O....", ';' => ".O.O..", ':' => ".OO...", '.' => ".OOO..",
    '!' => ".OO.O.", '?' => ".OOOO.", '-' => "O.....", '/' => "OO....",
    '>' => "OO.O..", '<' => "O..O..", '(' => "OOO...", ')' => "OOOO..",
    ' ' => "......"
  }
}

#invert above mapping to get the braille to english translations
BRAILLE_TO_ENGLISH = {
  characters: ENGLISH_TO_BRAILLE[:characters].invert,
  numbers: ENGLISH_TO_BRAILLE[:numbers].invert,
  special_chars: ENGLISH_TO_BRAILLE[:special_chars].invert
}

#check if the given input is braille (only contains '0' and '.')
def isBraille(input)
    input.each_char { |letter|
        if letter != 'O' &&  letter != '.'
            return false
        end
    }
    return true
end

#convert given input to braille from english
def convToBraille(input)
    englishAns = ""
    num_on = false

    input.each_char { |letter|
        # case 1 : is capital
        if(letter.match?(/[A-Z]/))
            num_on = false
            englishAns += ENGLISH_TO_BRAILLE[:characters]['capital']
            englishAns += ENGLISH_TO_BRAILLE[:characters][letter.downcase]
        # case 2 : is number
        elsif(letter.match?(/[0-9]/))
            unless num_on
                num_on = true
                englishAns += ENGLISH_TO_BRAILLE[:numbers]['number']
                englishAns += ENGLISH_TO_BRAILLE[:numbers][letter]
            else
                englishAns += ENGLISH_TO_BRAILLE[:numbers][letter]
            end
        # case 3 : lowercase letter
        elsif(letter.match?(/[a-z]/)) 
            num_on = false
            englishAns += ENGLISH_TO_BRAILLE[:characters][letter]
        #case 4 : special character
        else
            num_on = false
            englishAns += ENGLISH_TO_BRAILLE[:special_chars][letter]
        end
    }
    return englishAns
end


def convToEnglish(input)
    brailleAns = '';
    num_on = false
    cap_on = false

    #split the input into an array with 6 characters strings
    braille = input.scan(/.{1,6}/)
    braille.each { |letter|
    # case 1 : is capital flag 
    if letter == ENGLISH_TO_BRAILLE[:characters]['capital']
        cap_on = true
    # case 2 : capital letter
    elsif cap_on
        brailleAns += BRAILLE_TO_ENGLISH[:characters][letter].upcase
        cap_on = false
    # case 3 : num flag on and space
    elsif num_on && letter == ENGLISH_TO_BRAILLE[:special_chars][' ']
        num_on = false
    # case 4 : num flag on 
    elsif letter == ENGLISH_TO_BRAILLE[:numbers]['number']
        num_on = true
    # case 5 : number 
    elsif num_on 
        brailleAns += BRAILLE_TO_ENGLISH[:numbers][letter]
    # case 6 : space
    elsif letter == BRAILLE_TO_ENGLISH[:special_chars][' ']
        brailleAns += ' '
    elsif BRAILLE_TO_ENGLISH[:characters].key?(letter)
        brailleAns += BRAILLE_TO_ENGLISH[:characters][letter]
    elsif BRAILLE_TO_ENGLISH[:special_chars].key?(letter)
        brailleAns += BRAILLE_TO_ENGLISH[:special_chars][letter]
    end
}
    return brailleAns

end

def main(input)
    if(isBraille(input)) 
        puts convToEnglish(input)
    else 
        puts convToBraille(input)
    end
end