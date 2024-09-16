use anyhow::{bail, Context, Result};

pub const CAPITAL_FOLLOWS: &str = ".....O";
pub const NUMBER_FOLLOWS: &str = ".O.OOO";
pub const SPACE: &str = "......";

pub fn from_lower_alpha(c: char) -> Result<&'static str> {
    let cell = match c {
        'a' => "O.....",
        'b' => "O.O...",
        'c' => "OO....",
        'd' => "OO.O..",
        'e' => "O..O..",
        'f' => "OOO...",
        'g' => "OOOO..",
        'h' => "O.OO..",
        'i' => ".OO...",
        'j' => ".OOO..",
        'k' => "O...O.",
        'l' => "O.O.O.",
        'm' => "OO..O.",

        'n' => "OO.OO.",
        'o' => "O..OO.",
        'p' => "OOO.O.",
        'q' => "OOOOO.",
        'r' => "O.OOO.",
        's' => ".OO.O.",
        't' => ".OOOO.",
        'u' => "O...OO",
        'v' => "O.O.OO",
        'w' => ".OOO.O",
        'x' => "OO..OO",
        'y' => "OO.OOO",
        'z' => "O..OOO",

        _ => bail!("not lower alpha: {c:?}"),
    };
    Ok(cell)
}

pub fn to_lower_alpha(cell: &str) -> Result<char> {
    let alpha = match cell {
        "O....." => 'a',
        "O.O..." => 'b',
        "OO...." => 'c',
        "OO.O.." => 'd',
        "O..O.." => 'e',
        "OOO..." => 'f',
        "OOOO.." => 'g',
        "O.OO.." => 'h',
        ".OO..." => 'i',
        ".OOO.." => 'j',
        "O...O." => 'k',
        "O.O.O." => 'l',
        "OO..O." => 'm',

        "OO.OO." => 'n',
        "O..OO." => 'o',
        "OOO.O." => 'p',
        "OOOOO." => 'q',
        "O.OOO." => 'r',
        ".OO.O." => 's',
        ".OOOO." => 't',
        "O...OO" => 'u',
        "O.O.OO" => 'v',
        ".OOO.O" => 'w',
        "OO..OO" => 'x',
        "OO.OOO" => 'y',
        "O..OOO" => 'z',

        _ => bail!("not an a..=z braille cell: {cell:?}"),
    };
    Ok(alpha)
}

/// Note that the braille characters for `1234567890` overlap with `abcdefghij`.
pub fn from_digit(c: char) -> Result<&'static str> {
    let alpha = match c {
        '1' => 'a',
        '2' => 'b',
        '3' => 'c',
        '4' => 'd',
        '5' => 'e',
        '6' => 'f',
        '7' => 'g',
        '8' => 'h',
        '9' => 'i',
        '0' => 'j',
        _ => bail!("not a digit: {c:?}"),
    };
    let cell = from_lower_alpha(alpha).unwrap();
    Ok(cell)
}

/// Note that braille cells `1234567890` are the same as `abcdefghij`. So you
/// only probably only want to call this function if you know from context that
/// the cell is numeric.
pub fn to_digit(cell: &str) -> Result<char> {
    let alpha = to_lower_alpha(cell).context("digits are alpha a..=j")?;
    let digit = match alpha {
        'a' => '1',
        'b' => '2',
        'c' => '3',
        'd' => '4',
        'e' => '5',
        'f' => '6',
        'g' => '7',
        'h' => '8',
        'i' => '9',
        'j' => '0',
        _ => bail!("out of range for braille digit: {alpha:?}"),
    };
    Ok(digit)
}

#[cfg(test)]
mod tests {
    use std::iter;

    use super::*;

    /// This code is prone to typos, so let's double-check it here.
    #[test]
    fn test_from_lower_alpha() {
        let expected = &[
            b"O.  O.  OO  OO  O.  OO  OO  O.  .O  .O  O.  O.  OO",
            b"..  O.  ..  .O  .O  O.  OO  OO  O.  OO  ..  O.  ..",
            b"..  ..  ..  ..  ..  ..  ..  ..  ..  ..  O.  O.  O.",
            b"                                                  ",
            b"OO  O.  OO  OO  O.  .O  .O  O.  O.  .O  OO  OO  O.",
            b".O  .O  O.  OO  OO  O.  OO  ..  O.  OO  ..  .O  .O",
            b"O.  O.  O.  O.  O.  O.  O.  OO  OO  .O  OO  OO  OO",
        ];

        // "Pretty-print" the braille patterns for `a..=z`.
        let mut out = vec![vec![b' '; expected[0].len()]; expected.len()];

        for (i, chars) in ['a'..='m', 'n'..='z'].into_iter().enumerate() {
            for (j, c) in chars.enumerate() {
                let braille = lower_alpha_to_braille(c).unwrap();
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
