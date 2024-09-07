letters_and_symboles = {
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
  " " => "......"
}

numbers = {
  "1" => "O.....",
  "2" => "O.O...",
  "3" => "OO....",
  "4" => "OO.O..",
  "5" => "O..O..",
  "6" => "OOO...",
  "7" => "OOOO..",
  "8" => "O.OO..",
  "9" => ".OO...",
  "0" => ".OOO..",
}

input = ARGV

if input.to_s.include?("." && "O") && !input.to_s.include?(" ")
  characters = []

  def add_character_to_array_from_hash(character, array, hash)
    array << hash.key(character)
  end

  input_array = input.first.scan(/....../)

  result = input_array.map.with_index do |character, index|
    if input_array[index-1] == ".O.OOO" || (numbers.keys.include?(characters.last) && character != "......")
      add_character_to_array_from_hash(character, characters, numbers)
      numbers.key(character)
    elsif input_array[index-1] == ".....O"
      add_character_to_array_from_hash(character, characters, letters_and_symboles)
      letters_and_symboles.key(character).capitalize
    else
      add_character_to_array_from_hash(character, characters, letters_and_symboles)
      letters_and_symboles.key(character)
    end

  end

else
  input_array = input.join(' ').split('')

  result = input_array.map.with_index do |character, index|
    if numbers.keys.include?(character) && (!numbers.keys.include?(input_array[index-1]) || index == 0)
      ".O.OOO" + numbers[character].to_s
    elsif numbers.keys.include?(character) && numbers.keys.include?(input_array[index-1])
      numbers[character].to_s
    elsif character == character.capitalize && character != " "
      ".....O" + letters_and_symboles[character.downcase].to_s
    else
      letters_and_symboles[character].to_s
    end
  end

end

puts result.join
