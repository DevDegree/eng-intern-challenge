# frozen_string_literal: true

original_sentence = ARGV.join(' ')

# From https://en.wikipedia.org/wiki/Braille - History - Derivation,
# there are 10 variations of the top 4 dots in a braille letter.
# The bottom two dots are used to decide which charset of 10 chars the top 4 dots reffers to.

# The valid permutations for the top 4 dots are:
# O..., O.O., OO.., OO.O, O..O, OOO., OOOO, O.OO, .OO., .OOO

# For the bottom 2 dots,
#   If the pattern is "..", the braile represents the charset abcdefghij or 1234567890
#   If the pattern is "O.", the braile represents the charset klmnopqrst
#   If the pattern is "OO", the braile represents the charset uvxyz-----
#   If the pattern is ".O", the braile represents the charset w---------

# Special codes are:
#   ".....O", capital follows
#   ".O.OOO", number follows
#   "......", space

# if a number follows sequence is read, the pattern is considered a number until the next space
# the top four dots are mapped to the charset 1234567890.

# The list of possible permutations for the top 4 dots.
TOP_IDS = ['O...', 'O.O.', 'OO..', 'OO.O', 'O..O', 'OOO.', 'OOOO', 'O.OO', '.OO.', '.OOO'].freeze

# Permutations of the bottom 2 dots, and their corresponding charsets.
BOTTOM_IDS = {
  '..' => 'abcdefghij',
  'O.' => 'klmnopqrst',
  'OO' => 'uvxyz',
  '.O' => 'w'
}.freeze

# Special cases
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

NUMBER_CHARSET = '1234567890'

def braile_to_english(braile)
  res = ''

  next_capital = false
  number_mode = false

  (0...(braile.length / 6)).each do |chunk_index|
    # Extract chunk.
    chunk_start = chunk_index * 6
    chunk_end = chunk_start + 6
    chunk = braile[chunk_start...chunk_end]

    # Extract top and bottom ids.
    top_id = chunk[0..3]
    bottom_id = chunk[4..5]

    # Handle spaces.
    if chunk == SPACE
      number_mode = false
      res += ' '
      next
    end

    charset_index = TOP_IDS.index(top_id)

    # Handle number mode.
    if number_mode
      res += NUMBER_CHARSET[charset_index]
      next
    end

    # Handle special cases.
    if chunk == CAPITAL_FOLLOWS
      next_capital = true
      next
    elsif chunk == NUMBER_FOLLOWS
      number_mode = true
      next
    end

    # Obtain charset.
    charset = BOTTOM_IDS[bottom_id]
    res += (next_capital ? charset[charset_index].capitalize : charset[charset_index])

    next_capital = false
  end

  res
end

def english_to_braile(english)
  res = ''

  number_mode = false
  english.split('').each do |char|
    # Handle space.
    if char == ' '
      res += SPACE
      next
    end

    # If upper case, add special flag.
    res += CAPITAL_FOLLOWS if /[[:upper:]]/.match?(char)

    # If start of digit, add a special flag
    is_digit = /[[:digit:]]/.match?(char)
    if is_digit && !number_mode
      number_mode = true
      res += NUMBER_FOLLOWS
    end

    # Handle digit.
    if is_digit
      res += "#{TOP_IDS[NUMBER_CHARSET.index(char)]}.."
      next
    else
      number_mode = false
    end

    # Handle generic chars.
    BOTTOM_IDS.each do |bottom_id, charset|
      charset_index = charset.index(char.downcase)
      res += TOP_IDS[charset_index] + bottom_id unless charset_index.nil?
    end
  end

  res
end

def braile?(sentence)
  /^((O|\.){6})+$/.match?(sentence)
end

if braile?(original_sentence)
  puts braile_to_english(original_sentence)
else
  puts english_to_braile(original_sentence)
end
