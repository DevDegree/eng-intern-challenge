=begin
The purpose of this Braille/English translator is to take in a command-line argument input and translate it from Braille to English or vice-versa.
The program can recognize the type of input (English or Braille) and convert it to 

Its use case is as follows: ruby translator.rb [input]
where input is the string of English/Braille to be translated

The translator is capable of handling alphanumeric characters and translating them to English
A quick inspection of the 
=end

#Creating a hash that stores all key/value pairs of letters and their braille representations
CHARACTER_HASH = {
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
  "z" => "O..OOO",
  "." => "..OO.O",
  "," => "..O...",
  "?" => "..O.OO",
  "!" => "..OOO.",
  ":" => "..OO..",
  ";" => "..O.O.",
  "-" => "....OO",
  "/" => ".O..O.",
  "<" => ".OO..O",
  # ">" => "O..OO.", note that the > character has been omitted since it is the same as the letter o
  "(" => "O.O..O",
  ")" => ".O.OO.",
  " " => "......"
}

#Creating a hash that stores key/value pairs of numbers and their braille representation
NUMBER_HASH = {
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

#Defining the flag for capitalization to signal to the program that the next letter will be a capital
CAPITALFOLLOWS_FLAG = ".....O"

#Defining the flag to indicate that a number follows until a space is found
NUMBERFOLLOWS_FLAG = ".O.OOO"

#Creating a space braille character to make coding visualization easier (personal preference and not needed)
SPACE_IN_BRAILLE = CHARACTER_HASH[" "]

#Function assumes that input is in English and returns a Braille string (consisting of O's and .'s')
def english_to_braille(input)

  translated_string = ""
  number_follows = false

  #Following loop converts each character into Braille depending on if it is a number or a letter
  input.chars.each do |english_char|

    #Use regex to check for numbers
    if english_char =~ /[0-9]/

      if !number_follows
        translated_string += NUMBERFOLLOWS_FLAG
        number_follows = true
      end

      translated_string += NUMBER_HASH[english_char]

    else
      if english_char == " "
        number_follows = false
      #Use regex to check for capital letters
      elsif english_char =~ /[A-Z]/
        translated_string += CAPITALFOLLOWS_FLAG
      end

      #Using begin/rescue block to make sure the character truly exists in our dictionary
      begin
        translated_string += CHARACTER_HASH[english_char.downcase]
      rescue TypeError
        puts "Certain characters in your string don't exist in the given list of valid braille and english characters"
      end
    end
  end

  return translated_string

end

#Function assumes that input is in Braille and returns an English string
def braille_to_english(input)
  translated_string = ""
  number_follows = false
  capital_follows = false

  input.scan(/.{6}/).each do |braille_char|

    #Handling each special case of a flag/space showing up
    if braille_char == CAPITALFOLLOWS_FLAG
      capital_follows = true

    elsif braille_char == NUMBERFOLLOWS_FLAG
      number_follows = true

    elsif braille_char == SPACE_IN_BRAILLE
      number_follows = false
      translated_string += " "

    #If there is no flag then convert the braille depending on our number and capital booleans
    else
      if number_follows
        translated_string += NUMBER_HASH.key(braille_char)

      elsif capital_follows
        capital_follows = false
        translated_string += CHARACTER_HASH.key(braille_char).upcase

      else
        #Using begin/rescue block to make sure the character truly exists in our dictionary
        begin
          translated_string += CHARACTER_HASH.key(braille_char)
        rescue TypeError
          puts "Certain characters in your string don't exist in the given list of valid braille and english characters"
        end

      end
    end
  end

  return translated_string

end

def translate(input)

  if input.match?(/^[.O]+$/) && input.length % 6 == 0
    return braille_to_english(input)
  else
    return english_to_braille(input)
  end

end

if __FILE__ == $0
  input = ARGV.join(" ")
  puts translate(input)
end