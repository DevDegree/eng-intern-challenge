ENGLISH_TO_BRAILLE_MAP = {
  alpha: {
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
    'y' => 'OO.OOO', 'z' => 'O..OOO'
  },
  nums: {
    '1' => 'O.....', '2' => 'O.O...', 
    '3' => 'OO....', '4' => 'OO.O..', 
    '5' => 'O..O..', '6' => 'OOO...', 
    '7' => 'OOOO..', '8' => 'O.OO..', 
    '9' => '.OO...', '0' => '.OOO..'
  },
  codes: {
    'capital' => '.....O',  
    'number' => '.O.OOO'   
  },
  special: {
    ' ' => '......',  
    '.' => '..OO.O',   
    ',' => '..O...',  
    '?' => '..O.OO', 
    '!' => '..OOO.',    
    ':' => '..OO..', 
    ';' => '..O.O.',
    '-' => '....OO',    
    '/' => '.O..O.',  
    '(' => 'O.O..O',    
    ')' => '.O.OO.'   
  }
}

# Correctly inverting the map for reverse lookup
BRAILLE_TO_ENGLISH_MAP = {
  alpha: ENGLISH_TO_BRAILLE_MAP[:alpha].invert,
  nums: ENGLISH_TO_BRAILLE_MAP[:nums].invert,
  codes: ENGLISH_TO_BRAILLE_MAP[:codes].invert,
  special: ENGLISH_TO_BRAILLE_MAP[:special].invert
}

# Translate English to Braille
def english_to_braille(string)
  result = ''
  is_number_mode = false

  string.each_char do |char|
    if char.match?(/[a-z]/)
      result += ENGLISH_TO_BRAILLE_MAP[:alpha][char]
      is_number_mode = false
    elsif char.match?(/[A-Z]/)
      result += ENGLISH_TO_BRAILLE_MAP[:codes]['capital'] + ENGLISH_TO_BRAILLE_MAP[:alpha][char.downcase]
      is_number_mode = false
    elsif ENGLISH_TO_BRAILLE_MAP[:special].key?(char)
      result += ENGLISH_TO_BRAILLE_MAP[:special][char]
      is_number_mode = false
    elsif char.match?(/[0-9]/)
      unless is_number_mode
        result += ENGLISH_TO_BRAILLE_MAP[:codes]['number']
        is_number_mode = true
      end
      result += ENGLISH_TO_BRAILLE_MAP[:nums][char]
    end
  end

  result
end

# Translate Braille to English
def braille_to_english(braille_string)
  english_result = ''
  braille_characters = braille_string.scan(/.{6}/)
  is_number_mode = false
  is_capital_mode = false

  braille_characters.each do |braille_char|
    if braille_char == '......'
      is_number_mode = false
      is_capital_mode = false
      english_result += ' '
    elsif BRAILLE_TO_ENGLISH_MAP[:codes].key?(braille_char)
      if BRAILLE_TO_ENGLISH_MAP[:codes][braille_char] == 'capital'
        is_capital_mode = true
      elsif BRAILLE_TO_ENGLISH_MAP[:codes][braille_char] == 'number'
        is_number_mode = true
      end
    elsif is_number_mode
      english_result += BRAILLE_TO_ENGLISH_MAP[:nums][braille_char]
    elsif BRAILLE_TO_ENGLISH_MAP[:alpha].key?(braille_char)
      english_char = BRAILLE_TO_ENGLISH_MAP[:alpha][braille_char]
      english_result += is_capital_mode ? english_char.upcase : english_char
      is_capital_mode = false
    elsif BRAILLE_TO_ENGLISH_MAP[:special].key?(braille_char)
      english_result += BRAILLE_TO_ENGLISH_MAP[:special][braille_char]
    end
  end

  english_result
end

# Check if input is in Braille or English 
def check_if_input_english(user_input)
  # Remove spaces for Braille detection 
  sanitized_input = user_input.gsub(' ', '')

  # Check if input is valid Braille
  is_braille = sanitized_input.chars.all? { |char| ['O', '.'].include?(char) } && (sanitized_input.length % 6).zero?
  !is_braille
end

# Main function
def main
  input = ARGV.join(" ")

  if check_if_input_english(input)
    puts english_to_braille(input)
  else
    puts braille_to_english(input)
  end
end

main
