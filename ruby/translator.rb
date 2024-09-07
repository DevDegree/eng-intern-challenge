BRAILLE_DICTIONARY = {
  "a" => "O.....",
  "b" => "O.O...",
  "c" => "OO....",
  "d" => "OO.O..",
  "e" => "O..O..",
  "f" => "OOO...",
  "g" => "OOOO..",
  "h" => "O.OO..",
  "i" => ".OO...",
  "j" => ".OOO..",
  "k" => "O...O.",
  "l" => "O.O.O.",
  "m" => "OO..O.",
  "n" => "OO.OO.",
  "o" => "O..OO.",
  "p" => "OOO.O.",
  "q" => "OOOOO.",
  "r" => "O.OOO.",
  "s" => ".OO.O.",
  "t" => ".OOOO.",
  "u" => "O...OO",
  "v" => "O.O.OO",
  "w" => ".OOO.O",
  "x" => "OO..OO",
  "y" => "OO.OOO",
  "z" => "O..OOO",
  " " => "......"
}

BRAILLE_NUMBER = {
  "1" => "O.....",
  "2" => "O.O...",
  "3" => "OO....",
  "4" => "OO.O..",
  "5" => "O..O..",
  "6" => "OOO...",
  "7" => "OOOO..",
  "8" => "O.OO..",
  "9" => ".OO...",
  "0" => ".OOO.."
}

def translate(message)
  case detect_text_type(message)
  when "English"
    translate_to_braille(message)
  when "Braille"
    translate_to_english(message)
  else
    "Unknown input type"
  end
end

def detect_text_type(message)
  if message.include?(".") && message.include?("O")
    "Braille"
  else
    "English"
  end
end

def translate_to_braille(message)
  english_message = message.chars
  number_mode = false
  capitalize_next = false
  translated_message_to_braille = []

  english_message.each_with_index do |char, index|
    if BRAILLE_NUMBER[char] && (!BRAILLE_NUMBER[english_message[index - 1]] || index == 0)
      number_mode = true
      translated_message_to_braille << ".O.OOO" # Number sign in Braille
      translated_message_to_braille << BRAILLE_NUMBER[char]
      number_mode = false
    elsif BRAILLE_NUMBER[char]
      translated_message_to_braille << BRAILLE_NUMBER[char]
    elsif char == char.upcase && char != " "
      translated_message_to_braille << ".....O" # Capital indicator in Braille
      translated_message_to_braille << BRAILLE_DICTIONARY[char.downcase]
    else
      translated_message_to_braille << BRAILLE_DICTIONARY[char.downcase] || "unknown"
    end
  end

  translated_message_to_braille.join
end

def translate_to_english(message)
  braille_message = message.chars.each_slice(6).map(&:join)
  translated_message_to_english = []
  capitalize_next = false
  number_mode = false

  braille_message.each do |braille_char|
    if braille_char == ".....O" # Braille Symbol to indicate that a capital follows
      capitalize_next = true
    elsif braille_char == ".O.OOO" # Braille Symbol to indicate that a number follows
      number_mode = true
    elsif braille_char == "......" # Braille symbol for space
      translated_message_to_english << (number_mode ? BRAILLE_NUMBER.key(braille_char) : BRAILLE_DICTIONARY.key(braille_char))
      number_mode = false
    elsif number_mode
      translated_message_to_english << BRAILLE_NUMBER.key(braille_char)
    elsif capitalize_next
      translated_message_to_english << BRAILLE_DICTIONARY.key(braille_char).upcase
      capitalize_next = false
    else
      translated_message_to_english << BRAILLE_DICTIONARY.key(braille_char)
    end
  end

  translated_message_to_english.join
end

# Example usage:
# puts translate("Hello world")
# puts translate("42")
# puts translate(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")