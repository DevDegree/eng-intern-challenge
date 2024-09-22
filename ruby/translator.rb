input = ARGV.join(' ')

# puts input.to_s

# this check is a little bit faster than looping through every character
is_braille = input.include?('.')

# # puts "Is braille", is_braille
#
# puts "Input", input

c_to_b = {
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
  ' ' => '......',
}

# number to braille has conflicts with character to braille
num_to_b = {
  '1' => 'O.....',
  '2' => 'O.O...',
  '3' => 'OO....',
  '4' => 'OO.O..',
  '5' => 'O..O..',
  '6' => 'OOO...',
  '7' => 'OOOO..',
  '8' => 'O.OO..',
  '9' => '.OO...',
  '0' => '.OOO..'
}

b_to_c = c_to_b.invert
b_to_num = num_to_b.invert

# merging character to braille because no conflicts
c_to_b.merge!(num_to_b)

# puts "Is braille", is_braille

capital_mode = false
# don't need this...
# decimal_mode = false
number_mode = false

if is_braille
  final_str = ""
  (0...input.length).step(6) do |index|
    chunk = input[index, 6]
    # puts "analyzing chunk", chunk
    # puts "In map", b_to_c[chunk]
    # puts "Is capital", chunk == '.....O'
    # puts "analzying chunk: '#{chunk}' (length: #{chunk.length})"
    case chunk.strip
    when '.....O'
      # puts "Capital mode!"
      capital_mode = true
    when '.O.OOO'
      number_mode = true
    when '......'
      # disable number/decimal after space
      number_mode = false
      final_str += ' '
    else
      if capital_mode
        # because capital only works for a single character
        capital_mode = false
        final_str += b_to_c[chunk].upcase
      elsif number_mode
        # hash map uses lowercase
        final_str += b_to_num[chunk]
      else
        final_str += b_to_c[chunk]
      end
    end
  end
  puts final_str
else
  # some shit here
  final_str = ""
  input.chars.map do |char|
    case char
    when 'A'..'Z'
      # capital letter = capital mode
      final_str += ".....O"
    when '0'..'9'
      # enable number mode if not already enabled
      if !number_mode
        number_mode = true
        final_str += '.O.OOO'
      end
    when ' '
      number_mode = false
      # puts "Detected space", char, char.downcase
      # puts "Braille: ", c_to_b[char.downcase]
      # final_str += c_to_b[' '] 
      # next
    end
    # puts "Debugging char", char, char.downcase
    # puts "Corresponding", c_to_b[char.downcase]
    # puts "HP", c_to_b
    final_str += c_to_b[char.downcase]
  end
  puts final_str
end
