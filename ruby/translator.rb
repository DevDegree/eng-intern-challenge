# Braille Translator: Converts English text to Braille and vice versa

# Braille representation of alphabets
BRAILLE_ALPHABET_MAP = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 
  'e' => 'O..O..', 'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 
  'i' => '.OO...', 'j' => '.OOO..', 'k' => 'O...O.', 'l' => 'O.O.O.', 
  'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.', 'p' => 'OOO.O.', 
  'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.', 
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 
  'y' => 'OO.OOO', 'z' => 'O..OOO', 'capital' => '.....O', 
  'number' => '.O.OOO', ' ' => '......'
}

# Braille representation of numbers
BRAILLE_NUMBER_MAP = {
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', 
  '5' => 'O..O..', '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', 
  '9' => '.OO...', '0' => '.OOO..'
}

# Reverse mappings for decoding Braille to English
ALPHABET_REVERSE_MAP = BRAILLE_ALPHABET_MAP.invert
NUMBER_REVERSE_MAP = BRAILLE_NUMBER_MAP.invert

# Check if a character is a digit
def digit?(char)
  char =~ /\d/
end

# Check if a character is uppercase
def uppercase?(char)
  char =~ /[A-Z]/
end

# Get Braille representation of an alphabet character
def braille_for_alphabet(char)
  BRAILLE_ALPHABET_MAP[char] || '......'
end

# Get Braille representation of a number
def braille_for_number(char)
  BRAILLE_NUMBER_MAP[char] || '......'
end

# Translate English text to Braille
def to_braille(text)
  braille_output = ""
  number_mode = false

  text.each_char do |char|
    if uppercase?(char)
      braille_output << braille_for_alphabet('capital')
      braille_output << braille_for_alphabet(char.downcase)
      number_mode = false
    elsif digit?(char)
      braille_output << braille_for_alphabet('number') unless number_mode
      braille_output << braille_for_number(char)
      number_mode = true
    else
      number_mode = false if char == ' '
      braille_output << braille_for_alphabet(char)
    end
  end

  braille_output
end

# Translate Braille to English text
def to_english(braille_input)
  english_output = ""
  capital_flag = false
  number_mode = false
  braille_char = ""

  braille_input.each_char do |char|
    braille_char << char

    if braille_char.length == 6
      case braille_char
      when braille_for_alphabet('capital')
        capital_flag = true
      when braille_for_alphabet('number')
        number_mode = true
      else
        if number_mode
          english_char = NUMBER_REVERSE_MAP[braille_char] || ''
        else
          english_char = ALPHABET_REVERSE_MAP[braille_char] || ''
          if capital_flag
            english_char.upcase!
            capital_flag = false
          end
        end
        english_output << english_char
      end
      braille_char.clear
    end
  end

  english_output
end

# Main entry point for the Braille Translator
def main
  if ARGV.empty?
    puts "Usage: ruby translator.rb < braille/plain formatted text >"
    return
  end

  input_text = ARGV.join(' ')

  # Determine if input is Braille or English text and translate accordingly
  if input_text.gsub(' ', '').chars.all? { |char| 'O.'.include?(char) }
    puts to_english(input_text)
  else
    puts to_braille(input_text)
  end
end

main if __FILE__ == $PROGRAM_NAME
