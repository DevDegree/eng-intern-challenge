# Braille mappings for English alphabet and digits
BRAILLE_TO_ENGLISH = {
  'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c', 'OO.O..' => 'd', 'O..O..' => 'e',
  'OOO...' => 'f', 'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l', 'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
  'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r', '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x', 'OO.OOO' => 'y',
  'O..OOO' => 'z', '......' => ' ' # only map letters and space here
}

# Numbers map using the same symbols as 'a' to 'j' but require NUMBER_SYMBOL context
BRAILLE_NUMBERS = {
  'O.....' => '1', 'O.O...' => '2', 'OO....' => '3', 'OO.O..' => '4', 'O..O..' => '5',
  'OOO...' => '6', 'OOOO..' => '7', 'O.OO..' => '8', '.OO...' => '9', '.OOO..' => '0'
}

ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert

# Special symbols
CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'

def is_braille?(input)
  input.match?(/\A[O.]+\z/)
end

def translate_to_braille(text)
  result = []
  text.each_char do |char|
    if char =~ /[A-Z]/
      result << CAPITAL_SYMBOL
      result << ENGLISH_TO_BRAILLE[char.downcase]
    elsif char =~ /\d/
      result << NUMBER_SYMBOL
      result << ENGLISH_TO_BRAILLE[(char.to_i + 96).chr] # Convert number to corresponding letter a-j for Braille
    else
      result << ENGLISH_TO_BRAILLE[char]
    end
  end
  result.join  # Join without spaces to match the format
end

def translate_to_english(braille)
  result = []
  is_capital = false
  is_number = false

  braille.scan(/.{6}/).each do |symbol|
    if symbol == CAPITAL_SYMBOL
      is_capital = true
    elsif symbol == NUMBER_SYMBOL
      is_number = true
    elsif is_number
      result << BRAILLE_NUMBERS[symbol]
    elsif is_capital
      result << BRAILLE_TO_ENGLISH[symbol].upcase
      is_capital = false
    else
      result << BRAILLE_TO_ENGLISH[symbol]
    end
  end
  result.join
end

if __FILE__ == $0
  
  input_str = ARGV.join(' ')

  if is_braille?(input_str)
    
    puts translate_to_english(input_str)
  else
   
    puts translate_to_braille(input_str)
  end
end
