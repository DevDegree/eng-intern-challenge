# Mapping of alphabet letters to their Braille representations
ALPHABET_TO_BRAILLE = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..",
  "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.",
  "o" => "O..OO.", "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.", "u" => "O...OO",
  "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO", "z" => "O..OOO",
  "capital" => ".....O",  # Braille representation for capital letters
  " " => "......"  # Braille representation for space
}

# Mapping of numbers to their Braille representations
NUMBER_TO_BRAILLE = {
  "number" => ".O.OOO",  # Braille representation for indicating a number sequence
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...",
  "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", " " => "......"  # Braille representation for space
}

# Invert the mappings for translation from Braille to Alphabet/Number
BRAILLE_TO_ALPHABET = ALPHABET_TO_BRAILLE.invert
BRAILLE_TO_NUMBER = NUMBER_TO_BRAILLE.invert

# Function to translate text to Braille
def translate_to_braille(text)
  result = ''
  number_sequence = false  # Flag to track if the current sequence is a number

  text.chars.each do |char|
    if char.match(/[A-Z]/)  # Check if the character is an uppercase letter
      result += (ALPHABET_TO_BRAILLE['capital']) + (ALPHABET_TO_BRAILLE[char.downcase])
      number_sequence = false
    elsif char.match(/\d/)  # Check if the character is a digit
      if !number_sequence
        result += NUMBER_TO_BRAILLE['number']
        number_sequence = true
      end
      result += (NUMBER_TO_BRAILLE[char])
    else  # For alphabetic characters or space
      result += (ALPHABET_TO_BRAILLE[char] || ALPHABET_TO_BRAILLE[' '])
      number_sequence = false
    end
  end
  result
end

# Function to translate Braille text back to English
def translate_to_english(input)
  solution = ""
  check_capital = false  # Flag to determine if the next character should be capitalized
  number_mode = false  # Flag to determine if the current mode is number mode
  curr_string = ''  # Accumulator for Braille characters

  input.each_char do |char|
    curr_string += char

    if curr_string.length == 6  # Braille characters are 6 dots long
      if curr_string == ALPHABET_TO_BRAILLE['capital']  # Check if the current string is the capital indicator
        check_capital = true
      elsif curr_string == NUMBER_TO_BRAILLE['number']  # Check if the current string is the number indicator
        number_mode = true
      else
        if curr_string == ALPHABET_TO_BRAILLE[" "] && number_mode # Check if it's the end of the sequence of numbers
          char = BRAILLE_TO_ALPHABET.fetch(curr_string, '')
          number_mode = false
        elsif number_mode # Translate digits
          char = BRAILLE_TO_NUMBER.fetch(curr_string, '')
        else # Translate alphabet
          char = BRAILLE_TO_ALPHABET.fetch(curr_string, '')
          if check_capital
            char = char.upcase  # Capitalize the character if needed
            check_capital = false
          end
        end
        solution += char
      end
      curr_string = ''  # Reset the accumulator for the next Braille character
    end
  end
  solution
end

# Function to determine if the input contains Braille characters
def determine_input_type(input)
  input.include?('O') || input.include?('.')
end

# Main function to handle command-line arguments and execute translation
def main(args)
  input = args.join(' ')  # Combine arguments into a single string

  if determine_input_type(input)
    puts translate_to_english(input)
  else
    puts translate_to_braille(input)
  end
end

# Command-line execution with a sample input
main([".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"])
