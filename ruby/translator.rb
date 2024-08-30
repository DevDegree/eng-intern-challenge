require_relative 'constants'

def determine_if_input_is_braille_or_english()
  input_string = ARGV[0]

  if input_string.nil?
    return puts "Please provide an input string"
  else
    if input_string.include?(".")
      return BRAILLE_TYPE
    else
      return ENGLISH_TYPE
    end
  end
end


def translate_braille_to_english(braille_string)
  result = ""
end

def main()
  input_type = determine_if_input_is_braille_or_english()

  if input_type == BRAILLE_TYPE
    puts "hello"
  else
    puts "world"
  end


end

main()
