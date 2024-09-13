use anyhow::{bail, ensure, Result};

pub fn english_to_braille(s: &str) -> Result<String> {
    ensure!(s.is_ascii());
    let mut out = String::new();

    let n = s.len();
    let mut i = 0;
    while i < n {
        let c = s.as_bytes()[i] as char;

        if c.is_ascii_lowercase() {
            out.push_str(&lower_alpha_to_braille(c));
        } else if c.is_ascii_uppercase() {
            out.push_str(CAPITAL_FOLLOWS);
            out.push_str(&lower_alpha_to_braille(c.to_ascii_lowercase()));
        } else if c == ' ' {
            out.push_str(SPACE);
        } else if c.is_ascii_digit() {
            // Handle a group of consecutive digits all at once.
            out.push_str(NUMBER_FOLLOWS);
            while i < n && (s.as_bytes()[i] as char).is_ascii_digit() {
                out.push_str(digit_to_braille(s.as_bytes()[i] as char));
                i += 1;
            }

            // Insert a ' ' to reset the "context" from digits to letters, if
            // needed.
            if i < n && (s.as_bytes()[i] as char).is_ascii_alphabetic() {
                out.push_str(SPACE);
            }

            continue;
        } else {
            bail!("don't know how to convert {c:?} from English to Braille");
        }

        i += 1
    }

    Ok(out)
}

fn lower_alpha_to_braille(c: char) -> &'static str {
    match c {
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

        _ => panic!("not lower alpha: {c:?}"),
    }
}

/// Note that the braille characters for `1234567890` overlap with `abcdefghij`.
fn digit_to_braille(c: char) -> &'static str {
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
        _ => panic!("not a digit: {c:?}"),
    };

    lower_alpha_to_braille(alpha)
}

const CAPITAL_FOLLOWS: &str = ".....O";
const NUMBER_FOLLOWS: &str = ".O.OOO";
const SPACE: &str = "......";

#[cfg(test)]
mod tests {
    use std::iter;

    use super::*;

    /// The code for `lower_alpha_to_braille` is prone to typos, so let's
    /// double-check it here.
    #[test]
    fn test_lower_alpha_to_braille() {
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
