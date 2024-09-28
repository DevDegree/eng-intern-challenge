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

SPACE = '......'
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

input_string = ARGV.join(' ')

capslock_on = false
number_mode = false

##### if braille #####
if input_string.count('^.O').zero? && (input_string.length % 6).zero?
## split input_string into chunks of 6
  chunks = input_string.scan(/.{1,6}/)
  output = chunks.map do |chunk|
    if chunk == CAPITAL_FOLLOWS
      capslock_on = true
      next
    elsif chunk == NUMBER_FOLLOWS
      number_mode = true
      next
    elsif capslock_on
      capslock_on = false
      alphabet_map.key(chunk).upcase
    elsif number_mode
      if chunk == SPACE
        number_mode = false
        ' '
      else # else convert to number using numbers map
        numbers_map.key(chunk)
      end
    else # convert alphabet
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
        number_mode = true
        output += NUMBER_FOLLOWS
        output += numbers_map[char]
      end
    elsif char == ' '
      number_mode = false
      output += SPACE
    else # assuming current char is alphabet
      output += char == char.upcase ? CAPITAL_FOLLOWS : ''
      output += alphabet_map[char.downcase]
    end
  end
end

puts output