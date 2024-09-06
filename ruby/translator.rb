
BRAILLE_CHAR_LENGTH = 6
NUMBER_PREFIX = ".O.OOO"
CAPITAL_PREFIX = ".....O"

ENGLISH_TO_BRAILLE = {
  'a' => "O.....", 'b' => "O.O...", 'c' => "OO....", 'd' => "OO.O..", 'e' => "O..O..",
  'f' => "OOO...", 'g' => "OOOO..", 'h' => "O.OO..", 'i' => ".OO...", 'j' => ".OOO..",
  'k' => "O...O.", 'l' => "O.O.O.", 'm' => "OO..O.", 'n' => "OO.OO.", 'o' => "O..OO.",
  'p' => "OOO.O.", 'q' => "OOOOO.", 'r' => "O.OOO.", 's' => ".OO.O.", 't' => ".OOOO.",
  'u' => "O...OO", 'v' => "O.O.OO", 'w' => ".OOO.O", 'x' => "OO..OO", 'y' => "OO.OOO",
  'z' => "O..OOO", ' ' => "......"
}

def english_to_braille(text)
  result = ""
  is_number = false

  text.each_char do |char|
    if char.match?(/[A-Z]/)
      result += CAPITAL_PREFIX
      char = char.downcase
    end

    if char.match?(/\d/)
      unless is_number
        result += NUMBER_PREFIX
        is_number = true
      end
      if char == '0'
        result += ENGLISH_TO_BRAILLE['j']
      else
        result += ENGLISH_TO_BRAILLE[(char.to_i - 1 + 'a'.ord).chr]
      end
    else
      is_number = false if char != ' '
      result += ENGLISH_TO_BRAILLE[char]
    end
  end

  result
end

if __FILE__ == $0
  puts ARGV.map { |word| english_to_braille(word) }.join(ENGLISH_TO_BRAILLE[' '])
end