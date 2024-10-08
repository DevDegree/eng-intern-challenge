=begin
 - When a Braille `capital follows` symbol is read, 
 assume only the next symbol should be capitalized. 
  - When a Braille `number follows` symbol is read, 
  assume all following symbols are numbers until the next `space` symbol.
=end

argument = ARGV

# Translation Setup
LETTERS = [
  ['O.....', 'a'],
  ['O.O...', 'b'],
  ['OO....', 'c'],
  ['OO.O..', 'd'],
  ['O..O..', 'e'],
  ['OOO...', 'f'],
  ['OOOO..', 'g'],
  ['O.OO..', 'h'],
  ['.OO...', 'i'],
  ['.OOO..', 'j'],
  ['O...O.', 'k'],
  ['O.O.O.', 'l'],
  ['OO..O.', 'm'],
  ['OO.OO.', 'n'],
  ['O..OO.', 'o'],
  ['OOO.O.', 'p'],
  ['OOOOO.', 'q'],
  ['O.OOO.', 'r'],
  ['.OO.O.', 's'],
  ['.OOOO.', 't'],
  ['O...OO', 'u'],
  ['O.O.OO', 'v'],
  ['.OOO.O', 'w'],
  ['OO..OO', 'x'],
  ['OO.OOO', 'y'],
  ['O..OOO', 'z'],
  ['......', ' '],
  ['.....O', 'capital follows'],
  ['.O.OOO', 'number follows'],
]

NUMBERS = [
  ['O.....', '1'],
  ['O.O...', '2'],
  ['OO....', '3'],
  ['OO.O..', '4'],
  ['O..O..', '5'],
  ['OOO...', '6'],
  ['OOOO..', '7'],
  ['O.OO..', '8'],
  ['.OO...', '9'],
  ['.OOO..', '0'],
]
  
BRAILLE_ENG = LETTERS.to_h
ENG_BRAILLE = LETTERS.map { |arr| arr.reverse }.to_h

BRAILLE_ENG_NUMBERS = NUMBERS.to_h
ENG_BRAILLE_NUMBERS = NUMBERS.map { |arr| arr.reverse }.to_h


# Braille to English
def braille_to_eng(input)
  braille_chars = []
  index = 0
  length = 6

  while braille_chars.size < (input.size / 6)
    braille_chars << input[index, length]
    index += 6
  end

  capital_follows = false
  number_follows = false

  eng_chars = braille_chars.map do |char|
    if char == '.....O'
      capital_follows = true
      next
    elsif char == '.O.OOO'
      number_follows = true
      next
    end

    if char == '......'
      number_follows = false
    end

    if number_follows
      BRAILLE_ENG_NUMBERS[char]
    elsif capital_follows
      capital_follows = false
      BRAILLE_ENG[char].upcase
    else
      BRAILLE_ENG[char]
    end
  end

  puts eng_chars.join
end

# English to Braille
def eng_to_braille(input)
  capital_follows = '.....O'
  number_follows = '.O.OOO'
  number_on = true

  translated_words = []
  input.each do |word|
    translated_word = ""
    word.each_char do |char|
      if ('0'..'9').include?(char)
        translated_word << number_follows if number_on
        translated_word << ENG_BRAILLE_NUMBERS[char]
        number_on = false
      elsif char == ' '
        number_on = true
        translated_word << ENG_BRAILLE[char]

      elsif char == char.upcase
        translated_word << capital_follows
        translated_word << ENG_BRAILLE[char.downcase]
      else
        translated_word << ENG_BRAILLE[char]
      end
    end
    translated_words << translated_word
  end
puts translated_words.join('......')
end

def input_braille?(words)
  words[0].chars.all? do |char|
  char == '.' || char == 'O'
  end
end

if input_braille?(argument)
  braille_to_eng(argument[0])
else
  eng_to_braille(argument)
end
