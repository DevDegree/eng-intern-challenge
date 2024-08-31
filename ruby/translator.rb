# Mappings for English to Braille translation
ENGLISH_TO_BRAILLE_MAPPING = {
  alpha: {
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
  },
  numeric: {
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
  },
  special: {
    'capital_follows' => '.....O',
    'decimal_follows' => '.O...O',
    'number_follows' => '.O.OOO',
    ' ' => '......',
  }
}

# Mappings for Braille to English translation
BRAILLE_TO_ENGLISH_MAPPING = ENGLISH_TO_BRAILLE_MAPPING.transform_values { |v| v.invert }

ENGLISH_SPACE = ' '
BRAILLE_SPACE = ENGLISH_TO_BRAILLE_MAPPING[:special][ENGLISH_SPACE]

# Check if string contains any non-Braille (not O or .) characters or not a length multiple of 6
def is_english?(str)
  str.length % 6 != 0 || str.chars.any? { |char| not ['O', '.'].include?(char) }
end

# Check if Braille symbol exists in alpha translations
def is_alpha_symbol?(symbol)
  return BRAILLE_TO_ENGLISH_MAPPING[:alpha].key?(symbol)
end

# Check if Braille symbol exists in numeric translations
def is_numeric_symbol?(symbol)
  return BRAILLE_TO_ENGLISH_MAPPING[:numeric].key?(symbol)
end

# Check if Braille symbol exists in special translations
def is_special_symbol?(symbol)
  return BRAILLE_TO_ENGLISH_MAPPING[:special].key?(symbol)
end

# Check if English character is numeric
def is_numeric_char?(char)
  char.match?(/[0-9]/)
end

# Check if English character is uppercase and alpha
def is_upper_case_alpha_char?(char)
  char.match?(/[A-Z]/)
end

# Check if English character is lowercase and alpha
def is_lower_case_alpha_char?(char)
  char.match?(/[a-z]/)
end

# Translate Braille string to English
def translate_to_english(str)
  translated_str = ''
  numeric_mode = false
  capital_next = false

  # Process in chunks of 6 characters (a single Braille symbol)
  str.chars.each_slice(6) do |symbol_arr|
    symbol = symbol_arr.join('')

    if is_special_symbol?(symbol)
      case BRAILLE_TO_ENGLISH_MAPPING[:special][symbol]
      when 'capital_follows'
        # The next chunk we process will need to be capitalized
        capital_next = true
      when 'decimal_follows'
      when 'number_follows'
        numeric_mode = true
      when ENGLISH_SPACE
        # Reset modes and add a space to the translated string
        numeric_mode = false
        capital_next = false
        translated_str += ENGLISH_SPACE
      end 
    elsif numeric_mode && is_numeric_symbol?(symbol)
      # Translate number
      translated_str += BRAILLE_TO_ENGLISH_MAPPING[:numeric][symbol]
    elsif is_alpha_symbol?(symbol)
      # Translate letter and convert to capital if previous symbol indicated so
      char = BRAILLE_TO_ENGLISH_MAPPING[:alpha][symbol]
      translated_str += capital_next ? char.capitalize : char
      capital_next = false
    end
  end
  
  translated_str
end

# Translate English string to Braille
def translate_to_braille(str)
  translated_str = ''
  numeric_mode = false

  # Process each character in the English string
  str.each_char do |char|
    if char == ENGLISH_SPACE
      # Reset modes and add a space to the translated string
      numeric_mode = false
      translated_str += BRAILLE_SPACE
    elsif is_numeric_char?(char)
      # Prefix with numerical notifying symbol and translate the number
      if not numeric_mode
        # Enable numeric mode so number_follows symbol is not added again
        numeric_mode = true
        translated_str += ENGLISH_TO_BRAILLE_MAPPING[:special]['number_follows']
      end
      translated_str += ENGLISH_TO_BRAILLE_MAPPING[:numeric][char]
    elsif is_upper_case_alpha_char?(char)
       # Prefix with capitlized notifying symbol and translate the lowercased letter
      translated_str += ENGLISH_TO_BRAILLE_MAPPING[:special]['capital_follows']
      translated_str += ENGLISH_TO_BRAILLE_MAPPING[:alpha][char.downcase]
    elsif is_lower_case_alpha_char?(char)
      # Translate lowercase letters
      translated_str += ENGLISH_TO_BRAILLE_MAPPING[:alpha][char]
    end
  end

  translated_str
end

def main
  input_string = ARGV.join(' ')

  # Based on if string is Braille or English, translate and print out
  translated_string = is_english?(input_string) ? translate_to_braille(input_string) : translate_to_english(input_string)
  puts(translated_string)
end

main