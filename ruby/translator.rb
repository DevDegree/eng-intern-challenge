#Create a dictionary that defines the mapping of each letter/digits to Braille representations
ALPHABET_BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO', 'z' => 'O..OOO',
  
  #Space for empty braille
  ' ' => '......'
}

# Invert dictionary to translate Braille to English
BRAILLE_ALPHABET = ALPHABET_BRAILLE.invert

#Number representations uses letters from 'a' to 'j'
ALPHABET_NUMBER = {
  'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
  'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
}

#Map 0-9 to a-j (invert the hashmap to map digits to letter in Braille)
NUMBER_ALPHABET = ALPHABET_NUMBER.invert


#Function translates Braille to English
def braille_english(input)
    fulltranslation = ''
    is_capital = false
    is_number = false

    #Split each Braille in chunks of 6 characters [2 x 3 matrix]
    input.chars.each_slice(6) do |char|
        char = char.join

        if char == '.....O'   #Indication of capital letter
            is_capital = true
        
        elsif char == '.O.OOO'   #Indication of number
            is_number = true
        
        else
            translation = BRAILLE_ALPHABET[char]  #Look up braille characters in dictionary


            if is_capital
                translation = translation.upcase
                is_capital = false
            end

            if is_number
                translation =  ALPHABET_NUMBER[translation] || translation #Map to digit or keep as is (nil cases)
                
                #reset number if encountered space
                if char == '......'
                    is_number = false
                end
            end

            fulltranslation += translation


        end
    end
    
    fulltranslation
end


#Function translates English to Braille
def english_braille(input)
    fulltranslation = ''
    is_number = false

    input.each_char do |char|

        if char.match?(/[A-Z]/)  
            fulltranslation += '.....O'   #Indicates capital letter
            char = char.downcase
            is_number = false
        end

        #Indicates Numbers
        if char.match?(/[0-9]/)
            unless is_number
                fulltranslation += '.O.OOO'
                is_number = true
            end

            char = NUMBER_ALPHABET[char]
        else
            is_number = false
        end

        #Translation
        fulltranslation += ALPHABET_BRAILLE[char] || char #Braille translation or keep as is (handles nil cases)
    end
    fulltranslation
end

#Determine if argument line is in Braille or English
def translate(input)
    if input.match?(/[O.]/)
        braille_english(input)
    else
        english_braille(input)
    end
end



#Handle command line input
if __FILE__ == $0
    input = ARGV.join(' ')
    puts translate(input)
end