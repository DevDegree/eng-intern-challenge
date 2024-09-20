# Map for English to Braille
ENGL_TO_BRAI_LETTERS_SPEICAL = {
  'a' => 'O.....', 
  'b' => 'O.O...', 
  'c' => 'OO....', 
  'd' => 'OO.O..', 
  'e' => 'O..O..',
  'f' => 'OOO...', 
  'g' => 'OOOO..', 
  'h' => 'O.OO..', 
  'i' => '.OO...', 
  'j' => '.OOO..',
  'k' => 'O...O.',
  'l' => 'O.O.O.', 
  'm' => 'OO..O.', 
  'n' => 'OO.OO.', 
  'o' => 'O..OO.',
  'p' => 'OOO.O.', 
  'q' => 'OOOOO.', 
  'r' => 'O.OOO.', 
  's' => '.OO.O.', 
  't' => '.OOOO.',
  'u' => 'O...OO', 
  'v' => 'O.O.OO', 
  'w' => '.OOO.O', 
  'x' => 'OO..OO', 
  'y' => 'OO.OOO',
  'z' => 'O..OOO',  
  'capital' => '.....O', 
  'decimal' => ".O...O",
  'number' => '.O.OOO',
  '.' => '..OO.O',
  ',' => '..O...',
  '?' => '..O.OO',
  '!' => '..OOO.',
  ':' => '..OO..',
  ';' => '..O.O.',
  '-' => '....OO',
  '/' => '.O..O.',
  '<' => '.O.O.O',
  '>' => 'O.O.O.',
  '(' => 'O.O..O',
  ')' => '.O.OO.',
  ' ' => '......'
}

ENGL_TO_BRAI_NUMBERS = {
    '1' => 'O.....', 
    '2' => 'O.O...', 
    '3' => 'OO....',
    '4' => 'OO.O..', 
    '5' => 'O..O..', 
    '6' => 'OOO...', 
    '7' => 'OOOO..', 
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..', 
}

# Map for Braille to English
BRAI_TO_ENGL_LETTERS_SPEICAL = ENGL_TO_BRAI_LETTERS_SPEICAL.invert

BRAI_TO_ENGL_NUMBERS = ENGL_TO_BRAI_NUMBERS.invert


def translate_to_braille(english)
    result = ''
    number = false
  
    english.chars.each do |char|
        # Add capital braille before uppercase letters
        if char.match?(/[A-Z]/)
            result += ENGL_TO_BRAI_LETTERS_SPEICAL['capital'] + ENGL_TO_BRAI_LETTERS_SPEICAL[char.downcase]
            number = false
        # Add number braille at start of the number
        elsif char.match?(/\d/)
            unless number
            result += ENGL_TO_BRAI_LETTERS_SPEICAL['number']
            number = true
            end
            result += ENGL_TO_BRAI_NUMBERS[char]

        # Add decimal braille for decimal numbers
        elsif char == '.'
            if number
                result += ENGL_TO_BRAI_LETTERS_SPEICAL['decimal']
            else # When decimal appears without number bool
                result += ENGL_TO_BRAI_LETTERS_SPEICAL['number'] + ENGL_TO_BRAI_LETTERS_SPEICAL['decimal']
                number = true
            end 
        else
            result += ENGL_TO_BRAI_LETTERS_SPEICAL[char]
            number = false
        end
    end
    result
end

def translate_to_english(braille)
    result = ''
    chars = braille.scan(/.{6}/)
    capitalize = false
    number = false
  
    chars.each do |char|
        # If char is a capital
        if char == ENGL_TO_BRAI_LETTERS_SPEICAL['capital']
            capitalize = true
            next
        
        # If char is a number
        elsif char == ENGL_TO_BRAI_LETTERS_SPEICAL['number']
            number = true
            next

        # If char is a decimal
        elsif char == ENGL_TO_BRAI_LETTERS_SPEICAL['decimal'] && number
            result += '.'
            next
        
        #If char is a space
        elsif char == '......'
            result += ' '
            number = false 
            next
        end
  
        if number  # Translate as a number
            result += BRAI_TO_ENGL_NUMBERS[char]
        else # Translate as a letter, and handle capitalization
            letter = BRAI_TO_ENGL_LETTERS_SPEICAL[char]
            result += capitalize ? letter.upcase : letter
            capitalize = false
        end
    end
  
    result
end
  

def main
    if ARGV.empty?
      exit
    end

    input = ARGV.join(' ')
    
    if input.chars.all? { |char| char == 'O' || char == '.'} && input.length >= 6 && input.length % 6 == 0
      # Input is Braille
      puts translate_to_english(input)
    else
      # Input is English
      puts translate_to_braille(input)
    end
  end
  
  main if __FILE__ == $PROGRAM_NAME
