ALPHABET_TO_BRAILLE = {
"a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..",
"h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.",
"o" => "O..OO.", "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.", "u" => "O...OO",
"v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO", "z" => "O..OOO",

"capital" => ".....O",
"number" => ".O.OOO",

" " => "......",
}

NUMBER_TO_BRAILLE = {
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...",
  "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", " " => "......",
}

BRAILLE_TO_ALPHABET = ALPHABET_TO_BRAILLE.to_a.reverse.to_h
BRAILLE_TO_NUMBER = NUMBER_TO_BRAILLE.to_a.reverse.to_h

# to_braile returns -1 if input is invalid
def convert_braille_to_alphabet(input)
  return -1 unless input.length % 6 == 0

  result = ""
  next_char_is_capital = false
  next_char_is_number = false

  input.scan(/.{6}/).each do |chunk|
    case chunk
    when ALPHABET_TO_BRAILLE["capital"]
      next_char_is_capital = true
      next_char_is_number = false
    when ALPHABET_TO_BRAILLE["number"]
      next_char_is_capital = false
      next_char_is_number = true
    when ALPHABET_TO_BRAILLE[" "]
      result += " "
      next_char_is_number = false
    else
      character = if next_char_is_number
                    BRAILLE_TO_NUMBER.key(chunk)
                  else
                    BRAILLE_TO_ALPHABET.key(chunk)
                  end
      if next_char_is_capital
        character = character.upcase
        next_char_is_capital = false
      end
      return -1 unless character
      result += next_char_is_capital ? character.upcase : character
      next_char_is_capital = false
    end
    next
  end

  return result
end

def convert_alphabet_to_braille(input)
  result = ""
  next_char_is_number = false

  input.each_char do |char|
    if char.ord >= 48 and char.ord <= 57
      unless next_char_is_number
        result += ALPHABET_TO_BRAILLE["number"]
        next_char_is_number = true
      end
      result += NUMBER_TO_BRAILLE[char]
    elsif char == " "
      result += ALPHABET_TO_BRAILLE[" "]
      next_char_is_number = false
    elsif char.ord >= 65 and char.ord <= 90
      result += ALPHABET_TO_BRAILLE["capital"]
      char = char.downcase
      result += ALPHABET_TO_BRAILLE[char]
      next_char_is_number = false
    else
      result += ALPHABET_TO_BRAILLE[char]
      next_char_is_number = false
    end
  end
  return result
end

if ARGV.length < 1
  puts "Usage: ruby translator.rb <input>"
  exit
end

code = convert_braille_to_alphabet(ARGV[0])
if code == -1 # invalid input
  input = ARGV.join(' ')
  if input.match?(/[^a-zA-Z0-9 ]/)
    puts "Invalid characters detected!"
    exit
  end
  code = convert_alphabet_to_braille(input)
end
puts code
