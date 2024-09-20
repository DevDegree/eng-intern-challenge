require_relative 'braille_alphabet'

input = ARGV.join(" ")

# detects lanugage
def is_braille?(input)
  return false unless input.length % 6 == 0 # if the input is not divisible by 6, it's not braille
  input.chars.each_slice(6).all? { |chunk| BRAILLE_ALPHABET.value?(chunk.join) || BRAILLE_SYMBOLS.value?(chunk.join) }
end

# translates braille to english
def translate_braille_to_eng(input)
  translated_string = ""
  capitalize = false
  numberize = false
  decimalize = false

  input.chars.each_slice(6).each do |chunk|
    symbol = chunk.join

    if capitalize
      translated_string << BRAILLE_ALPHABET.key(symbol).upcase
      capitalize = false
    elsif symbol == ".....O"
      capitalize = true
    elsif numberize && symbol == "......"
      translated_string << BRAILLE_SYMBOLS.key(symbol)
      numberize = false
    elsif numberize
      translated_string << BRAILLE_SYMBOLS.key(symbol)
    elsif symbol == ".O.OOO"
      numberize = true
    elsif decimalize
      translated_string << BRAILLE_SYMBOLS.key(symbol)
      decimalize = false
    elsif symbol == ".O...O"
      decimalize = true
    elsif BRAILLE_ALPHABET.value?(symbol)
      translated_string << BRAILLE_ALPHABET.key(symbol)
    else
      translated_string << BRAILLE_SYMBOLS.key(symbol)
    end
  end
  translated_string
end

# translates english to braille
def translate_eng_to_braille(input)
  translated_string = ""
  numberize = false

  input.chars.each do |char|
    if  char == char.to_i.to_s && !numberize
      translated_string << BRAILLE_SYMBOLS["num"]
      translated_string << BRAILLE_SYMBOLS[char]
      numberize = true
    elsif BRAILLE_SYMBOLS.key?(char) && !numberize
      translated_string << BRAILLE_SYMBOLS[char]
    elsif BRAILLE_SYMBOLS.key?(char) && numberize
      translated_string << BRAILLE_SYMBOLS[char]
    elsif char == " " && numberize
      numberize = false
      translated_string << BRAILLE_SYMBOLS[char]
    elsif BRAILLE_SYMBOLS.key?(char)
      translated_string << BRAILLE_SYMBOLS[char]
    elsif char == char.upcase && BRAILLE_ALPHABET.key?(char.downcase)
      translated_string << BRAILLE_SYMBOLS["cap"]
      translated_string << BRAILLE_ALPHABET[char.downcase]
    elsif BRAILLE_ALPHABET.key?(char)
      translated_string << BRAILLE_ALPHABET[char]
    else
      return "Invalid Input. Please enter a valid English string."
    end
  end
  translated_string
end

# This app doesn't account for foreign languages, gibberish phrases or phrases consisting of only special characters.
# It's possible a user might want to check specific letters, or characters so strings like "<<>//..<" are considered english.
# To ensure english only input we could check against an english dictionary, or use a gem like 'lingua' to detect the language.
# This check will reject any input including a character not in the BRAILLE_ALPHABET or BRAILLE_SYMBOLS hashes.

if is_braille?(input)
puts translate_braille_to_eng(input)
else
puts translate_eng_to_braille(input)
end
