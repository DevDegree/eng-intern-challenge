use anyhow::{bail, Result};

mod braille_to_english;
mod english_to_braille;

pub use braille_to_english::braille_to_english;
pub use english_to_braille::english_to_braille;

pub fn detect_and_translate(s: &str) -> Result<String> {
    let braille = english_to_braille(s);
    let english = braille_to_english(s);

    match (braille, english) {
        (Ok(s), Err(_)) => Ok(s),
        (Err(_), Ok(s)) => Ok(s),
        (Ok(_), Ok(_)) => bail!("ambiguous string; could be braille or english: {s:?}"),
        (Err(e1), Err(e2)) => {
            bail!("string is neither braille nor english: {s:?}\nerrors:\n{e1}\n{e2}")
        }
    }
}
