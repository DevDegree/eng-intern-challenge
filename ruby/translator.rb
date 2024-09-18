# Precomputed English to Braille and Braille to English mappings
ENGLISH_TO_BRAILLE = {
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
    ' ' => '......',
    'CAPITAL' => '.....O',
    'NUMBER' => '.O.OOO'
  }

BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.invert

def english_to_braille(english) 
    result = ""
    in_number_mode = false

    english.each_char do |char| 
        if char.match?(/[A-Z]/)
            result += ENGLISH_TO_BRAILLE['CAPITAL']
            char = char.downcase
        end

        if char.match?(/[1-9]/)
            result += ENGLISH_TO_BRAILLE['NUMBER'] unless in_number_mode
            in_number_mode = true
            char = ('a'.ord + char.to_i - 1).chr
        else
            in_number_mode = false
        end

        result += ENGLISH_TO_BRAILLE[char] || ''
    end

    result
end

def braille_to_english(braille) 
    split_string = braille.chars.each_slice(6).map(&:join)

    split_string.map do |braille_char|
        puts BRAILLE_TO_ENGLISH[braille_char] 
    end
end

puts "Enter text to translate:"
input = gets.chomp
puts "Input: #{input}"
puts "Output: #{braille_to_english(input)}"
