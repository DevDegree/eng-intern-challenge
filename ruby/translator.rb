# take the input string from the command line
input_str = ARGV.join(' ')

# instantiate braille and english conversion maps
braille_map = {
    "O....." => 'a',
    "O.O..." => 'b',
    "OO...." => 'c',
    "OO.O.." => 'd',
    "O..O.." => 'e',
    "OOO..." => 'f',
    "OOOO.." => 'g',
    "O.OO.." => 'h',
    ".OO..." => "i",
    ".OOO.." => "j",
    "O...O." => 'k',
    "O.O.O." => 'l',
    "OO..O." => 'm',
    "OO.OO." => 'n',
    "O..OO." => 'o',
    "OOO.O." => 'p',
    "OOOOO." => 'q',
    "O.OOO." => 'r',
    ".OO.O." => 's',
    ".OOOO." => 't',
    "O...OO" => 'u',
    "O.O.OO" => 'v',
    ".OOO.O" => 'w',
    "OO..OO" => 'x',
    "OO.OOO" => 'y',
    "O..OOO" => 'z',
    "......" => ' ',
    ".....O" => "cap",
    ".O...O" => "dec",
    ".O.OOO" => "num"
}
english_map = {}

# instantiate english map from braille map by reversing order of keys and values
braille_map.each do |key, value|
    english_map[value] = key
end

translated_string = ""

# determine if the input is in English or Braille
count_O = input_str.count('O');
count_periods = input_str.count('.');

if (count_O + count_periods == input_str.length)  # input is in braille
    index = 0

    num_mode = false
    capital_mode = false

    # iterate through braille in 6 character chunks
    while index < input_str.length
        braille_char = input_str[index..(index + 5)]
        mapped_char = braille_map[braille_char]

        case mapped_char
        when "cap"
            capital_mode = true
        when "num"
            num_mode = true
        when ' '
            translated_string += ' '
            num_mode = false
        else
            if num_mode  # print a number if the translator is in number mode
                if mapped_char.ord == 106  # edge case for 'j --> 0'
                    translated_string += '0'
                else
                    translated_string += (mapped_char.ord - 48).chr
                end
            else  # print a character
                translated_string += (capital_mode ? mapped_char.upcase : mapped_char)

                capital_mode = false  # set capital mode to false after every character
            end
        end
        
        index += 6
    end
else  # input is in English
    num_mode = false

    input_str.each_char do |char|
        ascii_code = char.ord

        if ascii_code >= 65 && ascii_code <= 90  # capital character
            translated_string += english_map["cap"]
            translated_string += english_map[char.downcase].upcase
        elsif ascii_code >= 48 && ascii_code <= 57  # numerical digit (0-9)
            # add braille 'number follows' code if not yet added
            if !num_mode
                translated_string += english_map["num"]
                num_mode = true
            end

            # edge case for 0
            if char == '0'
                translated_string += '.000..'
            else
                translated_string += english_map[(ascii_code + 48).chr]
            end
        else  # lowercase character
            translated_string += english_map[char]
        end
    end
end

puts translated_string
