if ARGV.empty?
  puts 'No arguments given'
  exit 1
end

def english?(string)
  string.match?(/\A[a-zA-Z0-9 ]+/)
end

def braille?(string)
  string.match?(/\A[.0]+/)
end

if english?(ARGV.join(' '))
  require_relative 'english_to_braille'
  puts EnglishToBraille.new.translate(ARGV.join(' '))
elsif braille?(ARGV.join(' '))
  require_relative 'braille_to_english'
  puts BrailleToEnglish.new.translate(ARGV.join(' '))
else
  puts 'Invalid input'
  exit 1
end
