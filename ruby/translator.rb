class BrailleTranslator
  # Dictionary for Braille translations
  BRAILLE_DICTIONARY = {
    alphabets: {
      "a" => "O.....", "b" => "O.O...", "c" => "OO....",
      "d" => "OO.O..", "e" => "O..O..", "f" => "OOO...",
      "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...",
      "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
      "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
      "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.",
      "s" => ".OO.O.", "t" => ".OOOO.", "u" => "O...OO",
      "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
      "y" => "OO.OOO", "z" => "O..OOO"
    },
    numbers: {
      "1" => "O.....", "2" => "O.O...", "3" => "OO....",
      "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...",
      "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...",
      "0" => ".OOO.."
    },
    indicators: {
      capital: ".....O", number: ".O.OOO",
      decimal: ".O...O", space: "......"
    },
    special_chars: {
      "." => "..OO.O", "," => "..O...", "?" => "..O.OO",
      "!" => "..OOO.", ":" => "..OO..", ";" => "..O.O.",
      "-" => "....OO", "/" => ".O..O.", "<" => ".OO..O",
      ">" => "O..OO.", "(" => "O.O..O", ")" => ".O.OO."
    }
  }.freeze

  class << self
    # Check input if it is Braille
    def braille?(input)
      input.length >= 6 && input.chars.all? { |char| ['O', '.'].include?(char) }
    end

    # Translates from Braille to English
    def braille_to_english(input)
      braille_chars = input.scan(/.{1,6}/) # Splits Braille into chunks of 6
      result = ''
      is_number = false
      is_capital = false

      braille_chars.each do |braille_char|
        # checks indicators first since following characters could depend on them
        if braille_char == BRAILLE_DICTIONARY[:indicators][:capital]
          is_capital = true
        elsif braille_char == BRAILLE_DICTIONARY[:indicators][:number]
          is_number = true
        elsif braille_char == BRAILLE_DICTIONARY[:indicators][:decimal]
          result += '.'
        elsif braille_char == BRAILLE_DICTIONARY[:indicators][:space]
          result += ' '
          is_number = false
          is_capital = false
        else
          if is_number
            num = BRAILLE_DICTIONARY[:numbers].key(braille_char)
            result += num if num
          else
            alphabet = BRAILLE_DICTIONARY[:alphabets].key(braille_char)
            if alphabet
              result += is_capital ? alphabet.upcase : alphabet
            else
              special_char = BRAILLE_DICTIONARY[:special_chars].key(braille_char)
              result += special_char if special_char
            end
            is_capital = false
          end
        end
      end

      result
    end

    # Translates input from English to Braille
    def english_to_braille(input)
      result = ''
      is_number = false

      input.each_char do |char|
        if ('A'..'Z').include?(char)
          # Capital letters always include the capital indicator
          result += BRAILLE_DICTIONARY[:indicators][:capital] + BRAILLE_DICTIONARY[:alphabets][char.downcase]
          is_number = false
        elsif ('a'..'z').include?(char)
          result += BRAILLE_DICTIONARY[:alphabets][char]
          is_number = false
        elsif ('0'..'9').include?(char)
          # if is_number, don't repeat the number indicator
          result += BRAILLE_DICTIONARY[:indicators][:number] unless is_number
          result += BRAILLE_DICTIONARY[:numbers][char]
          is_number = true
        elsif char == ' '
          result += BRAILLE_DICTIONARY[:indicators][:space]
          is_number = false # on space reset is_number
        elsif char == '.'
          # checks for context if is_number is true, if so, add decimal indicator, else add period
          result += is_number ? BRAILLE_DICTIONARY[:indicators][:decimal] : BRAILLE_DICTIONARY[:special_chars][char]
        elsif BRAILLE_DICTIONARY[:special_chars][char]
          result += BRAILLE_DICTIONARY[:special_chars][char]
          is_number = false
        end
      end

      result
    end

    # Translates input from English to Braille or vice versa
    def translate(input)
      if braille?(input)
        braille_to_english(input)
      else
        english_to_braille(input)
      end
    end
  end
end

# Input from command line arguments
input = ARGV.join(' ')

# Output the translation
puts BrailleTranslator.translate(input)
