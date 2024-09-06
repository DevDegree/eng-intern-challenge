# Braille Translator

TRANSLATION_TABLE = {
  letters: {
    "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..",
    "e" => "O..O..", "f" => "OOO..." ,"g" => "OOOO..", "h" => "O.OO..",
    "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
    "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.", "p" => "OOO.O.",
    "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
    "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
    "y" => "OO.OOO", "z" => "O..OOO",
  },

  numbers: {
    1 => "O.....", 2 => "O.O...", 3 => "OO....", 4 => "OO.O..", 5 => "O..O..",
    6 => "OOO...", 7 => "OOOO..", 8 => "O.OO..", 9 => ".OO...", 0 => ".OOO..",
  },

  special: {
    capital_follows: ".....O",
    decimal_follows: ".O...O",
    number_follows: ".O.OOO",
  },

  punctuations: {
    "." => "..OO.O", "," => "..O...", "?" => "..O.OO", "!" => "..OOO.",
    ":" => "..OO..", ";" => "..O.O.", "-" => "....OO", "/" => ".O..O.",
    "<" => ".OO..O", ">" => "O..OO.", "(" => "O.O..O", ")" => ".O.OO.",
    " " => "......"
  },
}

REVERSE_TRANSLATION_TABLE = {
  letters: TRANSLATION_TABLE[:letters].invert,
  numbers: TRANSLATION_TABLE[:numbers].invert,
  special: TRANSLATION_TABLE[:special].invert,
  punctuations: TRANSLATION_TABLE[:punctuations].invert,
}

BRAILLE_PATTERN = /^(?:[.O]{6})+$/
ENGLISH_PATTERN = /^[a-z0-9.,?!:;\-\/<>() ]+$/i

def main
  words = ARGV
  translated = translate(words)
  puts translated
end

# Determines the language of all given words.
#
# @param words [Array<String>]
# @return [Symbol]
#   <code>:braille</code> if all words are in Braille, <code>:english</code> if
#   all words are in English (contains letters, numbers and punctuation), and
#   <code>:unknown</code> otherwise.
def determine_language(words)
  if words.all? { |word| word.match?(BRAILLE_PATTERN) }
    :braille
  elsif words.all? { |word| word.match?(ENGLISH_PATTERN) }
    :english
  else
    :unknown
  end
end

# Translates the given words.
#
# If the given words are in Braille, translate into English. If the given words
# are in English, then translate into Braille.
#
# @param words [Array<String>] A list of words either in Braille or in English.
# @return [String] The whole text of words translated.
def translate(words)
  language = determine_language(words)

  case language
  when :braille
    # translate from Braille to English
    translated = words.map { |word| braille_to_english(word) }
    translated.join " "
  when :english
    # translate from English to Braille
    translated = words.map { |word| english_to_braille(word) }
    translated.join "......"
  else # some words are not in Braille and not in English
    words.join " "
  end
end

# Translates Braille text into English.
#
# @param text [String] A line of text consists of only Braille symbols.
# @return [String] The Braille symbols translated to English.
def braille_to_english(text)
  english = ""
  state = :letter_or_punctuation

  # scan through each Braille symbol where each symbol consists of 6 characters
  # of either "." or "O" (capital letter "o")
  text.scan(/([.O]{6})/) do |group|
    state = parse_braille_symbol (group[0] || "......"), state, english
  end

  english
end

# Translates a single English word into Braille symbols.
#
# A word in English may contain letters, numbers and punctuation.
#
# @param word [String] A single word in English.
# @return [String] Braille symbols that represents the given English word.
def english_to_braille(word)
  braille = ""
  previous = ""

  word.each_char do |current|
    previous = parse_english_character current, previous, braille
  end

  braille
end

# Parse a single Braille symbol.
#
# The function simulates a state machine. At each step, the function checks the
# given Braille symbol and the current state. Depending on these two factors,
# the state machine decides what text should be appended and which state the
# state machine should transition into in the next step.
#
# @param symbol [String] The Braille symbol the state machine is reading.
# @param state [Symbol] The current state of the state machine.
# @param text [String] The text translated by the state machine so far. May be modified in-place.
# @return [Symbol] The next state of the state machine.
def parse_braille_symbol(symbol, state, text)
  # check if it is a special symbol
  case REVERSE_TRANSLATION_TABLE[:special][symbol]
  when :capital_follows then state = :capital_follows
  when :number_follows then state = :number_follows
  when :decimal_follows
    # in this case, the state should already be in :number_follows, so we only
    # have to append the decimal point and the state does not change
    text << "."

  else # symbol represents a letter, or a digit, or a punctuation
    # determine which character the symbol represents and append it to text, and
    # determine what the next state is based on current state and the symbol
    text << \
      case state
      when :letter_or_punctuation
        REVERSE_TRANSLATION_TABLE[:letters][symbol] \
          || REVERSE_TRANSLATION_TABLE[:punctuations][symbol] \
          || ""

      when :capital_follows
        state = :letter_or_punctuation
        REVERSE_TRANSLATION_TABLE[:letters][symbol]&.upcase || ""

      when :number_follows
        if REVERSE_TRANSLATION_TABLE[:punctuations][symbol] == " "
          # a space represents the end of a number, so the state should be
          # changed and the space should be appended
          state = :letter_or_punctuation
          " "
        else
          # still reading a number, append the digit and the state does not change
          REVERSE_TRANSLATION_TABLE[:numbers][symbol].to_s
        end

      else # unreachable
        raise "Unknown state: \"#{state}\""

      end
  end

  state
end

# Parse a single character in English and append the corresponding Braille
# symbol to the given <code>braille_text</code>.
#
# @param current [String] The current character in English.
# @param previous [String] The previous character in English.
# @param braille_text [String] The Braille symbols translated from previous characters in English.
# @return [String] The next <code>previous</code> character.
def parse_english_character(current, previous, braille_text)
  if current.match? /[0-9]/ # current is a digit
    # add the number mark unless previous is already a digit or a decimal point
    braille_text << TRANSLATION_TABLE[:special][:number_follows] \
      unless previous.match?(/[0-9.]/)

    braille_text << TRANSLATION_TABLE[:numbers][current.to_i]

  elsif current == "." && previous.match?(/[0-9]/) # current is a decimal point
    braille_text << TRANSLATION_TABLE[:special][:decimal_follows]

  elsif current.match? /[a-z]/i # current is a letter
    # add the capital letter sign if the letter is in upper case
    braille_text << TRANSLATION_TABLE[:special][:capital_follows] \
      if current == current.upcase

    braille_text << TRANSLATION_TABLE[:letters][current.downcase]

  else # current is punctuation
    braille_text << TRANSLATION_TABLE[:punctuations][current]

  end

  current
end

if __FILE__ == $0
  main
end
