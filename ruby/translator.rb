ALPHABET = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', ' ' => '......',
}

NUMBERS = {
    '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
    '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..'
}

CAPITAL_SYMBOL = ".....O"
NUMBER_SYMBOL = ".O.OOO"
SPACE = "......"


def braille?(text)
    """
    Checks if all characters are Braille
    """
    allowed_chars = ['O', '.']
    text.chars.all? { |char| allowed_chars.include?(char) } && text.length % 6 == 0
end

# Convert English to Braille
def english_to_braille(text)
    braille = ''
    number_mode = false
    text.each_char do |char|
        if char =~ /[A-Z]/
            braille += CAPITAL_SYMBOL
            char = char.downcase
        elsif char =~ /[0-9]/
            if !number_mode 
                braille += NUMBER_SYMBOL
                number_mode = true
        end 
        elsif char === ' ' and number_mode
            number_mode = false
        end
        braille += ALPHABET[char] || NUMBERS[char] || ''
    end
    braille
end

# Convert Braille to English
def braille_to_english(text)
    result = ""
    is_number_mode = false
    capitalize_next = false
    index = 0
    text.scan(/.{6}/) do |char|
        index += 6
        if (char === CAPITAL_SYMBOL)
            capitalize_next = true
        elsif char === NUMBER_SYMBOL
            is_number_mode = true
        elsif (char === SPACE)
            is_number_mode = false
            result += ' '
        else 
            if is_number_mode
                result += NUMBERS.key(char)
            else
                result += capitalize_next ? ALPHABET.key(char).upcase : ALPHABET.key(char)
                capitalize_next = false
            end
        end
    end
  result
end

def translator
    input = ARGV.join(' ')
    if braille?(input)
      puts braille_to_english(input)
    else
      puts english_to_braille(input)
    end
end
translator