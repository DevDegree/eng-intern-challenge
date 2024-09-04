BRAILLE_ALPHABET = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
  "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
  "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
  "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
  "z" => "O..OOO",
  " " => "......", 
  "cap" => ".....O",
  "num" => ".O.OOO"  
}

BRAILLE_NUMBERS = {
  "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
  "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", "0" => ".OOO.."
}

# translating Braille back to English
ENGLISH_ALPHABET = BRAILLE_ALPHABET.invert.merge(BRAILLE_NUMBERS.invert)

# check if a string is in Braille format
def braille?(input)
  input.match?(/^[O.]+$/)
end

# translate English to Braille
def translate_to_braille(input)
  braille_output = ''
  number_mode = false
  
  input.each_char do |char|
    if char =~ /[A-Z]/
      braille_output += BRAILLE_ALPHABET["cap"]
      braille_output += BRAILLE_ALPHABET[char.downcase]
      number_mode = false
    elsif char =~ /[0-9]/
      unless number_mode
        braille_output += BRAILLE_ALPHABET["num"]
        number_mode = true
      end
      braille_output += BRAILLE_NUMBERS[char]
    else
      braille_output += BRAILLE_ALPHABET[char]
      number_mode = false
    end
  end

  braille_output
end

# translate Braille to English
def translate_to_english(input)
  english_output = ''
  i = 0
  is_number_mode = false
  
  while i < input.length
    current_char = input[i, 6]

    if current_char == BRAILLE_ALPHABET["cap"]
      i += 6
      next_char = input[i, 6]
      english_output += ENGLISH_ALPHABET[next_char]&.upcase || '?'
    elsif current_char == BRAILLE_ALPHABET["num"]
      is_number_mode = true
    elsif current_char == "......"  # Space character
      english_output += " "
      is_number_mode = false  # Reset number mode after a space
    else
      if is_number_mode
        english_output += ENGLISH_ALPHABET[current_char] || '?'
        is_number_mode = false if BRAILLE_NUMBERS.value?(current_char)
      else
        english_output += ENGLISH_ALPHABET[current_char] || '?'
      end
    end
    i += 6
  end
  english_output
end


input = ARGV.join(" ")

if braille?(input)
  puts translate_to_english(input)
else
  puts translate_to_braille(input)
end
