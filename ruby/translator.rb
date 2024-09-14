#!/usr/bin/env ruby

@alpha_crib = [
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "OO..O."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  [" ", "......"], # Space
]
@number_crib = [
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."],
]
@capital_marker = ".....O"
@number_marker = ".O.OOO"

def is_braile(string)
  reduced = string.chars.uniq
  reduced.count == 2 && reduced.include?('.') && reduced.include?('O')
end

def braille_to_alpha(string)
  # All correct braille characters are multiples of 6
  if string.length % 6 != 0
    raise 'Braille is malformed, make sure no spaces are in the input?'
  end
  # Flip keys then make into hash
  alpha_dict = @alpha_crib.map(&:reverse).to_h
  number_dict = @number_crib.map(&:reverse).to_h
  capital_flag = false
  number_flag = false
  string.chars.each_slice(6).map do |slice|
    # translate token
    token = slice.join('')
    # if token is capital, set flags and go on
    if token == @capital_marker
      capital_flag = true
      next nil # short circuit map
    elsif token == @number_marker
      number_flag = true
      next nil
    end

    # Process flags
    if capital_flag
      capital_flag = false
      alpha_dict[token].upcase
    elsif number_flag
      # Do we end flag here?
      if alpha_dict[token] == ' '
        number_flag = false
        ' '
      else
        next number_dict[token]
      end
    else
      next alpha_dict[token]
    end
  end.join('')
end

def alpha_to_braille(input)
  alpha_dict = @alpha_crib.to_h
  number_dict = @number_crib.to_h
  number_flag = false # only flag we need here
  input.chars.flat_map do |token|
    # if token is captial, put marker
    if ('A'..'Z').include? token
      [@capital_marker, alpha_dict[token.downcase]]
    elsif ('0'..'9').include? token
      unless number_flag # is set
        number_flag = true
        [@number_marker, number_dict[token]] # emit first digit with marker
      else
        number_dict[token] # just the digit
      end
    elsif alpha_dict[token] == ' '
      # clear number flag if set, add space
      number_flag = false
      ' '
    else
      alpha_dict[token]
    end
  end.join('')
end

# alpha_text = 'Abc 123 xYz'
# braille_text = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
# if alpha_text == braille_to_alpha(braille_text)
#   puts 'yeh'
# end

# if braille_text = alpha_to_braille(alpha_text)
#   puts 'yeh'
# end

input = ARGV.each.to_a.join(' ')
if is_braile input
  #puts "READING BRAILE"
  puts braille_to_alpha(input)
else
  #puts "READING ALPHA"
  puts alpha_to_braille(input)
end
