
BRAILLE_TO_ENGLISH = {
  "O....." => "a",
  "O.O..." => "b",
  "OO...." => "c",
  "OO.O.." => "d",
  "O..O.." => "e",
  "OOO..." => "f",
  "OOOO.." => "g",
  "O.OO.." => "h",
  ".OO..." => "i",
  ".OOO.." => "j",
  "O...O." => "k",
  "O.O.O." => "l",
  "OO..O." => "m",
  "OO.OO." => "n",
  "O..OO." => "o",
  "OOO.O." => "p",
  "OOOOO." => "q",
  "O.OOO." => "r",
  ".OO.O." => "s",
  ".OOOO." => "t",
  "O...OO" => "u",
  "O.O.OO" => "v",
  ".OOO.O" => "w",
  "OO..OO" => "x",
  "OO.OOO" => "y",
  "O..OOO" => "z",
}

BRAILLE_TO_DIGITS = {
  "O....." => "1",
  "O.O..." => "2",
  "OO...." => "3",
  "OO.O.." => "4",
  "O..O.." => "5",
  "OOO..." => "6",
  "OOOO.." => "7",
  "O.OO.." => "8",
  ".OO..." => "9",
  ".OOO.." => "0",
}

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_SPACE = "......"

# Inverse map
ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.map { |k, v| [v, k] }.to_h
DIGITS_TO_BRAILLE = BRAILLE_TO_DIGITS.map { |k, v| [v, k] }.to_h

def translate_braille_to_english(braille)
  raise "Length should be multiple of 6" unless braille.length % 6 == 0

  result = ""

  capital_mode = false
  number_mode = false

  for i in 0...(braille.length / 6)
    # Get next block of 6 characters
    braille_letter = braille[i * 6, 6]

    if braille_letter == BRAILLE_CAPITAL_FOLLOWS
      capital_mode = true
    elsif braille_letter == BRAILLE_NUMBER_FOLLOWS
      number_mode = true
    elsif braille_letter == BRAILLE_SPACE
      result += " "
      number_mode = false
      capital_mode = false
    else
      if number_mode
        result += BRAILLE_TO_DIGITS[braille_letter]
      elsif capital_mode
        result += BRAILLE_TO_ENGLISH[braille_letter].upcase
        capital_mode = false
      else
        result += BRAILLE_TO_ENGLISH[braille_letter]
      end
    end
  end

  result
end

def translate_english_to_braille(english)
  result = ""

  number_mode = false

  for i in 0...(english.length)
    char = english[i]

    if !number_mode
      if char.ord >= "A".ord && char.ord <= "Z".ord
        # If capitalized
        result += BRAILLE_CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.downcase]
      elsif char.ord >= "0".ord && char.ord <= "9".ord
        # If start of number
        result += BRAILLE_NUMBER_FOLLOWS + DIGITS_TO_BRAILLE[char]
        number_mode = true
      elsif char === " "
        result += BRAILLE_SPACE
      else
        result += ENGLISH_TO_BRAILLE[char]
      end
    else
      if char.ord >= "0".ord && char.ord <= "9".ord
        result += DIGITS_TO_BRAILLE[char]
      elsif char === " "
        result += BRAILLE_SPACE
        # End number mode
        number_mode = false
      else
        # As required in the spec, assume 
        raise "Invalid number terminator character"
      end
    end
  end

  result
end

def is_valid_braille(s)
  # Multiple of 6 characters and consists of . and O characters
  s.length % 6 == 0 && /^[.O]*$/.match(s)
end

def main
  input_string = ARGV.join(" ")

  if is_valid_braille(input_string)
    puts translate_braille_to_english(input_string)
  else
    puts translate_english_to_braille(input_string)
  end
end

main
