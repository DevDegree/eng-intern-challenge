# Define Braille mappings for letters and numbers
BRAILLE_LETTERS = {
  'O.....' => 'a',
  'O.O...' => 'b',
  'OO....' => 'c',
  'OO.O..' => 'd',
  'O..O..' => 'e',
  'OOO...' => 'f',
  'OOOO..' => 'g',
  'O.OO..' => 'h',
  '.OO...' => 'i',
  '.OOO..' => 'j',
  'O...O.' => 'k',
  'O.O.O.' => 'l',
  'OO..O.' => 'm',
  'OO.OO.' => 'n',
  'O..OO.' => 'o',
  'OOO.O.' => 'p',
  'OOOOO.' => 'q',
  'O.OOO.' => 'r',
  '.OO.O.' => 's',
  '.OOOO.' => 't',
  'O...OO' => 'u',
  'O.O.OO' => 'v',
  '.OOO.O' => 'w',
  'OO..OO' => 'x',
  'OO.OOO' => 'y',
  'O..OOO' => 'z',
}

CAPITAL_SIGN = '.....O'
NUMBER_SIGN = '.O.OOO'
WHITESPACE = '......'

BRAILLE_NUMBERS = {
  'O.....' => '1',
  'O.O...' => '2',
  'OO....' => '3',
  'OO.O..' => '4',
  'O..O..' => '5',
  'OOO...' => '6',
  'OOOO..' => '7',
  'O.OO..' => '8',
  '.OO...' => '9',
  '.OOO..' => '0',
}

LETTERS_TO_BRAILLE = BRAILLE_LETTERS.invert
NUMBERS_TO_BRAILLE = BRAILLE_NUMBERS.invert

LETTERS_TO_BRAILLE[' '] = WHITESPACE

def braille_converter(input_string)
  # Determine whether the input contains Braille characters or standard text
  if input_string.match(/[O.]/)
    output = []
    capital_mode = false
    number_mode = false

    # Process each 6-character Braille code block
    input_string.scan(/.{6}/).each do |braille_char|
      if braille_char == CAPITAL_SIGN
        capital_mode = true
      elsif braille_char == NUMBER_SIGN
        number_mode = true
      elsif braille_char == WHITESPACE
        output << ' '
        number_mode = false
      else
        # Translate Braille to English letters or numbers
        char = number_mode ? BRAILLE_NUMBERS[braille_char] : BRAILLE_LETTERS[braille_char]

        # Handle capitalization
        if capital_mode
          char = char.upcase
          capital_mode = false
        end
        output << char
      end
    end

    output.join
  else
    # If the input is in English, convert it to Braille
    output = []
    number_mode = false

    input_string.chars.each do |char|
      if char.match(/\d/)
        output << NUMBER_SIGN unless number_mode
        number_mode = true
        output << NUMBERS_TO_BRAILLE[char]
      elsif char == ' '
        output << WHITESPACE
        number_mode = false
      elsif char == char.upcase
        output << CAPITAL_SIGN
        output << LETTERS_TO_BRAILLE[char.downcase]
        number_mode = false
      else
        output << LETTERS_TO_BRAILLE[char]
        number_mode = false
      end
    end

    output.join
  end
end

puts braille_converter(ARGV.join(' '))