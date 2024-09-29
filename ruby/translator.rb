ALPHABET_TO_BRAILLE = {
  'a' => "O.....",
  'b' => "O.O...",
  'c' => "OO....",
  'd' => "OO.O..",
  'e' => "O..O..",
  'f' => "OOO...",
  'g' => "OOOO..",
  'h' => "O.OO..",
  'i' => ".OO...",
  'j' => ".OOO..",
  'k' => "O...O.",
  'l' => "O.O.O.",
  'm' => "OO..O.",
  'n' => "OO.OO.",
  'o' => "O..OO.",
  'p' => "OOO.O.",
  'q' => "OOOOO.",
  'r' => "O.OOO.",
  's' => ".OO.O.",
  't' => ".OOOO.",
  'u' => "O...OO",
  'v' => "O.O.OO",
  'w' => ".OOO.O",
  'x' => "OO..OO",
  'y' => "OO.OOO",
  'z' => "O..OOO",
  ' ' => "......"
}.freeze

NUMBER_TO_BRAILLE = {
  '1' => "O.....",
  '2' => "O.O...",
  '3' => "OO....",
  '4' => "OO.O..",
  '5' => "O..O..",
  '6' => "OOO...",
  '7' => "OOOO..",
  '8' => "O.OO..",
  '9' => ".OO...",
  'O' => ".OOO.."
}.freeze

BRAILLE_TO_ALPHABET = ALPHABET_TO_BRAILLE.invert.freeze
BRAILLE_TO_NUMBER = NUMBER_TO_BRAILLE.invert.freeze

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

input_string = ARGV.join(' ')
is_braille = input_string.count('^.O').zero? && (input_string.length % 6).zero?

def convert_to_braille(input_string)
  number_mode = false
  output = ''

  input_string.each_char do |char|
    if char =~ /[0-9]/ # current char is number
      unless number_mode # add number follows symbol if first number
        output += NUMBER_FOLLOWS
        number_mode = true
      end
      output += NUMBER_TO_BRAILLE[char]
    else
      # add capital follows symbol if char is in uppercase
      output += CAPITAL_FOLLOWS if char =~ /[A-Z]/
      output += ALPHABET_TO_BRAILLE[char.downcase]
      number_mode = false if number_mode
    end
  end

  output
end

def convert_to_english(input_string)
  capslock_on = false
  number_mode = false

  # split into chunks of braille characters
  chunks = input_string.scan(/.{1,6}/)

  output = chunks.map do |chunk|
    if chunk == CAPITAL_FOLLOWS
      capslock_on = true
      next # skip to next iteration
    elsif chunk == NUMBER_FOLLOWS
      number_mode = true
      next # skip to next iteration
    elsif capslock_on
      capslock_on = false
      BRAILLE_TO_ALPHABET[chunk].upcase
    elsif number_mode
      if chunk == ALPHABET_TO_BRAILLE[' '] # exit number mode if chunk is space char
        number_mode = false
        ' '
      else
        BRAILLE_TO_NUMBER[chunk]
      end
    else
      BRAILLE_TO_ALPHABET[chunk]
    end
  end

  output.join
end

output = is_braille ? convert_to_english(input_string) : convert_to_braille(input_string)

puts output