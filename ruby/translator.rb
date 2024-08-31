# # make the hashmap to be used for the translation
# # Since there is just a fixed amount of characters, hardcoding the hashmap is fine as it will take constant time to access the value of a key

# letters = {
#     'a' => 'O.....',
#     'b' => 'O.O...',
#     'c' => 'OO....',
#     'd' => 'OO.O..',
#     'e' => 'O..O..',
#     'f' => 'OOO...',
#     'g' => 'OOOO..',
#     'h' => 'O.OO..',
#     'i' => '.OO...',
#     'j' => '.OOO..',
#     'k' => 'O...O.',
#     'l' => 'O.O.O.',
#     'm' => 'OO..O.',
#     'n' => 'OO.OO.',
#     'o' => 'O..OO.',
#     'p' => 'OOO.O.',
#     'q' => 'OOOOO.',
#     'r' => 'O.OOO.',
#     's' => '.OO.O.',
#     't' => '.OOOO.',
#     'u' => 'O...OO',
#     'v' => 'O.O.OO',
#     'w' => '.OOO.O',
#     'x' => 'OO..OO',
#     'y' => 'OO.OOO',
#     'z' => 'O..OOO',
#     'capital'   => '.....O',
#     'number'    => '.O.OOO',
#     'space' => '......',
# }

# non_letters = {
#     '.' => '..OO.O',
#     ',' => '..O...',
#     '?' => '..O.OO',
#     '!' => '..OOO.',
#     ':' => '..OO..',
#     ';' => '..O.O.',
#     '-' => '....OO',
#     '/' => '.O..O.',
#     '<' => '.OO..O',
#     '>' => 'O..OO.',
#     '(' => 'O.O..O',
#     ')' => '.O.OO.',
# }

# numbers = {
#     '1' => 'O.....',
#     '2' => 'O.O...',
#     '3' => 'OO....',
#     '4' => 'OO.O..',
#     '5' => 'O..O..',
#     '6' => 'OOO...',
#     '7' => 'OOOO..',
#     '8' => 'O.OO..',
#     '9' => '.OO...',
#     '0' => '.OOO..',
# }

# def translate_english_to_braille(word)
#     # iterate through the word
#     # check and see if the current char is uppercase, and add the uppercase braille when needed
#     # check for numbers followed by spaces

#     result = ""
#     flag_digit = false

#     word.each_char do |char|
#         puts char
#         # in case the char is a capital letter
#         if char.match?(/[A-Z]/)
#             result += letters['capital']
#             result += letters[char.downcase]
#         end

#         if char.match?(/[0-9]/)
#             # in case the char is a number
#             if !flag_digit
#                 result += letters['number']
#                 flag_digit = true
#             end

#             result += numbers[char]
#         end

#         # in case the char is a letter
#         if char.match?(/[a-z]/)
#             result += letters[char.downcase]
#         end

#         # in case the char is a non-letter
#         if char.match?(/[.,?!:;\/<>()\-]/)
#             result += non_letters[char]
#         end

#         # in case the char is a space
#         if char == ' '
#             result += letters['space']
#             flag_digit = false
#         end
#     end

#     return result

# end


# def main
#     # take the input, assuming the full input needs to be translated

#     if ARGV.empty?
#         puts 'Usage: ruby translator.rb <english or braille to be translated>'
#         return
#     end

#     word = ARGV.join(' ')

#     if word.chars.all? { |char| ['.', 'O'].include?(char) }
#         puts translate_braille_to_english(word)
#     else 
#         puts translate_english_to_braille(word)
#     end

# end

# main


$letters = {
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
    'capital'   => '.....O',
    'number'    => '.O.OOO',
    'space' => '......',
    '.' => '..OO.O',
    ',' => '..O...',
    '?' => '..O.OO',
    '!' => '..OOO.',
    ':' => '..OO..',
    ';' => '..O.O.',
    '-' => '....OO',
    '/' => '.O..O.',
    '<' => '.OO..O',
    '>' => 'O..OO.',
    '(' => 'O.O..O',
    ')' => '.O.OO.',
}

$numbers = {
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..',
}

$braille_letters = $letters.invert
$braille_numbers = $numbers.invert

def translate_english_to_braille(word)
    result = ""
    flag_digit = false

    word.each_char do |char|
        # Check for capital letters
        if char.match?(/[A-Z]/)
            result += $letters['capital']
            result += $letters[char.downcase]
        
        # Check for digits
        elsif char.match?(/[0-9]/)
            if !flag_digit
                result += $letters['number']
                flag_digit = true
            end
            result += $numbers[char]
        
        # Check for lowercase letters
        elsif char.match?(/[a-z]/)
            result += $letters[char.downcase]
        
        # Check for non-letters
        elsif char.match?(/[.,?!:;\/<>()\-]/)
            result += $letters[char]
        
        # Check for spaces
        elsif char == ' '
            result += $letters['space']
            flag_digit = false
        end
    end

    return result
end


def main
    # check if the input is empty
    if ARGV.empty?
        puts 'Usage: ruby translator.rb <english or braille to be translated>'
        return
    end

    word = ARGV.join(' ')

    # check if the input is braille or english and print the translation
    if word.chars.all? { |char| ['.', 'O'].include?(char) }
        puts translate_braille_to_english(word)
    else 
        puts translate_english_to_braille(word)
    end
end

main
