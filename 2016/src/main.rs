use std::collections::HashMap;
use std::error::Error;
use std::fs::File;
use std::io::{self, BufReader};
use std::io::prelude::*;
use std::time::Instant;

pub mod days;

type DayRunner = Box<dyn Fn(Vec<String>) -> Result<(), Box<dyn Error>>>;

fn main() -> Result<(), Box<dyn Error>> {
    let funcs: HashMap<&str, DayRunner> = HashMap::from([
        ("1", Box::new(days::day01::day01) as DayRunner),
        ("2", Box::new(days::day02::day02) as DayRunner),
        ("3", Box::new(days::day03::day03) as DayRunner),
        ("4", Box::new(days::day04::day04) as DayRunner),
        ("5", Box::new(days::day05::day05) as DayRunner),
        ("6", Box::new(days::day06::day06) as DayRunner),
        ("7", Box::new(days::day07::day07) as DayRunner),
        ("8", Box::new(days::day08::day08) as DayRunner),
    ]);

    let mut args = std::env::args().skip(1);
    let day = match args.next() {
        Some(d) => d,
        None => return Err("Usage: aoc-2016 <day> [<inputfile>]".into())
    };

    let func = match funcs.get(day.as_str()) {
        Some(f) => f,
        None => return Err(format!("Day {} is not supported", day).into())
    };

    let filename = match args.next() {
        Some(filename) => filename,
        None => format!("data/day{:0>2}.txt", day)
    };

    let file = File::open(filename)?;
    let lines = BufReader::new(file).lines().collect::<io::Result<Vec<String>>>()?;

    let time = Instant::now();
    func(lines)?;
    eprintln!("time: {}us", time.elapsed().as_micros());

    Ok(())
}
