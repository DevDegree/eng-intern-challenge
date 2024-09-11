# Braille - Alphabet Translator

# Creating the translator function
# The program will run in the command line as such: ruby translator.rb Abc 123 xYz
# Therefore, the translator function will need to be the main function that will be called and take in 1 argument.
# Note: the argument can be alphanumeric to braille or braille to alphanumeric (including special characters).

def translator(input)

  # Creating a mapping between letters and their corresponding braille representation
  # Note: Using lowercase letters because a special character will be used to indicate capitalization
  # Note 2: 3x2 matrix for each letter
  letters_mapping = {
    "a" => "O.....",
    "b" => "O.O...",
    "c" => "OO....",
    "d" => "OO.O..",
    "e" => "O..O..",
    "f" => "OOO...",
    "g" => "OOOO..",
    "h" => "O.OO..",
    "i" => ".OO...",
    "j" => ".OOO..",
    "k" => "O...O.",
    "l" => "O.O.O.",
    "m" => "OO..O.",
    "n" => "OO.OO.",
    "o" => "O..OO.",
    "p" => "OOO.O.",
    "q" => "OOOOO.",
    "r" => "O.OOO.",
    "s" => ".OO.O.",
    "t" => ".OOOO.",
    "u" => "O...OO",
    "v" => "O.O.OO",
    "w" => ".OOO.O",
    "x" => "OO..OO",
    "y" => "OO.OOO",
    "z" => "O..OOO"
  }

  # Creating a mapping between numbers and their corresponding braille representation
  numbers_mapping = {
    "1" => "O.....",
    "2" => "O.O...",
    "3" => "OO....",
    "4" => "OO.O..",
    "5" => "O..O..",
    "6" => "OOO...",
    "7" => "OOOO..",
    "8" => "O.OO..",
    "9" => ".OO...",
    "0" => ".OOO.."
  }

  # Defining a variable to tell the program that the next letter should be capitalized
  # Note: only the next symbol will be capitalized
  capital_follows = ".....O"

  # Defining a variable to tell the program that the next symbol should be a number
  # Note: all the symbols after this will be numbers until the next space symbol
  number_follows = ".O.OOO"

  # Defining a mapping between special characters and their corresponding braille representation
  special_characters_mapping = {
    "." => "..OO.O",
    "," => "..O...",
    "?" => "..O.OO",
    "!" => "..OOO.",
    ":" => "..OO..",
    ";" => "..O.O.",
    "-" => "....OO",
    "/" => ".O..O.",
    "<" => ".OO..O",
    "(" => "O.O..O",
    ")" => ".O.OO.",
    " " => "......"
  }

  # Defining boolean variables to keep track of the state of the program
  capitalization = false
  number = false
  result = ""

  # Check if the input is in Braille format (look through regex)
  # If it is in Braille format, convert it to alphanumeric
  if input.match(/^[O.]+$/) && input.length % 6 == 0

    # We need to slice the input string into 6 character chunks (3x2 matrix)
    # 6 characters of braille will be converted to 1 character of alphanumeric (or special character)
    input.scan(/.{6}/).each do |braille|
      # Check if the braille character is a capitalization flag
      if braille == capital_follows
        capitalization = true
        next
      end

      # Check if the braille character is a number flag
      if braille == number_follows
        number = true
        next
      end

      # Check if the braille character is a special character
      if special_characters_mapping.key(braille)
        # Check if the special character is a space
        # If it is a space, reset the number flag and add a space to the result
        if special_characters_mapping.key(braille) == " "
          number = false
          result += " "
          next
        end

        # otherwise, add the special character to the result
        # Note: special characters will be added to the result as is
        result += special_characters_mapping.key(braille)
      end

      # Check if the braille character is a number
      # If it is a number, the next symbols will be numbers until a space is found
      if number
        result += numbers_mapping.key(braille)
        next
      end

      # Check if the braille character is a capital letter
      # If it is a capital letter, the next letter will be capitalized and the flag will be reset
      if capitalization
        result += letters_mapping.key(braille).upcase
        capitalization = false
        next
      end

      # If the braille character is not a special character, number, or capital letter, it is a lowercase letter
      result += letters_mapping.key(braille)
    end
  else
    # If the input is not in Braille format, convert it to Braille
    # We need to iterate through each character of the input string
    # Each character will be converted to its corresponding braille representation (1 char -> 6 chars)
    input.chars.each do |char|

      # Check if the character is a capital letter
      if char.match(/[A-Z]/)
        result += capital_follows
        result += letters_mapping[char.downcase]
        next
      end

      # Check if the character is a number
      if char.match(/[0-9]/)
        if !number
          result += number_follows
          number = true
        end
        result += numbers_mapping[char]
        next
      end

      # Check if the character is a special character
      if special_characters_mapping[char]
        # Check if the special character is a space
        # If it is a space, reset the number flag and add a space to the result
        if char == " "
          number = false
          result += special_characters_mapping[char]
          next
        end
        result += special_characters_mapping[char]
        next
      end

      # If the character is not a special character, number, or capital letter, it is a lowercase letter
      result += letters_mapping[char]
    end
  end

  # Return the result
  result
end

# Ensuring that the translator function is called when the file is run
# Note: We need to join all of the arguments into 1 arg / string
if __FILE__ == $0
  input = ARGV.join(" ")
  puts translator(input)
end