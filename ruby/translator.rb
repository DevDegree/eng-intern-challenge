# Callum Brezden
# 29/24/2024
# Shopify Winter 2025 Internship Application

# Notes
# Black dot is represented by '0' and empty dot is represented by '.'

BRAILLE_TO_ENGLISH = {
  'O.....' => 'a', 'O.O...' => 'b',
  'OO....' => 'c', 'OO.O..' => 'd',
  'O..O..' => 'e', 'OOO...' => 'f',
  'OOOO..' => 'g', 'O.OO..' => 'h',
  '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l',
  'OO..O.' => 'm', 'OO.OO.' => 'n',
  'O..OO.' => 'o', 'OOO.O.' => 'p',
  'OOOOO.' => 'q', 'O.OOO.' => 'r',
  '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v',
  '.OOO.O' => 'w', 'OO..OO' => 'x',
  'OO.OOO' => 'y', 'O..OOO' => 'z',

  '.....0' => 'capital_follows',
  '.0.000' => 'number_follows',
  '......' => ' '
}

ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert

NUMBERS = {
  'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
  'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
}

def language_detector(input)
  is_braille = input.match?(/^[O.]+$/)
  is_braille ? braille_to_english(input) : english_to_braille(input)
end
