# English to Braille mapping, including capital and number follows symbols
$english_to_braille = {
  'a' => 'O.....',
  'b' => 'O.O...',
  'c' => 'OO....',
  'd' => 'OO.O..',
  'e' => 'O..O..',
  'f' => 'OOO...',
  'g' => 'OOOO..',
  'h' => 'O.OO..',
  'i' => '.OO...',
  'j' => '.OOO..',
  'k' => 'O...O.',
  'l' => 'O.O.O.',
  'm' => 'OO..O.',
  'n' => 'OO.OO.',
  'o' => 'O..OO.',
  'p' => 'OOO.O.',
  'q' => 'OOOOO.',
  'r' => 'O.OOO.',
  's' => '.OO.O.',
  't' => '.OOOO.',
  'u' => 'O...OO',
  'v' => 'O.O.OO',
  'w' => '.OOO.O',
  'x' => 'OO..OO',
  'y' => 'OO.OOO',
  'z' => 'O..OOO',
}
  # Numbers (same pattern as letters a-j)
$eng_braille_num = {
  1 => 'O.....',
  2 => 'O.O...',
  3 => 'OO....',
  4 => 'OO.O..',
  5 => 'O..O..',
  6 => 'OOO...',
  7 => 'OOOO..',
  8 => 'O.OO..',
  9 => '.OO...',
  0 => '.OOO..'
}

  # Special symbols
$eng_special_sym = {
  'capital' => '.....O',
  'number' => '.O.OOO',
  'decimal' => '.O...O'
}


# Special characters and space in Braille
$eng_special_char_to_braille = {
  ' '  => '......',
  '.'  => '..OO.O',
  ','  => '..O...',
  '?'  => '..O.OO',
  '!'  => '..OOO.',
  ':'  => '..OO..',
  ';'  => '..O.O.',
  '-'  => '....OO',
  '/'  => '.O..O.',
  '('  => 'O.O..O',
  ')'  => '.O.OO.',
  '<'  => '.OO..O',
  '>'  => 'O..OO.'
}

$braille_to_english = $english_to_braille.invert
$braille_eng_num = $eng_braille_num.invert
$braille_special_sym = $eng_special_sym.invert
$braille_special_char_to_eng = $eng_special_char_to_braille.invert

input = ARGV.join(" ")
def eng_or_braille(input)
 input = input.to_s if input.is_a?(Integer)
 if input.is_a?(Integer) || (!input.match(/^[O.]+$/) && input.match(/[a-zA-Z]/)) || input.match?(/\d/)
  eng_to_braille(input)
 else
  braille_to_eng(input)
 end
end

# translate from English to Braille
def eng_to_braille(input)
 translation = ""
 is_num = false

 input.each_char do |char|
  if char == " "
   translation << $eng_special_char_to_braille[' ']
   is_num = false  # Reset number mode on space

  elsif $eng_special_char_to_braille[char]  # Special characters
   translation << $eng_special_char_to_braille[char]

  elsif char.match?(/\d/)  # Numbers
   if !is_num
    translation << $eng_special_sym["number"]  # Append number symbol
    is_num = true
   end
   translation << $eng_braille_num[char.to_i]

  elsif char == char.upcase  # Capitalization
   translation << $eng_special_sym["capital"] << $english_to_braille[char.downcase]

  else  # Regular letters
   translation << $english_to_braille[char]
  end
 end

 puts translation
end

def braille_to_eng(braille_input)
 translation = ""
 is_num = false
 is_capital = false

 # Split Braille into 6-dot chunks
 braille_input.scan(/.{6}/).each do |braille_char|
  if braille_char == $braille_special_sym["number"]
   is_num = true

  elsif braille_char == $braille_special_sym["capital"]
   is_capital = true

  elsif is_num
   translation << $braille_eng_num[braille_char]

  elsif $braille_special_char_to_eng[braille_char]  # Handle special characters in reverse
   translation << $braille_special_char_to_eng[braille_char]

  else
   letter = $braille_to_english[braille_char]
   translation << (is_capital ? letter.upcase : letter)  # Handle capitalization
   is_capital = false
  end
 end

 puts translation
end


eng_or_braille(input)