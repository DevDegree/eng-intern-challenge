fn upper_alpha_to_braille(c: char) -> &'static str {
    match c {
        'A' => ".OOOOO",
        'B' => ".O.OOO",
        'C' => "..OOOO",
        'D' => "..O.OO",
        'E' => ".OO.OO",
        'F' => "...OOO",
        'G' => "....OO",
        'H' => ".O..OO",
        'I' => "O..OOO",
        'J' => "O...OO",
        'K' => ".OOO.O",
        'L' => ".O.O.O",
        'M' => "..OO.O",

        'N' => "..O..O",
        'O' => ".OO..O",
        'P' => "...O.O",
        'Q' => ".....O",
        'R' => ".O...O",
        'S' => "O..O.O",
        'T' => "O....O",
        'U' => ".OOO..",
        'V' => ".O.O..",
        'W' => "O...O.",
        'X' => "..OO..",
        'Y' => "..O...",
        'Z' => ".OO...",

        _ => panic!("not upper alpha: {c:?}"),
    }
}

#[cfg(test)]
mod tests {
    use std::iter;

    use super::*;

    /// The code for `upper_alpha_to_braille` is prone to typos, so let's
    /// double-check it here.
    #[test]
    fn test_upper_alpha_to_braille() {
        let expected = &[
            b".O  .O  ..  ..  .O  ..  ..  .O  O.  O.  .O  .O  ..",
            b"OO  .O  OO  O.  O.  .O  ..  ..  .O  ..  OO  .O  OO",
            b"OO  OO  OO  OO  OO  OO  OO  OO  OO  OO  .O  .O  .O",
            b"                                                  ",
            b"..  .O  ..  ..  .O  O.  O.  .O  .O  O.  ..  ..  .O",
            b"O.  O.  .O  ..  ..  .O  ..  OO  .O  ..  OO  O.  O.",
            b".O  .O  .O  .O  .O  .O  .O  ..  ..  O.  ..  ..  ..",
        ];

        // "Pretty-print" the braille patterns for `A..=Z`.
        let mut out = vec![vec![b' '; expected[0].len()]; expected.len()];

        for (i, chars) in ['A'..='M', 'N'..='Z'].into_iter().enumerate() {
            for (j, c) in chars.enumerate() {
                let braille = upper_alpha_to_braille(c);
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
