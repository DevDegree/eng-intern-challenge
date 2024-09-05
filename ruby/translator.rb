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

  # 0: lower case letters or punctuations, 1: capital follows, 2: number follows
  state = 0

  # for each Braille symbol, check the current state and look up the
  # corresponding character of the symbol, add/change characters in certain
  # situations
  text.scan(/([.O]{6})/) do |match|
    braille = match[0] || ""
    raised = raised_dots(braille)
    symbol = REVERSE_TRANSLATION_TABLE[:special][raised]

    if symbol.nil? # if is not a special symbol
      case state
      when 0 # lower case letters or punctuations
        # determine if the symbol represents a letter or a punctuation and append to the output
        english << (REVERSE_TRANSLATION_TABLE[:letters][raised] \
          || REVERSE_TRANSLATION_TABLE[:punctuations][raised]).to_s
      when 1 # upper case letters
        # the letter should be capitalized, and the state should be reset to 0
        english << REVERSE_TRANSLATION_TABLE[:letters][raised].to_s.upcase
        state = 0
      when 2 # numbers or spaces
        # append digits until there is a space, in which case append a space and set state to 0
        if REVERSE_TRANSLATION_TABLE[:special][raised] == " "
          english << " "
          state = 0
        else
          english << REVERSE_TRANSLATION_TABLE[:numbers][raised].to_s
        end
      else
        # unreachable
      end
    else # the current symbol is a special character
      case symbol
      when :capital_follows then state = 1
      when :number_follows then state = 2
      when :decimal_follows then english << "."
      else # unreachable
      end
    end
  end

  english
end

# @param word [String]
# @return [String]
def english_to_braille(word)
  braille = ""
  last_character = ""

  # Read characters one by one, add special symbols when necessary
  word.each_char do |c|
    if c.match? /[0-9]/
      # c is a number
      # add the number sign if necessary
      unless last_character.match?(/[0-9.]/)
        braille << braille_symbol(TRANSLATION_TABLE[:special][:number_follows])
      end
      braille << braille_symbol(TRANSLATION_TABLE[:numbers][c.to_i])
    elsif c == "." && last_character.match?(/[0-9]/)
      # c is a decimal point
      braille << braille_symbol(TRANSLATION_TABLE[:special][:decimal_follows])
    elsif c.match? /[a-z]/i
      # c is a letter
      # add the capital letter sign if the letter is in upper case
      if c == c.upcase
        braille << braille_symbol(TRANSLATION_TABLE[:special][:capital_follows])
      end
      braille << braille_symbol(TRANSLATION_TABLE[:letters][c.downcase.to_sym])
    else # c is non-letter and non-digit symbol
      braille << braille_symbol(TRANSLATION_TABLE[:punctuations][c.to_sym])
    end

    # update last_character
    last_character = c
  end

  braille
end

# @param raised [Array<Integer>] The raised dots of a Braille symbol, should be the indices of the raised dots from 0 to 5.
# @return [String]
def braille_symbol(raised)
  braille = "......"
  raised.each { |i| braille[i] = "O" }
  braille
end

# @param braille [String] A Braille symbol in the form of <code>O..OO..</code>.
# @return [Array<Integer>] The indices of the raised dots.
def raised_dots(braille)
  raised = []
  braille.chars.each_with_index do |c, i|
    raised << i if c == "O"
  end
  raised
end

if __FILE__ == $0
  main
end
