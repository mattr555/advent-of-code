use std::error::Error;
use std::str::FromStr;

pub fn day03(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let input = lines
        .iter()
        .map(|l| l.trim().split_whitespace().map(|x| i64::from_str(x).unwrap()).collect::<Vec<i64>>())
        .collect::<Vec<Vec<i64>>>();

    let mut ct = 0;
    for possible in &input {
        let mut copy = possible.clone();
        copy.sort();
        if copy[0] + copy[1] > copy[2] {
            ct += 1;
        }
    }
    println!("{}", ct);

    ct = 0;
    for x in 0..(input.len() / 3) {
        for y in 0..3 {
            let mut t = [0; 3];
            for ix in 0..3 {
                t[ix] = input[x * 3 + ix][y];
            }
            t.sort();
            if t[0] + t[1] > t[2] {
                ct += 1;
            }
        }
    }
    println!("{}", ct);

    Ok(())
}