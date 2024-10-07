argument = ARGV

TRANSLATION = [
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
]
  
BRAILLE_ENG = TRANSLATION.to_h
ENG_BRAILLE = TRANSLATION.map { |arr| arr.reverse }.to_h

def braille_to_eng(input)
  braille_chars = []
  index = 0
  length = 6

  while braille_chars.size < (input.size / 6)
    braille_chars << input[index, length]
    index += 6
  end

  capital_follows = 0
  number_follows = 0

  eng_chars = braille_chars.map do |char|
    BRAILLE_ENG[char]
  end

  puts eng_chars.join
end

def eng_to_braille(input)
  translated_words = []
  input.each do |word|
    translated_word = "" 
    word.each_char do |char|
      translated_word << ENG_BRAILLE[char]
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
