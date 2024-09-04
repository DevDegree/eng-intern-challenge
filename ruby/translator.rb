ALPHABET_TO_BRAILLE = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..",
  "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.",
  "o" => "O..OO.", "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.", "u" => "O...OO",
  "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO", "z" => "O..OOO",
  "capital" => ".....O",
  " " => "......"
}

NUMBER_TO_BRAILLE = {
  "number" => ".O.OOO","0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...",
  "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", " " => "......",
}

BRAILLE_TO_ALPHABET = ALPHABET_TO_BRAILLE.invert
BRAILLE_TO_NUMBER = NUMBER_TO_BRAILLE.invert

def translate_to_braille(text)
  result = ''
  number_sequence = false

  text.chars.each do |char|
    if char.match(/[A-Z]/)
      result += (ALPHABET_TO_BRAILLE['capital']) + (ALPHABET_TO_BRAILLE[char.downcase])
      number_sequence = false
    elsif char.match(/\d/)
      if !number_sequence
        result += NUMBER_TO_BRAILLE['number']
        number_sequence = true
      end
      result += (NUMBER_TO_BRAILLE[char])
    else
      result += (ALPHABET_TO_BRAILLE[char] || ALPHABET_TO_BRAILLE[' '])
      number_sequence = false
    end
  end
  result
end

def translate_to_english(input)
  solution = ""
  check_capital = false
  number_mode = false
  curr_string = ''

  input.each_char do |char|
    curr_string += char

    if curr_string.length == 6
      if curr_string == ALPHABET_TO_BRAILLE['capital']
        check_capital = true
      elsif curr_string == NUMBER_TO_BRAILLE['number']
        number_mode = true
      else
        if curr_string == ALPHABET_TO_BRAILLE[" "] && number_mode
          char = BRAILLE_TO_ALPHABET.fetch(curr_string, '')
          number_mode = false
        elsif number_mode
          char = BRAILLE_TO_NUMBER.fetch(curr_string, '')
        else
          char = BRAILLE_TO_ALPHABET.fetch(curr_string, '')
          if check_capital
            char = char.upcase
            check_capital = false
          end
        end
        solution += char
      end
      curr_string = ''
    end
  end
  solution
end





def determine_input_type(input)
  input.include?('O') || input.include?('.')
end

def main(args)
  input = args.join(' ')

  if determine_input_type(input)
    puts translate_to_english(input)
  else
    puts translate_to_braille(input)
  end
end

# Command-line execution
main([".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"])