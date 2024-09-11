# Mappings for English to Braille translation
ENGLISH_TO_BRAILLE = {
  letters: {
    'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
    'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
    'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
    'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
    'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO', 'z' => 'O..OOO',
  },
  numbers: {
    '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
    '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..',
  },
  special: {
    'capital_indicator' => '.....O', 'number_indicator' => '.O.OOO', 'space' => '......'
  }
}

# Reverse mapping for Braille to English
BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.transform_values(&:invert)

ENGLISH_SPACE = ' '
BRAILLE_SPACE = ENGLISH_TO_BRAILLE[:special]['space']

# Translate Braille string to English
def braille_to_english(str)
  result = ''
  numeric_mode = false
  capitalize_follows = false

  # Process each Braille symbol sequentially
  str.chars.each_slice(6) do |symbol_arr|
    symbol = symbol_arr.join('')

    if BRAILLE_TO_ENGLISH[:special].key?(symbol) # Special character
      case BRAILLE_TO_ENGLISH[:special][symbol]
      when 'capital_indicator'
        capitalize_follows = true
      when 'number_indicator'
        numeric_mode = true
      when 'space'
        result += ENGLISH_SPACE
        numeric_mode = false
        capitalize_follows = false
      end
    elsif numeric_mode && BRAILLE_TO_ENGLISH[:numbers].key?(symbol) # Number
      result += BRAILLE_TO_ENGLISH[:numbers][symbol]
    elsif BRAILLE_TO_ENGLISH[:letters].key?(symbol) # Letter
      char = BRAILLE_TO_ENGLISH[:letters][symbol]
      result += capitalize_follows ? char.upcase : char
      capitalize_follows = false
    end
  end

  result
end

# Translate English string to Braille
def english_to_braille(str)
  result = ''
  numeric_mode = false

  str.each_char do |char|
    if char == ENGLISH_SPACE
      result += BRAILLE_SPACE
      numeric_mode = false
    elsif char.match?(/[0-9]/) # Digit
      unless numeric_mode
        result += ENGLISH_TO_BRAILLE[:special]['number_indicator']
        numeric_mode = true
      end
      result += ENGLISH_TO_BRAILLE[:numbers][char]
    elsif char.match?(/[A-Z]/) # Uppercase letter
      result += ENGLISH_TO_BRAILLE[:special]['capital_indicator']
      result += ENGLISH_TO_BRAILLE[:letters][char.downcase]
    elsif char.match?(/[a-z]/) # Lowercase letter
      result += ENGLISH_TO_BRAILLE[:letters][char]
    end
  end

  result
end

# Check if string is Braille or English
def is_braille?(str)
  str.length % 6 == 0 && str.chars.all? { |char| ['O', '.'].include?(char) }
end

# Detect input type and perform translation
def main
  input_string = ARGV.join(' ')
  translated_string = is_braille?(input_string) ? braille_to_english(input_string) : english_to_braille(input_string)
  puts(translated_string)
end

main
