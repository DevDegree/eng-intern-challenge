# translator.rb

braille_alphabet = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..",
  "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..",
  "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
  "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.", "p" => "OOO.O.",
  "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
  "y" => "OO.OOO", "z" => "O..OOO", " " => "......",
  "capital" => ".....O", "number" => ".O.OOO",
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....",
  "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...", "7" => "OOOO..",
  "8" => "O.OO..", "9" => ".OO..."
}

def english_to_braille(text, braille_alphabet)
  output = ""
  in_number_mode = false
  text.each_char do |char|
    if char =~ /[A-Z]/
      output += braille_alphabet["capital"]
      output += braille_alphabet[char.downcase]
      in_number_mode = false
    elsif char =~ /\d/
      unless in_number_mode
        output += braille_alphabet["number"]
        in_number_mode = true
      end
      output += braille_alphabet[char]
    else
      in_number_mode = false if char == " "
      output += braille_alphabet[char] || ''
    end
  end
  output
end

def braille_to_english(braille, braille_alphabet)
  reversed_alphabet = braille_alphabet.invert
  english = ""
  i = 0
  capitalize_next = false
  in_number_mode = false

  while i < braille.length
    current_symbol = braille[i, 6]

    if current_symbol == braille_alphabet["capital"]
      capitalize_next = true
      i += 6
      next
    elsif current_symbol == braille_alphabet["number"]
      in_number_mode = true
      i += 6
      next
    elsif current_symbol == braille_alphabet[" "]
      english += " "
      in_number_mode = false
      i += 6
      next
    else
      char = reversed_alphabet[current_symbol] || ''
      if in_number_mode && char =~ /[a-j]/
        char = (reversed_alphabet[current_symbol].ord - 'a'.ord).to_s
      end
      char = char.upcase if capitalize_next
      capitalize_next = false
      english += char
    end
    i += 6
  end
  english
end

input = ARGV[0]

if input =~ /^[O.]+$/
  puts braille_to_english(input, braille_alphabet)
else
  puts english_to_braille(input, braille_alphabet)
end
