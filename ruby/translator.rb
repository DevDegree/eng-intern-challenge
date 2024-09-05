# Braille Translator

TRANSLATION_TABLE = {
  letters: {
    a: [0],       b: [0, 2],       c: [0, 1],       d: [0, 1, 3],
    e: [0, 3],    f: [0, 1, 2],    g: [0, 1, 2, 3], h: [0, 2, 3],
    i: [1, 2],    j: [1, 2, 3],    k: [0, 4],       l: [0, 2, 4],
    m: [0, 1, 4], n: [0, 1, 3, 4], o: [0, 3, 4],    p: [0, 1, 2, 4],

    q: [0, 1, 2, 3, 4], r: [0, 2, 3, 4], s: [1, 2, 4],    t: [1, 2, 3, 4],
    u: [0, 4, 5],       v: [0, 2, 4, 5], w: [1, 2, 3, 5], x: [0, 1, 4, 5],
    y: [0, 1, 3, 4, 5], z: [0, 3, 4, 5],
  },

  numbers: {
    1 => [0],       2 => [0, 2],       3 => [0, 1],    4 => [0, 1, 3], 5 => [0, 3],
    6 => [0, 1, 2], 7 => [0, 1, 2, 3], 8 => [0, 2, 3], 9 => [1, 2],    0 => [1, 2, 3],
  },

  special: {
    capital_follows: [5],
    decimal_follows: [1, 5],
    number_follows: [1, 3, 4, 5],
  },

  punctuations: {
    ".": [2, 3, 5], ",": [2],       "?": [2, 4, 5], "!": [2, 3, 4],
    ":": [2, 3],    ";": [2, 4],    "-": [4, 5],    "/": [1, 4],
    "<": [1, 2, 5], ">": [0, 3, 4], "(": [0, 2, 5], ")": [1, 3, 4],
    " ": []
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

# @param words [Array<String>]
# @return [Symbol] <code>:braille</code>, <code>:english</code>, <code>:unknown</code>
def determine_language(words)
  if words.all? { |word| word.match?(BRAILLE_PATTERN) }
    :braille
  elsif words.all? { |word| word.match?(ENGLISH_PATTERN) }
    :english
  else
    :unknown
  end
end

# @param words [Array<String>]
# @return [String]
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

# @param text [String]
# @return [String]
def braille_to_english(text)
  english = ""
  state = :letter_or_punctuation

  # scan through each Braille symbol where each symbol consists of 6 characters
  # of either "." or "O" (capital letter "o")
  text.scan(/([.O]{6})/) do |match|
    state = parse_braille_symbol (match[0] || "......"), state, english
  end

  english
end

# @param word [String]
# @return [String]
def english_to_braille(word)
  braille = ""
  previous = ""

  word.each_char do |current|
    previous = parse_english_character current, previous, braille
  end

  braille
end

# @param symbol [String]
# @param state [Symbol]
# @param text [String]
# @return [Symbol]
def parse_braille_symbol(symbol, state, text)
  braille_dots = []
  symbol.chars.each_with_index do |c, i|
    braille_dots << i if c == "O"
  end

  # check if it is a special symbol
  case look_up(:special, braille_dots)&.to_sym
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
        look_up(:letters, braille_dots) \
          || look_up(:punctuations, braille_dots) \
          || ""

      when :capital_follows
        state = :letter_or_punctuation
        look_up(:letters, braille_dots)&.upcase || ""

      when :number_follows
        if look_up(:punctuations, braille_dots) == " "
          # a space represents the end of a number, so the state should be
          # changed and the space should be appended
          state = :letter_or_punctuation
          " "
        else
          # still reading a number, append the digit and the state does not change
          look_up :numbers, braille_dots
        end

      else # unreachable
        raise "Unknown state: \"#{state}\""

      end
  end

  state
end

# @param current [String]
# @param previous [String]
# @param braille_text [String]
# @return [String]
def parse_english_character(current, previous, braille_text)
  if current.match? /[0-9]/ # current is a digit
    # add the number mark unless previous is already a digit or a decimal point
    braille_text << braille_symbol(:special, :number_follows) \
      unless previous.match?(/[0-9.]/)

    braille_text << braille_symbol(:numbers, current.to_i)

  elsif current == "." && previous.match?(/[0-9]/) # current is a decimal point
    braille_text << braille_symbol(:special, :decimal_follows)

  elsif current.match? /[a-z]/i # current is a letter
    # add the capital letter sign if the letter is in upper case
    braille_text << braille_symbol(:special, :capital_follows) \
      if current == current.upcase

    braille_text << braille_symbol(:letters, current.downcase.to_sym)

  else # current is punctuation
    braille_text << braille_symbol(:punctuations, current.to_sym)

  end

  current
end

# Helpers

# @param category [Symbol]
# @param braille_dots [Array<Integer>]
# @return [String, nil]
def look_up(category, braille_dots)
  REVERSE_TRANSLATION_TABLE[category][braille_dots]&.to_s
end

# @param category [Symbol]
# @param key [Symbol, Integer]
# @return [String]
def braille_symbol(category, key)
  braille = "......"
  TRANSLATION_TABLE[category][key]&.each { |i| braille[i] = "O" }
  braille
end

if __FILE__ == $0
  main
end
