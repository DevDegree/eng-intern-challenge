use std::env;

use anyhow::{Context, Result};
use itertools::Itertools;

mod translate;

fn main() -> Result<()> {
    let (_prog_name, input) = env::args()
        .collect_tuple()
        .context("expected 1 argument: the string to translate")?;

    let output = format!("TODO: translate {input}");
    println!("{}", output);

    Ok(())
}
