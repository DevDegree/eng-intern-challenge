# This file contains the implementation of a Braille translator that can translate English text to Braille and vice versa.


# Braille representation of alphabets
ALPHABET_DICT = {
    'a' => 'O.....', 'b' => 'O.O...', 
    'c' => 'OO....', 'd' => 'OO.O..', 
    'e' => 'O..O..', 'f' => 'OOO...', 
    'g' => 'OOOO..', 'h' => 'O.OO..',
    'i' => '.OO...', 'j' => '.OOO..',
    'k' => 'O...O.', 'l' => 'O.O.O.',
    'm' => 'OO..O.', 'n' => 'OO.OO.',
    'o' => 'O..OO.', 'p' => 'OOO.O.',
    'q' => 'OOOOO.', 'r' => 'O.OOO.',
    's' => '.OO.O.', 't' => '.OOOO.',
    'u' => 'O...OO', 'v' => 'O.O.OO',
    'w' => '.OOO.O', 'x' => 'OO..OO',
    'y' => 'OO.OOO', 'z' => 'O..OOO',
    'capital' => '.....O', 'number' => '.O.OOO', 
    ' ' => '......', 
}

# Braille representation of numbers
NUMBER_DICT = {
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..'
}


# Invert the dictionaries to get the reverse mapping
BRAILLE_ALPHABET = ALPHABET_DICT.invert
BRAILLE_NUMBER = NUMBER_DICT.invert


# Helper function to check if a character is a digit
def is_digit?(char)
    char.match?(/\d/)
end

# Helper function to check if a character is uppercase
def is_upper_case?(char)
    char.match?(/[A-Z]/)
end

# Helper function to get Braille representation (alphabet)
def get_braille_representation_alphabet(char)
    ALPHABET_DICT.fetch(char, '......')
end

# Helper function to get Braille representation (number)
def get_braille_representation_number(char)
    NUMBER_DICT.fetch(char, '......')
end

def translate_to_braille(text)
    solution = ""
    number_mode = false
    
    # Iterate through the input text and translate each character
    text.each_char do |char|
    if is_upper_case?(char) # Check if the character is uppercase
        solution += get_braille_representation_alphabet('capital')
        solution += get_braille_representation_alphabet(char.downcase)
        number_mode = false
    elsif is_digit?(char) # Check if the character is a digit
        unless number_mode
            solution += get_braille_representation_alphabet('number')
            number_mode = true
        end
        solution += get_braille_representation_number(char)
    else # Translate the character
        number_mode = false if number_mode && char == ' ' # Reset number mode on encountering a space
        solution += get_braille_representation_alphabet(char)
    end
  end

  solution
end

def translate_to_english(braille)
    solution = ""
    check_capital = false # Variable checking if the current context is a capital letter
    number_mode = false # Variable checking if the current context is numeric
    curr_string = '' 
    # Iterate through the Braille string and translate each character
    braille.each_char do |char|
        curr_string += char
        if curr_string.length == 6 # Check if the current string is a full Braille character
            if curr_string == get_braille_representation_alphabet('capital') # Check if the current string is a capital letter
                check_capital = true # Set check_capital flag
            elsif curr_string == get_braille_representation_alphabet('number') # Check if the current string is a number
                number_mode = true # Set number mode
            else
                if number_mode
                    char = BRAILLE_NUMBER.fetch(curr_string, '') # Translate the number
                else
                    char = BRAILLE_ALPHABET.fetch(curr_string, '')
                    if check_capital
                        char = char.upcase
                        check_capital = false  # Reset check_capital after using it
                    end
                end
                solution += char # Append the translated character to the solution
            end
            curr_string = '' # Reset the current string after processing
        end
    end
  
    solution # Return the translated string
  end


# Main function to handle input and call translation functions
def main
    if ARGV.empty?
        puts "Usage: ruby translator.rb <text_or_braille>"
        return
    end

    input_text = ARGV.join(' ')

    # Determine if input is Braille or text and translate accordingly
    if input_text.gsub(' ', '').chars.all? { |char| 'O.'.include?(char) }
        puts translate_to_english(input_text)
    else
        puts translate_to_braille(input_text)
    end
end
  
main