ENGLISH_BRAILLE_DICTIONARY = {
    'a' => 'O.....',
    'b' => 'O.O...',
    'c' => 'OO....',
    'd' => 'OO.O..',
    'e' => 'O..O..',
    'f' => 'OOO...',
    'g' => 'OOOO..',
    'h' => 'O.OO..',
    'i' => '.OO...',
    'j' => '.OOO..',
    'k' => 'O...O.',
    'l' => 'O.O.O.',
    'm' => 'OO..O.',
    'n' => 'OO.OO.',
    'o' => 'O..OO.',
    'p' => 'OOO.O.',
    'q' => 'OOOOO.',
    'r' => 'O.OOO.',
    's' => '.OO.O.',
    't' => '.OOOO.',
    'u' => 'O...OO',
    'v' => 'O.O.OO',
    'w' => '.OOO.O',
    'x' => 'OO..OO',
    'y' => 'OO.OOO',
    'z' => 'O..OOO',
    ' ' => '......'
}

VALUES_BRAILLE_DICTIONARY = {
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..'
}

CAPITAL_FOLLOWS_INDICATOR = '.....O'
DECIMAL_FOLLOWS_INDICATOR = '.O...O'
NUMBER_FOLLOWS_INDICATOR = '.O.OOO'
SPACE_INDICATOR = '......'


BRAILLE_ENGLISH_DICTIONARY = ENGLISH_BRAILLE_DICTIONARY.invert
BRAILLE_VALUES_DICTIONARY = VALUES_BRAILLE_DICTIONARY.invert



def translate(message)
    if message.match(/[O.]/)
        value_check = false
        capital_check = false
        convertedMsg = []

        message.scan(/.{6}/).each do |sample|
            if sample == SPACE_INDICATOR
                convertedMsg << ' '
                value_check = false
            elsif sample == NUMBER_FOLLOWS_INDICATOR
                value_check = true
            elsif sample == CAPITAL_FOLLOWS_INDICATOR
                capital_check = true
            else
                symbol = value_check ? BRAILLE_VALUES_DICTIONARY[sample] : BRAILLE_ENGLISH_DICTIONARY[sample]

                if capital_check
                    symbol = symbol.upcase
                    capital_check = false
                end
                convertedMsg << symbol
            end
        end

        convertedMsg.join
    else
        convertedMsg = []
        value_check = false

        message.chars.each do |character|
            if character.match(/\d/)
                convertedMsg << NUMBER_FOLLOWS_INDICATOR unless value_check
                value_check = true
                convertedMsg << VALUES_BRAILLE_DICTIONARY[character]
            elsif character == character.upcase
                value_check = false
                convertedMsg << CAPITAL_FOLLOWS_INDICATOR
                convertedMsg << ENGLISH_BRAILLE_DICTIONARY[character.downcase]

            elsif character == ' '
                value_check = false
                convertedMsg << SPACE_INDICATOR
                
            else 
                value_check = false  
                convertedMsg << ENGLISH_BRAILLE_DICTIONARY[character]
                
            end
        end

        convertedMsg.join
    end
end

puts translate(ARGV.join(' '))


