#!/usr/bin/env ruby

ENGLISH_TO_BRAILLE = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..", "f" => "OOO...",
  "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
  "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.", "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.",
  "s" => ".OO.O.", "t" => ".OOOO.", "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
  "y" => "OO.OOO", "z" => "O..OOO", " " => "......", "." => "..OO.O", "," => "..O...", "?" => "..O.O.",
  "!" => "..OOO.", ":" => "OO....", ";" => "..0.0.", "-" => "..O..O", "/" => ".O..O.", "(" => ".O.O.O",
  ")" => ".O.O.O", "cap_next" => ".....O", "num_next" => ".O.OOO", "decimal_next" => ".O...O"
}

BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.invert

NUMS_TO_BRAILLE = {
  "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
  "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", "0" => ".OOO.."
}

BRAILLE_TO_NUMS = NUMS_TO_BRAILLE.invert

def is_braille(input)
  (input.length % 6 == 0) && input.chars.all? { |c| c == 'O' || c == '.' }
end

def translate_to_braille(input)
  result = ""
  num_marker = false

  input.each_char do |char|
    if char =~ /\d/
      unless num_marker
        result += ENGLISH_TO_BRAILLE['num_next']
        num_marker = true
      end
      result += NUMS_TO_BRAILLE[char]
    elsif char =~ /[A-Za-z]/
      result += ENGLISH_TO_BRAILLE['cap_next'] if char =~ /[A-Z]/
      result += ENGLISH_TO_BRAILLE[char.downcase]
    elsif char == " "
      result += ENGLISH_TO_BRAILLE[char]
      num_marker = false
    elsif ENGLISH_TO_BRAILLE.key?(char)
      result += ENGLISH_TO_BRAILLE[char]
    end
  end

  result
end

def translate_to_english(input)
  chars = input.scan(/.{1,6}/)
  result = ""
  num_marker = false
  cap_next = false

  chars.each do |brl|
    if brl == ".....O"
      cap_next = true
    elsif brl == ".O.OOO"
      num_marker = true
    elsif brl == "......"
      num_marker = false
      result += BRAILLE_TO_ENGLISH[brl]
    else
      if num_marker
        result += BRAILLE_TO_NUMS[brl]
      elsif cap_next
        result += BRAILLE_TO_ENGLISH[brl].upcase
        cap_next = false
      else
        result += BRAILLE_TO_ENGLISH[brl]
      end
    end
  end

  result
end

def translate(input)
  if is_braille(input)
    translate_to_english(input)
  else
    translate_to_braille(input)
  end
end

if __FILE__ == $0
  if ARGV.length > 0
    input = ARGV.join(" ")
    result = translate(input)
    puts result
  else
    puts "Did not provide a string argument"
  end
end

