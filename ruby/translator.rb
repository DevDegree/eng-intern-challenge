BRAILLE_TO_ENGLISH_LETTERS = {
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

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

BRAILLE_TO_ENGLISH_NUMBERS = {
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

ENGLISH_TO_BRAILLE_LETTERS = BRAILLE_TO_ENGLISH_LETTERS.invert
ENGLISH_TO_BRAILLE_NUMBERS = BRAILLE_TO_ENGLISH_NUMBERS.invert


ENGLISH_TO_BRAILLE_LETTERS.merge!({
  ' ' => SPACE,
})
def translate(input)
    if input.match(/[O.]/)
      result = []
      is_capital = false
      is_number = false
  
      input.scan(/.{6}/).each do |braille|
        if braille == CAPITAL_FOLLOWS
          is_capital = true
        elsif braille == NUMBER_FOLLOWS
          is_number = true
        elsif braille == SPACE
          result << ' '
          is_number = false
        else
          character = is_number ? BRAILLE_TO_ENGLISH_NUMBERS[braille] : BRAILLE_TO_ENGLISH_LETTERS[braille]
          
          if is_capital
            character = character.upcase
            is_capital = false
          end
          result << character
        end
      end
  
      result.join
    else
      result = []
      is_number = false
  
      input.chars.each do |char|
        if char.match(/\d/)
          result << NUMBER_FOLLOWS unless is_number
          is_number = true
          result << ENGLISH_TO_BRAILLE_NUMBERS[char]
        elsif char == ' '
          result << SPACE
          is_number = false
        elsif char == char.upcase
          result << CAPITAL_FOLLOWS
          result << ENGLISH_TO_BRAILLE_LETTERS[char.downcase]
          is_number = false
        else
          result << ENGLISH_TO_BRAILLE_LETTERS[char]
          is_number = false
        end
      end
  
      result.join
    end
  end
  
  puts translate(ARGV.join(' '))
  
  