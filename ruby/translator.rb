ENGLISH_TO_BRAILLE = {
  # Letters
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO',

  # Numbers
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
  '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..',

  # Special Symbols
  'capital' => '.....O',   # Capital follows
  'decimal' => '.O..OO',   # Decimal follows
  'number' => '.O.OOO',    # Number follows
  ' ' => '......',         # Space

  # Punctuation
  '.' => '..OO.O',
  ',' => '..O...',
  '?' => '..O.OO',
  '!' => '..OOO.',
  ':' => '..OO..',
  ';' => '..O.O.',
  '-' => '....OO',
  '/' => '.O..O.',
  '<' => '.OO..O',
  '>' => 'O..OO.',
  '(' => 'O.O..O',
  ')' => '.O.OO.',
}

BRAILLE_TO_ENGLISH_LETTERS = {
  'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c', 'OO.O..' => 'd', 'O..O..' => 'e',
  'OOO...' => 'f', 'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l', 'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
  'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r', '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x', 'OO.OOO' => 'y',
  'O..OOO' => 'z',
}

BRAILLE_TO_ENGLISH_NUMBERS = {
  'O.....' => '1', 'O.O...' => '2', 'OO....' => '3', 'OO.O..' => '4', 'O..O..' => '5',
  'OOO...' => '6', 'OOOO..' => '7', 'O.OO..' => '8', '.OO...' => '9', '.OOO..' => '0',
}

BRAILLE_TO_ENGLISH_SPECIAL = {
  '.....O' => 'capital',   # Capital follows
  '.O..OO' => 'decimal',   # Decimal follows
  '.O.OOO' => 'number',    # Number follows
  '......' => ' ',         # Space

  '..OO.O' => '.',
  '..O...' => ',',
  '..O.OO' => '?',
  '..OOO.' => '!',
  '..OO..' => ':',
  '..O.O.' => ';',
  '....OO' => '-',
  '.O..O.' => '/',
  '.OO..O' => '<',
  'O..OO.' => '>',
  'O.O..O' => '(',
  '.O.OO.' => ')'
}

# Checks if input is braille or english
def is_braille?(input)
  input.chars.all? { |char| ['O', '.'].include?(char) }
end

# Method to translate English string to Braille
def translate_to_braille(english_string)
  result = []
  is_number = false

  english_string.each_char do |char|
    if char =~ /\d/ && !is_number
      result << ENGLISH_TO_BRAILLE['number']
      is_number = true
    elsif !char =~ /\d/ && is_number
      is_number = false
    end

    if char =~ /[A-Z]/
      result << ENGLISH_TO_BRAILLE['capital']
      result << ENGLISH_TO_BRAILLE[char.downcase]
    elsif char =~ /\d/
      result << ENGLISH_TO_BRAILLE[char]
    else
      result << ENGLISH_TO_BRAILLE[char]
    end
  end

  result.join
end


# Method to translate Braille string to English
def translate_to_english(braille_string)
  result = []
  is_capital = false
  is_number = false

  # Split the Braille string into segments of 6 characters
  braille_characters = braille_string.scan(/.{1,6}/)

  braille_characters.each do |braille_char|
    # Dealing with capitals and numbers
    if braille_char == ENGLISH_TO_BRAILLE['capital']
      is_capital = true
      next
    elsif braille_char == ENGLISH_TO_BRAILLE['number']
      is_number = true
      next
    elsif braille_char == '......'
      result << ' '
      is_number = false  # Exit number mode when space is encountered
      next
    end

    # Lookup the Braille character in the appropriate hash
    letter = BRAILLE_TO_ENGLISH_LETTERS[braille_char] ||
             BRAILLE_TO_ENGLISH_NUMBERS[braille_char] ||
             BRAILLE_TO_ENGLISH_SPECIAL[braille_char]


    # Handle numbers
    if is_number
      if BRAILLE_TO_ENGLISH_NUMBERS[braille_char]
        result << BRAILLE_TO_ENGLISH_NUMBERS[braille_char]
      else
        result << letter # Handle any characters that may appear in number mode
      end
    else
      # Handle capital letters
      if is_capital
        result << letter.upcase  # Capitalize the next letter
        is_capital = false  # Reset capital mode after one letter
      else
        result << letter  # Add the regular letter
      end
    end
  end

  result.join
end

def braille_translator(input)
  if is_braille?(input)
    # If the input is Braille, translate it to English
    translate_to_english(input)
  else
    # If the input is English, translate it to Braille
    translate_to_braille(input)
  end
end

# TEST
puts braille_translator('Abc 123 xYz')
# puts braille_translator('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
# puts braille_translator('42')
# puts braille_translator('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
