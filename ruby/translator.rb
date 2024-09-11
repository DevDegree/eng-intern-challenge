BRAILLE_TO_ENGLISH_ALPHA = {
  "O....." => 'a', "O.O..." => 'b', "OO...." => 'c', "OO.O.." => 'd',
  "O..O.." => 'e', "OOO..." => 'f', "OOOO.." => 'g', "O.OO.." => 'h',
  ".OO..." => 'i', ".OOO.." => 'j', "O...O." => 'k', "O.O.O." => 'l',
  "OO..O." => 'm', "OO.OO." => 'n', "O..OO." => 'o', "OOO.O." => 'p',
  "OOOOO." => 'q', "O.OOO." => 'r', ".OO.O." => 's', ".OOOO." => 't',
  "O...OO" => 'u', "O.O.OO" => 'v', ".OOO.O" => 'w', "OO..OO" => 'x',
  "OO.OOO" => 'y', "O..OOO" => 'z'
}.freeze

BRAILLE_TO_ENGLISH_NUM = {
  "O....." => '1', "O.O..." => '2', "OO...." => '3', "OO.O.." => '4',
  "O..O.." => '5', "OOO..." => '6', "OOOO.." => '7', "O.OO.." => '8',
  ".OO..." => '9', ".OOO.." => '0'
}.freeze

ENGLISH_TO_BRAILLE_ALPHA = BRAILLE_TO_ENGLISH_ALPHA.invert.freeze
ENGLISH_TO_BRAILLE_NUM = BRAILLE_TO_ENGLISH_NUM.invert.freeze
CAPITAL_FOLLOWS = ".....O".freeze
NUMBER_FOLLOWS = ".O.OOO".freeze
SPACE = "......".freeze

def braille?(text)
  return false unless text.match? /^[.O]+$/

  text.length % 6 == 0
end

def translate_braille_to_english(text)
  english_text = ''
  index = 0
  capital_mode = false
  number_mode = false

  while index < text.length
    symbol = text[index, 6]
    index += 6

    if symbol == CAPITAL_FOLLOWS
      capital_mode = true
      next
    elsif symbol == NUMBER_FOLLOWS
      number_mode = true
      next
    elsif symbol == SPACE
      number_mode = false if number_mode

      english_text += ' '
      next
    end

    if number_mode
      english_text += BRAILLE_TO_ENGLISH_NUM[symbol] || ''
    else
      char = BRAILLE_TO_ENGLISH_ALPHA[symbol] || ''
      english_text += capital_mode ? char.upcase : char
      capital_mode = false if capital_mode
    end
  end

  english_text
end

def translate_english_to_braille(text)
  braille_text = ''

  number_mode = false

  text.each_char do |char|
    if char.match?(/[[:digit:]]/)
      unless number_mode
        braille_text += NUMBER_FOLLOWS
        number_mode = true
      end
      braille_text += ENGLISH_TO_BRAILLE_NUM[char] || ''
    elsif char =~ /[A-Z]/
      braille_text += CAPITAL_FOLLOWS
      braille_text += ENGLISH_TO_BRAILLE_ALPHA[char.downcase] || ''
    elsif char == ' '
      braille_text += SPACE
      number_mode = false if number_mode
    else
      braille_text += ENGLISH_TO_BRAILLE_ALPHA[char] || ''
    end
  end

  braille_text
end


text = ARGV.join(' ')
puts braille?(text) ? translate_braille_to_english(text) : translate_english_to_braille(text)
