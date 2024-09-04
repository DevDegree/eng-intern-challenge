# Braille Translator

TRANSLATION_TABLE = {
  a: [0],       b: [0, 2],       c: [0, 1],       d: [0, 1, 3],
  e: [0, 3],    f: [0, 1, 2],    g: [0, 1, 2, 3], h: [0, 2, 3],
  i: [1, 2],    j: [1, 2, 3],    k: [0, 4],       l: [0, 2, 4],
  m: [0, 1, 4], n: [0, 1, 3, 4], o: [0, 3, 4],    p: [0, 1, 2, 4],

  q: [0, 1, 2, 3, 4], r: [0, 2, 3, 4], s: [1, 2, 4],    t: [1, 2, 3, 4],
  u: [0, 4, 5],       v: [0, 2, 4, 5], w: [1, 2, 3, 5], x: [0, 1, 4, 5],
  y: [0, 1, 3, 4, 5], z: [0, 3, 4, 5],

  1 => [0],       2 => [0, 2],       3 => [0, 1],    4 => [0, 1, 3], 5 => [0, 3],
  6 => [0, 1, 2], 7 => [0, 1, 2, 3], 8 => [0, 2, 3], 9 => [1, 2],    0 => [1, 2, 3],

  capital_follows: [5],
  decimal_follows: [1, 5],
  number_follows: [1, 3, 4, 5],

  ".": [2, 3, 5], ",": [2],       "?": [2, 4, 5], "!": [2, 3, 4],
  ":": [2, 3],    ";": [2, 4],    "-": [4, 5],    "/": [1, 4],
  "<": [1, 2, 5], ">": [0, 3, 4], "(": [0, 2, 5], ")": [1, 3, 4],
  " ": []
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

# @param word [String]
# @return [String]
def braille_to_english(word)
  " "
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
        braille << braille_symbol(TRANSLATION_TABLE[:number_follows])
      end
      braille << braille_symbol(TRANSLATION_TABLE[c.to_i])
    elsif c == "." && last_character.match?(/[0-9]/)
      # c is a decimal point
      braille << braille_symbol(TRANSLATION_TABLE[:decimal_follows])
    elsif c.match? /[a-z]/i
      # c is a letter
      # add the capital letter sign if the letter is in upper case
      if c == c.upcase
        braille << braille_symbol(TRANSLATION_TABLE[:capital_follows])
      end
      braille << braille_symbol(TRANSLATION_TABLE[c.downcase.to_sym])
    else # c is non-letter and non-digit symbol
      braille << braille_symbol(TRANSLATION_TABLE[c.to_sym])
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

if __FILE__ == $0
  main
end
