BRAILLE_TO_ENGLISH = {
  'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c', 'OO.O..' => 'd', 'O..O..' => 'e',
  'OOO...' => 'f', 'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l', 'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
  'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r', '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x', 'OO.OOO' => 'y',
  'O..OOO' => 'z', '.....O' => 'capital_follows', '.O.OOO' => 'number_follows', '......' => ' '
}

ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert
NUMBERS = { 'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5', 'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0' }

def language_output(input)
  input.match?(/^[O.]+$/) ? braille_to_english(input) : english_to_braille(input)
end

def braille_to_english(input)
  result = ''
  capitalize_next = false
  number_follows = false

  input.scan(/.{6}/).each do |char|
    case BRAILLE_TO_ENGLISH[char]
    when 'capital_follows'
      capitalize_next = true
    when 'number_follows'
      number_follows = true
    else
      letter = number_follows ? NUMBERS.key(BRAILLE_TO_ENGLISH[char]) : BRAILLE_TO_ENGLISH[char]
      result << (capitalize_next ? letter.upcase : letter)
      capitalize_next = number_follows = false
    end
  end

  result
end

def english_to_braille(input)
  result = ''
  number_mode = false

  input.each_char do |char|
    case char
    when /[A-Z]/
      result << ENGLISH_TO_BRAILLE['capital_follows'] << ENGLISH_TO_BRAILLE[char.downcase]
    when /[0-9]/
      result << ENGLISH_TO_BRAILLE['number_follows'] unless number_mode
      result << ENGLISH_TO_BRAILLE[NUMBERS.key(char)]
      number_mode = true
    else
      result << ENGLISH_TO_BRAILLE[char] << (char == ' ' ? '' : '')
      number_mode = false if char == ' '
    end
  end

  result
end

input = ARGV.join(' ')
puts language_output(input)

