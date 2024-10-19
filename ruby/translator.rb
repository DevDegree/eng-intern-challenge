# This file contains the implementation of a Braille translator that can translate English text to Braille and vice versa.

# Braille representation of alphabets and numbers
ALPHABET_DICT = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', 'capital' => '.....O', 'number' => '.O.OOO', ' ' => '......'
}

NUMBER_DICT = {
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
  '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..'
}

# Invert the dictionaries to get the reverse mapping
BRAILLE_ALPHABET = ALPHABET_DICT.invert
BRAILLE_NUMBER = NUMBER_DICT.invert

# Helper functions
def is_digit?(char)
  char.match?(/\d/)
end

def is_upper_case?(char)
  char.match?(/[A-Z]/)
end

def get_braille_representation(char, dict)
  dict.fetch(char, '......')
end

# Translate English text to Braille
def translate_to_braille(text)
  solution = ""
  number_mode = false

  text.each_char do |char|
    if is_upper_case?(char)
      solution += get_braille_representation('capital', ALPHABET_DICT)
      solution += get_braille_representation(char.downcase, ALPHABET_DICT)
      number_mode = false
    elsif is_digit?(char)
      unless number_mode
        solution += get_braille_representation('number', ALPHABET_DICT)
        number_mode = true
      end
      solution += get_braille_representation(char, NUMBER_DICT)
    else
      number_mode = false if number_mode && char == ' '
      solution += get_braille_representation(char, ALPHABET_DICT)
    end
  end

  solution
end

# Translate Braille to English text
def translate_to_english(braille)
  solution = ""
  check_capital = false
  number_mode = false
  curr_string = ''

  braille.each_char do |char|
    curr_string += char
    if curr_string.length == 6
      if curr_string == get_braille_representation('capital', ALPHABET_DICT)
        check_capital = true
      elsif curr_string == get_braille_representation('number', ALPHABET_DICT)
        number_mode = true
      else
        if number_mode
          char = BRAILLE_NUMBER.fetch(curr_string, '')
        else
          char = BRAILLE_ALPHABET.fetch(curr_string, '')
          char = char.upcase if check_capital
          check_capital = false
        end
        solution += char
      end
      curr_string = ''
    end
  end

  solution
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
