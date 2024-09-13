fn lower_alpha_to_braille(c: char) -> &'static str {
    match c {
        'a' => ".OOOOO",
        'b' => ".O.OOO",
        'c' => "..OOOO",
        'd' => "..O.OO",
        'e' => ".OO.OO",
        'f' => "...OOO",
        'g' => "....OO",
        'h' => ".O..OO",
        'i' => "O..OOO",
        'j' => "O...OO",
        'k' => ".OOO.O",
        'l' => ".O.O.O",
        'm' => "..OO.O",

        'n' => "..O..O",
        'o' => ".OO..O",
        'p' => "...O.O",
        'q' => ".....O",
        'r' => ".O...O",
        's' => "O..O.O",
        't' => "O....O",
        'u' => ".OOO..",
        'v' => ".O.O..",
        'w' => "O...O.",
        'x' => "..OO..",
        'y' => "..O...",
        'z' => ".OO...",

        _ => panic!("not lower alpha: {c:?}"),
    }
}

const CAPITAL_FOLLOWS: &str = "OOOOO.";
const NUMBER_FOLLOWS: &str = "O.O...";
const SPACE: &str = "OOOOOO";

#[cfg(test)]
mod tests {
    use std::iter;

    use super::*;

    /// The code for `lower_alpha_to_braille` is prone to typos, so let's
    /// double-check it here.
    #[test]
    fn test_lower_alpha_to_braille() {
        let expected = &[
            b".O  .O  ..  ..  .O  ..  ..  .O  O.  O.  .O  .O  ..",
            b"OO  .O  OO  O.  O.  .O  ..  ..  .O  ..  OO  .O  OO",
            b"OO  OO  OO  OO  OO  OO  OO  OO  OO  OO  .O  .O  .O",
            b"                                                  ",
            b"..  .O  ..  ..  .O  O.  O.  .O  .O  O.  ..  ..  .O",
            b"O.  O.  .O  ..  ..  .O  ..  OO  .O  ..  OO  O.  O.",
            b".O  .O  .O  .O  .O  .O  .O  ..  ..  O.  ..  ..  ..",
        ];

        // "Pretty-print" the braille patterns for `a..=z`.
        let mut out = vec![vec![b' '; expected[0].len()]; expected.len()];

        for (i, chars) in ['a'..='m', 'n'..='z'].into_iter().enumerate() {
            for (j, c) in chars.enumerate() {
                let braille = lower_alpha_to_braille(c);
                assert_eq!(braille.len(), 6);

                let offsets = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)];
                for ((row, col), dot) in iter::zip(offsets, braille.chars()) {
                    out[i * 4 + row][j * 4 + col] = dot.try_into().unwrap();
                }
            }
        }

        // In case the test fails, show us what we got wrong.
        for i in 0..out.len() {
            for j in 0..out[i].len() {
                print!("{}", out[i][j] as char);
            }
            println!();
        }

        assert_eq!(out, expected);
    }
}
