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


def handleNumber (translation)

    #Convert letters A to J to 1 to 0
    if translation >= 'a' && translation <= 'j'
        translation = (translation.ord - 'a'.ord + 1).to_s
      elsif translation == 'j'
        translation = '0' # If 'j' is 0
      end
      translation
end


def handleCapital(translation)
    translation.upcase
end

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
                translation = handleCapital(translation)
                is_capital = false
            end

            if is_number
                translation = handleNumber(translation)

                #reset number if encountered space
                is_number = false if char == '......'
            end

            fulltranslation += translation
        end
    end
    
    fulltranslation
end






#Determine if argument line is in Braille or English
def translate(input)
    if input.match?(/[O.]/)
        braille_english
    else
        english_braille
    end
end



        
