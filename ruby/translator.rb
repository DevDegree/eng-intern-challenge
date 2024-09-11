# Read command line arguments
message = ARGV.join(" ")

if message.empty?
  puts "No message provided for translation"
  puts "Usage: ruby translator.rb <message>"

  exit(0)
end

$braille = {
  "a" => "O.....",
  "b" => 'O.O...',
  "c" => 'OO....',
  "d" => 'OO.O..',
  "e" => 'O..O..',
  "f" => 'OOO...',
  "g" => 'OOOO..',
  "h" => 'O.OO..',
  "i" => '.OO...',
  "j" => '.OOO..',
  "k" => 'O...O.',
  "l" => 'O.O.O.',
  "m" => 'OO..O.',
  "n" => 'OO.OO.',
  "o" => 'O..OO.',
  "p" => 'OOO.O.',
  "q" => 'OOOOO.',
  "r" => 'O.OOO.',
  "s" => '.OO.O.',
  "t" => '.OOOO.',
  "u" => 'O...OO',
  "v" => 'O.O.OO',
  "w" => '.OOO.O',
  "x" => 'OO..OO',
  "y" => 'OO.OOO',
  "z" => 'O..OOO',
  "1" => 'O.....',
  "2" => 'O.O...',
  "3" => 'OO....',
  "4" => 'OO.O..',
  "5" => 'O..O..',
  "6" => 'OOO...',
  "7" => 'OOOO..',
  "8" => 'O.OO..',
  "9" => '.OO...',
  "0" => '.OOO..',
  "." => '..OO.O',
  "," => '..O...',
  "?" => '..O.OO',
  "!" => '..OOO.',
  ":" => '..OO..',
  ";" => '..O.O.',
  "_" => '....OO',
  "/" => '.O..O.',
  "<" => '.OO..O',
  ">" => 'O..OO.',
  "(" => 'O.O..O',
  ")" => '.O.OO.',
  " " => '......',
}

$specials = {
  "cap" => '.....O',
  "dec" => '.O...O',
  "num" => '.O.OOO',
}

# Translates message from English to Braille
def translate_to_braille(message)
  flag_num = false
  result = ""

  message.chars.map do |char|
    if char.match?(/[0-9]/)
      result += $specials["num"] unless flag_num
      result += $braille[char]
      flag_num = true
    elsif char.match?(/[A-Z]/)
      result += $specials["cap"]
      result += $braille[char.downcase]
    elsif char.match?(/\s/)
      result += $braille[char]
      flag_num = false
    else
      result += $braille[char]
    end
  end

  result
end

# Translates message from Braille to English
def translate_to_english(message)
  result = ""
  flag_num = false
  flag_cap = false

  message.chars.each_slice(6) do |char|
    char = char.join

    if char == $specials["num"]
      flag_num = true
    elsif char == $specials["cap"]
      flag_cap = true
    elsif char == $specials["dec"]
      result += "."
    else
      if char == $braille[" "]
        result += " "
        flag_num = false
      elsif flag_num
        result += $braille.keys.find { |key| $braille[key] == char && key.match?(/[0-9]/) }
      elsif flag_cap
        result += $braille.key(char).upcase
        flag_cap = false
      else
        result += $braille.key(char)
      end
    end
  end

  result
end

if message.match?(/^[a-zA-Z0-9 ]+$/)
  puts translate_to_braille(message)
else
  puts translate_to_english(message)
end
