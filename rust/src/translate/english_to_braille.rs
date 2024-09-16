use anyhow::{bail, ensure, Result};

use crate::translate::braille;

pub fn translate(s: &str) -> Result<String> {
    ensure!(s.is_ascii());
    let mut out = String::new();

    let n = s.len();
    let mut i = 0;
    while i < n {
        let c = s.as_bytes()[i] as char;

        if c.is_ascii_lowercase() {
            out.push_str(braille::from_lower_alpha(c).unwrap());
        } else if c.is_ascii_uppercase() {
            out.push_str(braille::CAPITAL_FOLLOWS);
            out.push_str(braille::from_lower_alpha(c.to_ascii_lowercase()).unwrap());
        } else if c == ' ' {
            out.push_str(braille::SPACE);
        } else if c.is_ascii_digit() {
            // Handle a group of consecutive digits all at once.
            out.push_str(braille::NUMBER_FOLLOWS);
            while i < n && (s.as_bytes()[i] as char).is_ascii_digit() {
                out.push_str(&braille::from_digit(s.as_bytes()[i] as char).unwrap());
                i += 1;
            }

            // Insert a ' ' to reset the "context" from digits to letters, if
            // needed.
            if i < n && s.as_bytes()[i] as char != ' ' {
                out.push_str(braille::SPACE);
            }

            continue;
        } else {
            bail!("don't know how to convert {c:?} from English to Braille");
        }

        i += 1
    }

    Ok(out)
}
