use std::collections::{HashMap, HashSet};
use std::error::Error;
use std::str::FromStr;

static COMPASS: &str = "NESW";

fn turn(facing: char, dir: char) -> char {
    let cur_ix: i64 = COMPASS.find(facing).unwrap().try_into().unwrap();
    match dir {
        'L' => COMPASS.chars().nth((cur_ix - 1).rem_euclid(4).try_into().unwrap()).unwrap(),
        'R' => COMPASS.chars().nth((cur_ix + 1).rem_euclid(4).try_into().unwrap()).unwrap(),
        _ => panic!("Invalid direction")
    }
}

pub fn day01(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let directions: HashMap<char, (i64, i64)> = HashMap::from([
        ('N', (0, 1)),
        ('E', (1, 0)),
        ('S', (0, -1)),
        ('W', (-1, 0))
    ]);

    let l: Vec<String> = lines.get(0).unwrap()
        .replace(" ", "")
        .split(',')
        .map(|x| x.to_string())
        .collect();

    let mut x = 0;
    let mut y = 0;
    let mut d = 'N';

    let mut visited: HashSet<(i64, i64)> = HashSet::new();
    let mut twice_visited: Option<(i64, i64)> = None;

    for instruction in l {
        d = turn(d, instruction.chars().next().unwrap());
        let (dx, dy) = directions.get(&d).unwrap();
        let distance = i64::from_str(instruction.get(1..).unwrap())?;
        for _ in 0..distance {
            x += dx;
            y += dy;
            if twice_visited.is_none() && visited.contains(&(x, y)) {
                twice_visited = Some((x, y));
            } else {
                visited.insert((x, y));
            }
        }
    };

    println!("{}", x.abs() + y.abs());
    if let Some((fx, fy)) = twice_visited {
        println!("{}", fx.abs() + fy.abs());
    }

    Ok(())
}