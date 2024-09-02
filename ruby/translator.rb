# I'm mapping the characters to their brailie representation
Brailie_Mapping = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
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
#Indication them outside for syntactical sugar 
Capital_Prefix = '.....O' # Indicates that next character is capitalized
Number_Prefix = '.O.OOO' # It will indicate the start of a number sequence

def brailie_to_english(brailie)
    result = ''
    number_mode = false # It will track if we are in a number sequence
    capitalize_next = false # It will track if next character shoule be capitalized
    #validate_brailie_input(brailie)

    # It will process each 6- character brailie symbol
    brailie.tr('^O.', '').scan(/.{6}/).each do |symbol|
        if symbol == Capital_Prefix
            capitalize_next = true
        elsif symbol == Number_Prefix
            number_mode = true
        else
            char = Brailie_Mapping.key(symbol)
            if char
                if number_mode && ('a'..'j').include?(char)
                    # this will convert letter a-j to numbers 1-0 in number mode
                    num = (char.ord - 'a'.ord + 1) % 10
                    result = result + num.to_s
                elsif capitalize_next
                    result = result + char.upcase
                    capitalize_next = false
                else
                    result  = result + char
                end
                # Now we will exit number mode if the character isn't a-j
                number_mode = false if !('a'..'j').include?(char)
            else
                # using '?' for unknown brailie symbols
                result = result + '?'
            end
        end
    end
    result
end

def english_to_brailie(text)
    result = ''
    number_mode = false
    text.each_char do |char|
        if char.match?(/[A-Z]/)
            # Adding capital prefix for uppercase
            result = result + Capital_Prefix + (Brailie_Mapping[char.downcase] || Brailie_Mapping[' '])
            number_mode = false
        elsif char.match?(/[0-9]/)
            #adding number prefix before the first digit in a sequende
            unless number_mode
                result = result + Number_Prefix
                number_mode = true
            end
            result = result + Brailie_Mapping[char]
        else
            result = result + Brailie_Mapping[char.downcase] || Brailie_Mapping[' ']
            number_mode  = false
        end
    end
    result 
end

# Here we check if CLI arguments are provided
if ARGV.empty?
    puts "Please provide some input"
    exit
end

#Joining all the CLI arguments int a single string
input = ARGV.join(" ")
begin   
    # We are determining if the input is brailie ('O', '.', and spaces)
    if input.match?(/^[O.\s]+$/)
        output = brailie_to_english(input)
    else
        output = english_to_brailie(input)
    end
    puts output
rescue => e
    #Erros that occur during processing are catched and reported
    puts "Error: #{e.message}"
    exit 1
end