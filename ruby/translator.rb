# Callum Brezden
# 29/24/2024
# Shopify Winter 2025 Internship Application

# Notes
# Black dot is represented by '0' and empty dot is represented by '.'

BRAILLE_TO_ENGLISH = {
  'O.....' => 'a', 'O.O...' => 'b',
  'OO....' => 'c', 'OO.O..' => 'd',
  'O..O..' => 'e', 'OOO...' => 'f',
  'OOOO..' => 'g', 'O.OO..' => 'h',
  '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l',
  'OO..O.' => 'm', 'OO.OO.' => 'n',
  'O..OO.' => 'o', 'OOO.O.' => 'p',
  'OOOOO.' => 'q', 'O.OOO.' => 'r',
  '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v',
  '.OOO.O' => 'w', 'OO..OO' => 'x',
  'OO.OOO' => 'y', 'O..OOO' => 'z',

  '.....O' => 'capital_follows',
  '.O.OOO' => 'number_follows',
  '......' => ' '
}

ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert

NUMBERS = {
  'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
  'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
}

def language_output(input)
  braille_detection(input) ? braille_to_english(input) : english_to_braille(input)
end

def braille_detection(input)
  input.match?(/^[O.]+$/)
end

def english_to_braille(input)
  result = ""
  number_mode = false

  input.each_char do |char|
    if char.match?(/[A-Z]/)
      result << ENGLISH_TO_BRAILLE['capital_follows']
      char = char.downcase
    elsif char.match?(/[0-9]/)
      unless number_mode
        result << ENGLISH_TO_BRAILLE['number_follows']
        number_mode = true
      end
      char = NUMBERS.key(char)
    elsif char == ' '
      number_mode = false
    end

    result << ENGLISH_TO_BRAILLE[char]
  end

  result
end

input = ARGV.join(' ')
output = language_output(input)
puts output
puts output == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
