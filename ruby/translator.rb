ENGLISH_TO_BRAILLE_MAPPING = {
  alpha_and_punctuation: {
    'a' => 'O.....',
    'b' => 'O.O...',
    'c' => 'OO....',
    'd' => 'OO.O..',
    'e' => 'O..O..',
    'f' => 'OOO...',
    'g' => 'OOOO..',
    'h' => 'O.OO..',
    'i' => '.OO...',
    'j' => '.OOO..',
    'k' => 'O...O.',
    'l' => 'O.O.O.',
    'm' => 'OO..O.',
    'n' => 'OO.OO.',
    'o' => 'O..OO.',
    'p' => 'OOO.O.',
    'q' => 'OOOOO.',
    'r' => 'O.OOO.',
    's' => '.OO.O.',
    't' => '.OOOO.',
    'u' => 'O...OO',
    'v' => 'O.O.OO',
    'w' => '.OOO.O',
    'x' => 'OO..OO',
    'y' => 'OO.OOO',
    'z' => 'O..OOO',
    '.' => '..00.0',
    ',' => '..0...',
    '?' => '..0.00',
    '!' => '..000.',
    ':' => '..00..',
    ';' => '..0.0.',
    '-' => '....00',
    '/' => '.0..0.',
    '<' => '.00..0',
    '>' => '0..00.',
    '(' => '0.0..0',
    ')' => '.0.00.',
  },
  numeric: {
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..',
  },
  special: {
    'capital_follows' => '.....0',
    'decimal_follows' => '.0...0',
    'number_follows' => '.0.000',
    ' ' => '......',
  }
}

BRAILLE_TO_ENGLISH_MAPPING = ENGLISH_TO_BRAILLE_MAPPING.transform_values { |v| v.invert }

ENGLISH_SPACE = ' '
BRAILLE_SPACE = ENGLISH_TO_BRAILLE_MAPPING[:special][ENGLISH_SPACE]

def is_english?(str)
  str.chars.any? { |char| not ['O', '.'].include?(char) }
end

def main
  input_string = ARGV.join(" ")
end