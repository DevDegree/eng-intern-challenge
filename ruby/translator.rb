# Braille alphabet mappings
BRAILLE_ALPHABET = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
  "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
  "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
  "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
  "z" => "O..OOO", " " => "......", "cap" => ".....O", "num" => ".O.OOO", "" => "......"
}

# Braille number mappings
BRAILLE_NUMBERS = {
  "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
  "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", "0" => ".OOO.."
}

# Check if the input string is in Braille format
def is_braille?(input)
  input.match?(/^[O.]+$/)
end

# Translate English text to Braille
def translate_to_braille(text)
  result = ""
  on_numbers = false
  text.each_char do |char|
    if char.match?(/[A-Z]/)
      result += BRAILLE_ALPHABET["cap"]
      char = char.downcase
      on_numbers = false
    end
    if char.match?(/[0-9]/)
      if on_numbers == false
        result += BRAILLE_ALPHABET["num"]
      end
      result += BRAILLE_NUMBERS[char]
      on_numbers = true
    else
      result += BRAILLE_ALPHABET[char]
      on_numbers = false
    end
  end
  result
end

# Translate Braille to English text
def translate_to_english(braille)
  result = ""
  on_numbers = false
  i = 0
  while i < braille.length
    if braille[i, 6] == BRAILLE_ALPHABET["cap"]
      i += 6
      char = BRAILLE_ALPHABET.key(braille[i, 6]).upcase
      on_numbers = false
    elsif braille[i, 6] == BRAILLE_ALPHABET["num"]
      i += 6
      char = BRAILLE_NUMBERS.key(braille[i, 6])
      on_numbers = true
    elsif braille[i, 6] == BRAILLE_ALPHABET[" "]
      char = " "
      on_numbers = false
    elsif braille[i, 6] == BRAILLE_NUMBERS[""]
      char = ""
    else
      if on_numbers == true
        char = BRAILLE_NUMBERS.key(braille[i, 6])
      else
        char = BRAILLE_ALPHABET.key(braille[i, 6])
      end
    end
    result += char
    i += 6
  end
  result
end

# Main execution block
if __FILE__ == $0
  input = ARGV.join(" ")
  if is_braille?(input)
    puts translate_to_english(input)
  else
    puts translate_to_braille(input)
  end
end