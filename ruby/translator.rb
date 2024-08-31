# Shopify Engineering Intern Challenge
# Saad Mazhar - saadmazharr@gmail.com

def input_is_braille?(string)
  # if the only characters in the input are . and O then it is safe to assume the input string is braille, otherwise it is english
  o_count = string.count('O')
  dot_count = string.count('.')
  o_count + dot_count == string.length
end

def return_translation_map(is_braille)
  # returns a hashmap that is referenced for translation based on which way the translation is going

  braille_to_english = {
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
  }

  # use symbols where possible instead of strings for keys
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
    :number => '.O.OOO',
    ' ' => '......',
  }

  if is_braille
    braille_to_english
  else
    english_to_braille
  end
end

# takes into account possiblity of multiple words being entered
input_string = ARGV.join(' ')

braille = input_is_braille?(input_string)

translation_map = return_translation_map(braille)

answer = ""
# use of boolean flags to track if next character should be capitalized or treated as a number
number_flag = false
capital_flag = false

# used to translate braille -> alphabet -> number when number flag is raised
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

if braille
  # read through the input string in blocks of 6 characters until the entire string is read
  counter = 0
  while counter < input_string.length

    curr_braille = input_string[counter..counter + 5]

    # capital follows braille
    if curr_braille == '.....O'
      capital_flag = true

    # number follows braille
    elsif curr_braille == '.O.OOO'
      number_flag = true

    else

      if capital_flag
        character = translation_map[curr_braille].capitalize
        capital_flag = false

      elsif number_flag == true
        # braille -> alphabetic character -> number
        letter = translation_map[curr_braille]
        character = char_to_num[letter]

      else
        character = translation_map[curr_braille]

      end
      # only a space can reset the number flag
      if character == ' '
        number_flag = false

      end
      # append onto the answer one character at a time
      answer << character

    end
    counter += 6
  end

else
  # english to braille translation
  for character in input_string.chars
    if character == ' '
      if number_flag
        number_flag = false
      end
      symbol = ' '
    
    # capital letters based on regex values
    elsif character.match?(/[A-Z]/)
      answer << translation_map[:capital]
      symbol = character.downcase.to_sym
    
    # standard (lowercase) letters
    elsif character.match?(/[a-z]/)
      symbol = character.to_sym

    else
      # non alphabetic character
      if !number_flag and character.match?(/\d/)
        answer << translation_map[:number]
        number_flag = true

      end
      symbol = character

    end
    # push braille onto answer string in groups of 6 length strings (according to translation map)
    answer << translation_map[symbol]

  end
end

puts answer
