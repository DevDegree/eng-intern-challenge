LETTERS_BRAILLE = {
  "O....." => 'a',
  "O.O..." => 'b',
  "OO...." => 'c',
  "OO.O.." => 'd',
  "O..O.." => 'e',
  "OOO..." => 'f',
  "OOOO.." => 'g',
  "O.OO.." => 'h',
  ".OO..." => 'i',
  ".OOO.." => 'j',
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
}

NUMBERS_BRAILLE = {
  "O....." => '1',
  "O.O..." => '2',
  "OO...." => '3',
  "OO.O.." => '4',
  "O..O.." => '5',
  "OOO..." => '6',
  "OOOO.." => '7',
  "O.OO.." => '8',
  ".OO..." => '9',
  ".OOO.." => '0',
}

SPECIAL_BRAILLE = {
  "..O..." => ',',
  "..O.O." => ';',
  "..OO.." => ':',
  "..OO.O" => '.',
  "..O.OO" => '?',
  "..OOO." => '!',
  "...OO" => '-',
  ".O..O." => '/',
  ".OO..O" => '<',
  "O..OO." => '>',
  "O.O..O" => '(',
  ".O.OO." => ')',
  "......" => ' ',

}

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

def braille_to_english(string)
    capital = false
    decimal = false
    number = false
    braille_array = string.scan(/.{6}/)
    
    braille_array.each do |character|
        if character == SPACE
            print " "
            number = false
        elsif character == CAPITAL_FOLLOWS
            capital = true
            next
        elsif character == DECIMAL_FOLLOWS
            decimal = true
            next
        elsif character == NUMBER_FOLLOWS
            number = true
            next
        elsif number == true
            print NUMBERS_BRAILLE[character]
        elsif decimal == true
            print "."
            decimal = false
        elsif LETTERS_BRAILLE.key?(character)
            if capital == true
                print LETTERS_BRAILLE[character].upcase
                capital = false
            else
                print LETTERS_BRAILLE[character]
            end
        elsif SPECIAL_BRAILLE.key?(character)
            print SPECIAL_BRAILLE[character]
        else
            print "error"
        end
    end
end

def english_to_braille(string)

    letters_braille = LETTERS_BRAILLE.invert
    numbers_braille = NUMBERS_BRAILLE.invert
    special_braille = SPECIAL_BRAILLE.invert

    number = false

    string.each_char do |character|
    
        if character =~ /[A-Z]/
            print CAPITAL_FOLLOWS
            print letters_braille[character.downcase]
        elsif character =~ /[a-z]/
            print letters_braille[character]
        elsif character =~ /[0-9]/
            if number == false
                print NUMBER_FOLLOWS
                number = true
                print numbers_braille[character]
            else
                print numbers_braille[character]
            end
        elsif character == "."
            print DECIMAL_FOLLOWS
            print special_braille[character]
        elsif character == " "
            print SPACE
            number = false
        elsif special_braille.key?(character)
            print special_braille[character]
        end
            
    end
end

string = ARGV.join(" ")

if string =~ /\A[.O]+\z/
    braille_to_english(string)
else
    english_to_braille(string)
end
