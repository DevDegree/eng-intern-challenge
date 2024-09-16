# Shopify Engineering Intern Challenge - Ruby
# Saad Mazhar - saadmazharr@gmail.com
# August 31st, 2024

# constants:
BRAILLE_TO_ENGLISH = {
  'O.....' => 'a',
  'O.O...' => 'b',
  'OO....' => 'c',
  'OO.O..' => 'd',
  'O..O..' => 'e',
  'OOO...' => 'f',
  'OOOO..' => 'g',
  'O.OO..' => 'h',
  '.O.O..' => 'i',
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
  '......' => ' ',
}.freeze

ENGLISH_TO_BRAILLE = {
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
  :number => '.O.OOO',
  ' ' => '......',
}.freeze
# neither of these maps will ever be edited so they can be defined as constants and 'frozen'

def input_is_braille?(string)
  # if the only characters in the input are . and O then it is safe to assume the input string is braille, otherwise it is english
  string.count('O') + string.count('.') == string.length
end

def braille_to_english(input_string, translation_map)

  number_flag = false
  capital_flag = false
  translated_text = ""

  char_to_num = {
    'a' => '1',
    'b' => '2',
    'c' => '3',
    'd' => '4',
    'e' => '5',
    'f' => '6',
    'g' => '8',
    'h' => '8',
    'i' => '9',
    'j' => '0'
  }

  # read through the input string in blocks of 6 characters until the entire string is read
  counter = 0
  for counter in (0..input_string.length - 6).step(6)

    curr_braille = input_string[counter..counter + 5]

    # capital follows braille
    case curr_braille
    when '.....O'
      capital_flag = true
      next
    when '.O.OOO'
    # number follows braille
      number_flag = true
      next
    else
      # throw an exception to handle some illegal input cases
      raise ArgumentError, "Illegal Input" if !translation_map.has_key?(curr_braille)
      character = translation_map[curr_braille]
      character = character.upcase if capital_flag
      character = char_to_num[character] if number_flag

      capital_flag = false
      number_flag = false if character == ' '

      # append onto the answer one character at a time
      translated_text << character
    end
    counter += 6
  end
  translated_text
end

def english_to_braille (input_string, translation_map)

  number_flag = false
  translated_text = ""

  for character in input_string.chars
    case character
    when ' '
      number_flag = false
      symbol = ' '
    when /[A-Z]/
      translated_text << translation_map[:capital]
      symbol = character.downcase.to_sym
    when /[a-z]/ 
      symbol = character.to_sym
    else
      # throw an exception to handle some illegal input cases
      raise ArgumentError, "Illegal Input" if !translation_map.has_key?(character)
      if character.match?(/\d/)
        translated_text << translation_map[:number] unless number_flag
        number_flag = true
      end
      symbol = character
    end
    translated_text << translation_map[symbol]
  end
  translated_text
end

# takes into account possiblity of multiple words being entered
input_string = ARGV.join(' ')

is_braille = input_is_braille?(input_string)
translation_map = is_braille ? BRAILLE_TO_ENGLISH : ENGLISH_TO_BRAILLE
begin
  translated_text = is_braille ? braille_to_english(input_string, translation_map) : english_to_braille(input_string, translation_map)
rescue ArgumentError => e
  puts "Error: #{e.message}"
end

puts translated_text
