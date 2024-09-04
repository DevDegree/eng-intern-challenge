# Determine if the input string is Braille
def braille?(input_string)

  # if the string contains all 0s and .s then it is Braille
  # TO DO: Logic out if it makes sense to check all values - I think it does
  input_string.chars.all? { |c| c == 'O' || c == '.' }

end

def main

  # Join all arguments into a single string
  input_string = ARGV.join(" ")

  # Verifies that there is at least something to translate
  if input_string.empty?
    puts "Usage: ruby translator.rb <input_string>"
    return
  end

  # Check if input is braille or english
  if braille?(input_string)
    puts "Braille"
  else
    puts "English"
  end

end

# Execute main for when file is run directly
main if __FILE__ == $PROGRAM_NAME
