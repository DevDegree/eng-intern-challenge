require_relative 'constants'

def get_input_type()
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
