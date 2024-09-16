use anyhow::{bail, Result};

mod braille;
mod braille_to_english;
mod english_to_braille;

pub fn detect_and_translate(s: &str) -> Result<String> {
    let braille = english_to_braille::translate(s);
    let english = braille_to_english::translate(s);

    match (braille, english) {
        (Ok(s), Err(_)) => Ok(s),
        (Err(_), Ok(s)) => Ok(s),
        (Ok(_), Ok(_)) => bail!("could be braille or english: {s:?}"),
        (Err(e1), Err(e2)) => {
            bail!("neither braille nor english: {s:?}\nerrors:\n{e1}\n{e2}")
        }
    }
}
