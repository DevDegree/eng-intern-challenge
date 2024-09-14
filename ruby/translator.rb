@alphabet_braille = [
  ['a', 'O.....'],
  ['b', 'O.O...'],
  ['c', 'OO....'],
  ['d', 'OO.O..'],
  ['e', 'O..O..'],
  ['f', 'OOO...'],
  ['g', 'OOOO..'],
  ['h', 'O.OO..'],
  ['i', '.OO...'],
  ['j', '.OOO..'],
  ['k', 'O...O.'],
  ['l', 'O.O.O.'],
  ['m', 'OO..O.'],
  ['n', 'OO.OO.'],
  ['o', 'O..OO.'],
  ['p', 'OOO.O.'],
  ['q', 'OOOOO.'],
  ['r', 'O.OOO.'],
  ['s', '.OO.O.'],
  ['t', '.OOOO.'],
  ['u', 'O...OO'],
  ['v', 'O.O.OO'],
  ['w', '.OOO.O'],
  ['x', 'OO..OO'],
  ['y', 'OO.OOO'],
  ['z', 'O..OOO'],
  [' ', '......'],
]
@number_braille = [
  ['1', 'O.....'],
  ['2', 'O.O...'],
  ['3', 'OO....'],
  ['4', 'OO.O..'],
  ['5', 'O..O..'],
  ['6', 'OOO...'],
  ['7', 'OOOO..'],
  ['8', 'O.OO..'],
  ['9', '.OO...'],
  ['0', '.OOO..'],
]
@capital_follows = '.....O'
@number_follows  = '.O.OOO'

# Check if the input is Braille.
def is_braille(string)
  unique_chars = string.chars.uniq
  unique_chars.size == 2 && unique_chars.include?('.') && unique_chars.include?('O')
end

# Convert Braille to English.
def braille_to_english(string)
  # All correct braille characters are multiples of 6
  if string.size % 6 != 0
    raise 'Invalid Braille, make sure no spaces are in the input?'
  end

  braille_to_alpha_dict = @alphabet_braille.map(&:reverse).to_h
  braille_to_number_dict = @number_braille.map(&:reverse).to_h
  process_capital = false
  process_number = false

  string.chars.each_slice(6).map do |slice|
    braille = slice.join('')

    # Skip the capital and number follow characters
    if braille == @capital_follows
      process_capital = true
      next nil
    elsif braille == @number_follows
      process_number = true
      next nil
    end

    # Process the capital and number follow characters
    if process_capital
      process_capital = false
      braille_to_alpha_dict[braille].upcase
    elsif process_number
      if braille_to_alpha_dict[braille] == ' '
        process_number = false
        ' '
      else
        braille_to_number_dict[braille]
      end
    else
      braille_to_alpha_dict[braille]
    end
  end.join('')
end

# Convert English to Braille.
def english_to_braille(string)
  alphabet_to_braille_dict = @alphabet_braille.to_h
  number_to_braille_dict = @number_braille.to_h
  process_number = false

  string.chars.flat_map do |value|
    if ('A'..'Z').include?(value)
      # Capital letters are followed by a capital follow character.
      [@capital_follows, alphabet_to_braille_dict[value.downcase]]
    elsif ('0'..'9').include?(value)
      if process_number
        number_to_braille_dict[value]
      else
        process_number = true
        # Numbers are followed by a number follow character.
        [@number_follows, number_to_braille_dict[value]]
      end
    elsif alphabet_to_braille_dict[value] == ' '
      process_number = false
      ' '
    else
      alphabet_to_braille_dict[value]
    end
  end.join('')
end

# Get the user input and determine if it's Braille or English.
user_input = ARGV.join(' ')
if is_braille(user_input)
  puts braille_to_english(user_input)
else
  puts english_to_braille(user_input)
end
