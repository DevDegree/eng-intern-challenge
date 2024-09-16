use std::env;

use anyhow::Result;
use itertools::Itertools;

mod translate;

fn main() -> Result<()> {
    let input = env::args().skip(1).join(" ");
    let output = translate::detect_and_translate(&input)?;
    println!("{}", output);
    Ok(())
}
