Brailie_Mapping = {'a' => 'O.....',  'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', ' ' => '......',
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
  '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..',
  '.' => '..OO.O', ',' => '..O...', '?' => '..O.OO', '!' => '..OOO.', '-' => '....OO',
  ';' => '..O.O.', ':' => '..OO..', '(' => 'O.O..O', '<' => '.OO..O', '>' => 'O..OO.',
  ')' => '.O.OO.', '/' => '.O..O.'
}
Capital_Prefix = '.....O'
Number_Prefix = '.O.OOO'

def brailie_to_english(brailie)
    result = ''
    number_mode = false
    capitalize_next = false
    validate_brailie_input(brailie)
    brailie.tr('^O.', '').scan(/.{6}/).each do |symbol|
        if symbol == Capital_Prefix
            capitalize_next = true
        elsif symbol = Number_Prefix
            number_mode = true
        else
            char = Brailie_Mapping.key(symbol)
            if char
                if number_mode && ('a'..'j').include?(char)
                    num = (char.ord - 'a'.ord + 1) % 10
                    result = result + num.to_s
                elsif capitalize_next
                    result = result + char.upcase
                    capitalize_next = false
                else
                    result  = result + char
                end
                number_mode = false if !('a..j').include?(char)
            else
                result = result + '?'
            end
        end
    end
    result
end