# Shopify Engineering Intern Challenge
# Saad Mazhar - saadmazharr@gmail.com

# braille string will be only 'O' (capital o) and '.', also has to be divisible by 6
#
hash = {
  key1: 'value1',
  key2: 'value2',
  key3: 'value3'
}
# 

def input_is_braille?(string)
  o_count = string.count('O')
  dot_count = string.count('.')
  o_count + dot_count == string.length
end

# english numbers 1-0 can be represented by letters a-j
# however it must be preceded by a number follows

def return_translation_map(is_braille)
  puts "translation map function: #{is_braille}"

  english_to_braille = {
    :a => 'O.....',
    :b => 'O.O...',
    :c => 'OO....',
    :d => 'OO.O..',
    :e => 'O..O..',
    :f => 'OOO...',
    :g => 'OOOO..',
    :h => 'O.OO..',
    :i => '.O.O..',
    :j => '.OOO..',
    :k => 'O...O.',
    :l => 'O.O.O.',
    :m => 'OO..O.',
    :n => 'OO.OO.',
    :o => 'O..OO.',
    :p => 'OOO.O.',
    :q => 'OOOOO.',
    :r => 'O.OOO.',
    :s => '.OO.O.',
    :t => '.OOOO.',
    :u => 'O...OO',
    :v => 'O.O.OO',
    :w => '.OOO.O',
    :x => 'OO..OO',
    :y => 'OO.OOO',
    :z => 'O..OOO',
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.O.O..',
    '0' => '.OOO..',
    :capital => '.....O',
    :decimal => '.O...O',
    :number => '.O.OOO',
    :space => '......',
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

  if is_braille
    braille_to_english
  else
    english_to_braille
  end
end

input_string = ARGV.join(' ')
puts "input string: #{input_string}, length: #{input_string.length}"

braille = input_is_braille?(input_string)

translation_map = return_translation_map(braille)

answer = ""
number_flag = false

if braille
  # do thing
else
  for character in input_string.chars
    if character == ' '
      if number_flag
        number_flag = false
      end
      symbol = :space
    elsif character.ord.between?(65, 90)
      answer << translation_map[:capital]
      symbol = character.downcase.to_sym
    elsif character.ord.between?(96, 123)
      symbol = character.to_sym
    else
      # non alphabetic character
      if !number_flag and character.match?(/\d/)
        answer << translation_map[:number]
        number_flag = true
      end
      symbol = character
    end
    answer << translation_map[symbol]
  end
end

puts answer
