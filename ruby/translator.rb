BRAILLE_TO_TEXT = {
  "O....." => "a", "O.O..." => "b", "OO...." => "c", "OO.O.." => "d", "O..O.." => "e",
  "OOO..." => "f", "OOOO.." => "g", "O.OO.." => "h", ".OO..." => "i", ".OOO.." => "j",
  "O...O." => "k", "O.O.O." => "l", "OO..O." => "m", "OO.OO." => "n", "O..OO." => "o",
  "OOO.O." => "p", "OOOOO." => "q", "O.OOO." => "r", ".OO.O." => "s", ".OOOO." => "t",
  "O...OO" => "u", "O.O.OO" => "v", ".OOO.O" => "w", "OO..OO" => "x", "OO.OOO" => "y",
  "O..OOO" => "z",
  
  ".....O" => :capital,   
  ".O.OOO" => :number, 
  "......" => " ", 
}

BRAILLE_NUMBERS = {
  "O....." => "1", "O.O..." => "2", "OO...." => "3", "OO.O.." => "4", "O..O.." => "5",
  "OOO..." => "6", "OOOO.." => "7", "O.OO.." => "8", ".OO..." => "9", ".OOO.." => "0",
}

TEXT_TO_BRAILLE = BRAILLE_TO_TEXT.invert.merge(BRAILLE_NUMBERS.invert)

def braille_to_text(braille_string)
  capital_flag = false
  number_flag = false
  result = ""

  braille_chars = braille_string.scan(/.{6}/)

  braille_chars.each do |braille_char|
    if number_flag
      character = BRAILLE_NUMBERS[braille_char] || BRAILLE_TO_TEXT[braille_char]
    else
      character = BRAILLE_TO_TEXT[braille_char]
    end

    case character
    when :capital
      capital_flag = true
    when :number
      number_flag = true
    when " "
      result += " "
      number_flag = false
    else
      if capital_flag
        result += character.upcase
        capital_flag = false
      else
        result += character
      end
    end
  end

  result
end

def text_to_braille(text)
  result = ""
  number_flag = false

  text.each_char do |char|
    if char =~ /[A-Z]/
      result += TEXT_TO_BRAILLE[:capital] 
      result += TEXT_TO_BRAILLE[char.downcase]  
    elsif char =~ /[0-9]/
      unless number_flag
        result += TEXT_TO_BRAILLE[:number]
        number_flag = true
      end
      result += TEXT_TO_BRAILLE[char]
    elsif char == " "
      result += TEXT_TO_BRAILLE[" "]
      number_flag = false
    else
      result += TEXT_TO_BRAILLE[char] 
      number_flag = false
    end
  end

  result
end

def translate(input_string)
  if input_string =~ /^[\.O]+$/
    puts braille_to_text(input_string)
  else
    puts text_to_braille(input_string)
  end
end

if __FILE__ == $0
  input_string = ARGV.join(" ")

  translate(input_string)
end
