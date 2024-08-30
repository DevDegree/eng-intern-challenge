def determine_if_input_is_braille_or_english()
  input_string = ARGV[0]

  if input_string.include?(".")
    return "braille"
  end
  return "english"
end

