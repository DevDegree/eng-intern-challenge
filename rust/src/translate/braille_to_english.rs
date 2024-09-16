use anyhow::{bail, ensure, Context, Result};

use super::braille;

pub fn translate(s: &str) -> Result<String> {
    let mut out = String::new();
    let mut cells = cells(s)?.into_iter().peekable();

    while let Some(cell) = cells.next() {
        if cell == braille::SPACE {
            out.push(' ');
        } else if let Ok(alpha) = braille::to_lower_alpha(cell) {
            out.push(alpha);
        } else if cell == braille::CAPITAL_FOLLOWS {
            let next = cells
                .next()
                .context("\"capital follows\" at end of string")?;
            let alpha = braille::to_lower_alpha(next).context("non-alpha after capital follows")?;
            out.push(alpha.to_ascii_uppercase());
        } else if cell == braille::NUMBER_FOLLOWS {
            ensure!(
                cells.peek().is_some(),
                "\"number follows\" at end of string"
            );
            while let Some(next) = cells.peek() {
                if let Ok(digit) = braille::to_digit(next) {
                    cells.next(); // Consume the cell.
                    out.push(digit);
                }
            }
            if let Some(&next) = cells.peek() {
                ensure!(
                    next == braille::SPACE,
                    "number must be terminated by space or end-of-string, got: {next:?}"
                );
            }
        } else {
            bail!("unrecognized braille cell: {cell:?}");
        }
    }

    Ok(out)
}

const DOTS_PER_CELL: usize = 6;

fn cells(s: &str) -> Result<Vec<&str>> {
    let n = s.len();
    ensure!(
        n % DOTS_PER_CELL == 0,
        "length must be a multiple of {DOTS_PER_CELL}, got: {n:?}"
    );

    let mut out = vec![];

    let mut i = 0;
    while i < n {
        let cell = &s[i..][..DOTS_PER_CELL];
        out.push(cell);

        i += DOTS_PER_CELL;
    }

    Ok(out)
}
