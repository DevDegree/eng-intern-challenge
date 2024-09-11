# Map of English characters to Braille characters and vice versa
ENGLISH_TO_BRAILLE_MAP = {
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
    'z' => 'O..OOO'
  },
  nums: {
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
  },
  codes: {
    capital: '.....O', 
    number: '.O.OOO'
  },
  special: {
    ' ' => '......'
  }
}
BRAILLE_TO_ENGLISH_MAP = ENGLISH_TO_BRAILLE_MAP.transform_values(&:invert)

# Translate English to Braille
def english_to_braille(string)
  result = ''
  digit_flag = false

  string.each_char do |char|
    if char.match?(/[a-z]/)
      result += ENGLISH_TO_BRAILLE_MAP[:alpha][char]
    elsif char.match?(/[A-Z]/)
      result += ENGLISH_TO_BRAILLE_MAP[:codes][:capital] + ENGLISH_TO_BRAILLE_MAP[:alpha][char.downcase]
    elsif ENGLISH_TO_BRAILLE_MAP[:special].key?(char)
      result += ENGLISH_TO_BRAILLE_MAP[:special][char]
      digit_flag = false
    elsif char.match?(/[0-9]/)
      if digit_flag
        result += ENGLISH_TO_BRAILLE_MAP[:nums][char]
      else
        result += ENGLISH_TO_BRAILLE_MAP[:codes][:number] + ENGLISH_TO_BRAILLE_MAP[:nums][char]
        digit_flag = true
      end
    end
  end

  result
end

# Translate Braille to English
def braille_to_english(string)
  # Split string into 6-character Braille characters
  result = ''
  braille_chars = string.scan(/.{6}/)

  # Flags to keep track of capitalization, numbers, and decimals
  digit_flag = false
  capitalize_flag = false

  braille_chars.each do |braille_char|
    if braille_char == '......'
      digit_flag = false
      capitalize_flag = false
      result += BRAILLE_TO_ENGLISH_MAP[:special][braille_char]
    elsif BRAILLE_TO_ENGLISH_MAP[:codes].key?(braille_char)
      case BRAILLE_TO_ENGLISH_MAP[:codes][braille_char]
      when :capital
        capitalize_flag = true
      when :number
        digit_flag = true
      end
    elsif digit_flag
      result += BRAILLE_TO_ENGLISH_MAP[:nums][braille_char]
    elsif BRAILLE_TO_ENGLISH_MAP[:alpha].key?(braille_char)
      char = BRAILLE_TO_ENGLISH_MAP[:alpha][braille_char]
      result += capitalize_flag ? char.upcase : char
      capitalize_flag = false
    end
  end

  result
end

# Check if input is English (true) or Braille (false)
def check_if_input_english(user_input)
  english_pattern = /[a-np-zA-NP-Z]/
  numeric_pattern = /[0-9]/
  punctuation_pattern = /[,?!:;\-\/<>\(\)]/

  is_english = user_input =~ english_pattern ||
               user_input =~ numeric_pattern ||
               user_input =~ punctuation_pattern ||
               user_input.length % 6 != 0

  is_english
end

# Main function
def main
  input = ARGV.join(" ")
  check_if_input_english(input) ? puts(english_to_braille(input)) : puts(braille_to_english(input))
end

main
