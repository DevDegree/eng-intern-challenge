alphabet_map = {
  'a' => "O.....",
  'b' => "O.O...",
  'c' => "OO....",
  'd' => "OO.O..",
  'e' => "O..O..",
  'f' => "OOO...",
  'g' => "OOOO..",
  'h' => "O.OO..",
  'i' => ".OO...",
  'j' => ".OOO..",
  'k' => "O...O.",
  'l' => "O.O.O.",
  'm' => "OO..O.",
  'n' => "OO.OO.",
  'o' => "O..OO.",
  'p' => "OOO.O.",
  'q' => "OOOOO.",
  'r' => "O.OOO.",
  's' => ".OO.O.",
  't' => ".OOOO.",
  'u' => "O...OO",
  'v' => "O.O.OO",
  'w' => ".OOO.O",
  'x' => "OO..OO",
  'y' => "OO.OOO",
  'z' => "O..OOO",
  ' ' => "......",
  '.' => "..OO.O",
  ',' => "..O...",
  '?' => "..O.OO",
  '!' => "..OOO.",
  ':' => "..OO..",
  ';' => "..O.O.",
  '-' => "....OO",
  '/' => ".O..O.",
  '<' => ".OO..O",
  '>' => "O..OO.",
  '(' => "O.O..O",
  ')' => ".O.OO.",
  'capital_follows' => '.....O',
  'number_follows' => '.O.OOO'
}

numbers_map = {
  '1' => "O.....",
  '2' => "O.O...",
  '3' => "OO....",
  '4' => "OO.O..",
  '5' => "O..O..",
  '6' => "OOO...",
  '7' => "OOOO..",
  '8' => "O.OO..",
  '9' => ".OO...",
  'O' => ".OOO.."
}

space = '......'
capital_follows = '.....O'
number_follows = '.O.OOO'

input_string = ARGV.join(' ')

capitalize_on = false
number_mode = false

##### if braille #####
if input_string.count('^.O').zero? && (input_string.length % 6).zero?
## split input_string into chunks of 6
  chunks = input_string.scan(/.{1,6}/)
  output = chunks.map do |chunk|
    if chunk == capital_follows
      capitalize_on = true
      next
    elsif chunk == number_follows
      number_mode = true
      next
    elsif capitalize_on
      capitalize_on = false
      alphabet_map.key(chunk).upcase
    elsif number_mode
      if chunk == space # if symbol is space, then space and set number_mode to false
        number_mode = false
        ' '
      else # else convert to number using numbers map
        numbers_map.key(chunk)
      end
    else # convert normally
      alphabet_map.key(chunk)
    end
  end
  output = output.join

else  ##### assume string #####
  output = ''
  input_string.each_char do |char|
    
    if char.to_i.to_s == char # if current char is number
      if number_mode
        output += numbers_map[char]
      else
        # 1. turn on number_mode
        # 2. convert number_follows braille 
        # 3. convert current number
        number_mode = true
        output += number_follows
        output += numbers_map[char]
      end
    elsif char == ' '
      number_mode = false if number_mode # exit out of number mode if it's on
      output += space
    else # assuming current char is alphabet
      output += char == char.upcase ? capital_follows : ''
      output += alphabet_map[char.downcase]
    end

  end
end

puts output