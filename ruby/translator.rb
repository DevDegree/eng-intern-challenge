BRAILLE_TO_ENGLISH = {
  "O....." => "a", "O.O..." => "b", "OO...." => "c", "OO.O.." => "d", "O..O.." => "e",
  "OOO..." => "f", "OOOO.." => "g", "O.OO.." => "h", ".OO..." => "i", ".OOO.." => "j",
  "O...O." => "k", "O.O.O." => "l", "OO..O." => "m", "OO.OO." => "n", "O..OO." => "o",
  "OOO.O." => "p", "OOOOO." => "q", "O.OOO." => "r", ".OO.O." => "s", ".OOOO." => "t",
  "O...OO" => "u", "O.O.OO" => "v", ".OOO.O" => "w", "OO..OO" => "x", "OO.OOO" => "y",
  "O..OOO" => "z", "......" => " "
}

NUMBER_TO_BRAILLE = {
  "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
  "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", "0" => ".OOO.."
}

ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert.merge(NUMBER_TO_BRAILLE)

NUMBER_SIGN = ".O.OOO"
CAPITAL_SIGN = ".....O"

def translate_braille_to_english(braille_str)
  cells = braille_str.scan(/.{6}/)
  result = ""
  number_mode = false
  capital_next = false

  cells.each do |cell|
    case cell
    when NUMBER_SIGN
      number_mode = true
    when CAPITAL_SIGN
      capital_next = true
    else
      if number_mode
        if NUMBER_TO_BRAILLE.invert[cell]
          result += NUMBER_TO_BRAILLE.invert[cell]
        else
          result += "?"
        end
      else
        char = BRAILLE_TO_ENGLISH[cell]
        if char
          result += capital_next ? char.upcase : char
        else
          result += "?"
        end
        capital_next = false
      end
      number_mode = false if NUMBER_TO_BRAILLE.invert[cell].nil?
    end
  end

  result
end

def translate_english_to_braille(english_str)
  result = ""
  number_mode = false

  english_str.chars.each do |char|
    if char =~ /[0-9]/
      result += NUMBER_SIGN unless number_mode
      result += NUMBER_TO_BRAILLE[char]
      number_mode = true
    else
      if number_mode && char =~ /[a-zA-Z]/
        result += "......"  # space after the number sequence
        number_mode = false
      end

      if char =~ /[A-Z]/
        result += CAPITAL_SIGN
        result += ENGLISH_TO_BRAILLE[char.downcase]
      else
        result += ENGLISH_TO_BRAILLE[char] || "......"
      end
    end
  end

  result
end

def main
  input = ARGV.join(" ")
  if input.empty?
    puts "Please provide text to translate."
    exit
  end

  if input =~ /^[O.\s]+$/
    puts translate_braille_to_english(input)
  else
    puts translate_english_to_braille(input)
  end
end

main
