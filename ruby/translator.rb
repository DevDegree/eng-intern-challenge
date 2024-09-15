#Create a dictionary that defines the mapping of each letter to Braille
ALPHABET_BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..',  'e' => 'O..O..', 
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..', 
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.', 
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.', 
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO', 'z' => 'O..OOO'

  #Space -> Braille Empty
  ' ' => '......', 

  #Numbers
  '0' => '.....O', '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', 
  '5' => 'O..O..', '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...' 
}


# If Braille translation to english, invert the dictionary
BRAILLE_ALPHABET = ALPHABET_BRAILLE.invert

# If we encounter a number, we convert all following numbers to letters with hashmap
Braille_number = {
  'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
  'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
}


def braille_english(input)
    fulltranslation = ''
    is_capital = false
    is_number = false

    #Split each Braille string individually and process in chunks of 6
    braille.chars.each_slice(6) do |char|
        char = char.join
        if char == '.....O'   #Indication of cpaital letter
            is_capital = true
        
        elsif char == '.O.OOO'   #Indication of number
            is_number = true
        
        else
            translation = BRAILLE_TO_ENGLISH[char]  #No capital/number = call dictionary


            if is_capital
                translation = translation.upcase
                is_capital = false
            end

            if is_number
                translation =  Braille_number[translation] || translation


                #reset number if encountered space
                is_number = false if char == '......'
            end

            fulltranslation += translation
        end
    end
    
    fulltranslation
end

def english_braille(input)
    result = ''

    input.each_char do |char|

        #UpperCase
        if char.match?(/[A-Z]/)  
            result += '.....O'
            char = char.downcase
        end

        #Numbers
        if char.match?(/[0-9]/)
            result += '.O.OOO'

            #Map 0-9 to a-j (invert the hasmap)
            char = Braille_number.invert
        end

        #Translation
        fulltranslation += ALPHABET_BRAILLE[char]
    end
    fulltranslation
end

