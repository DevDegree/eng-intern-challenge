ENGLISH_TO_BRAILLE_MAPPING = {
  alpha_and_punctuation: {
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
    # '.' => '..OO.O',
    # ',' => '..O...',
    # '?' => '..O.OO',
    # '!' => '..OOO.',
    # ':' => '..OO..',
    # ';' => '..O.O.',
    # '-' => '....OO',
    # '/' => '.O..O.',
    # '<' => '.OO..O',
    # '>' => 'O..OO.',
    # '(' => 'O.O..O',
    # ')' => '.O.OO.',
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

BRAILLE_TO_ENGLISH_MAPPING = ENGLISH_TO_BRAILLE_MAPPING.transform_values { |v| v.invert }

ENGLISH_SPACE = ' '
BRAILLE_SPACE = ENGLISH_TO_BRAILLE_MAPPING[:special][ENGLISH_SPACE]

def is_english?(str)
  str.length % 6 != 0 || str.chars.any? { |char| not ['O', '.'].include?(char) }
end

def is_special_symbol?(symbol)
  return BRAILLE_TO_ENGLISH_MAPPING[:special].key?(symbol)
end

def translate_to_english(str)
  translated_str = ''
  numeric_mode = false
  capital_next = false
  str.chars.each_slice(6) do |symbol_arr|
    symbol = symbol_arr.join('')

    if is_special_symbol?(symbol)
      case BRAILLE_TO_ENGLISH_MAPPING[:special][symbol]
      when 'capital_follows'
        capital_next = true
      when 'decimal_follows'
      when 'number_follows'
        numeric_mode = true
      when ENGLISH_SPACE
        numeric_mode = false
        capital_next = false
        translated_str += ENGLISH_SPACE
      end 
    elsif numeric_mode
      translated_str += BRAILLE_TO_ENGLISH_MAPPING[:numeric][symbol]
    else
      char = BRAILLE_TO_ENGLISH_MAPPING[:alpha_and_punctuation][symbol]
      translated_str += capital_next ? char.capitalize : char
      capital_next = false
    end
  end
  
  translated_str
end

def translate_to_braille(str)
  "......"
end

def main
  input_string = ARGV.join(' ')

  translated_string = is_english?(input_string) ? translate_to_braille(input_string) : translate_to_english(input_string)
  puts(translated_string)
end

main