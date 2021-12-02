use std::collections::HashSet;
use std::error::Error;
use std::str::FromStr;

type Screen = HashSet<(i16, i16)>;

#[derive(Debug)]
enum Instruction {
    Rect(i16, i16),
    RotateX(i16, i16),
    RotateY(i16, i16)
}

#[derive(Debug)]
struct InstructionParseError {}

impl FromStr for Instruction {
    type Err = InstructionParseError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if s.starts_with("rect") {
            let mut i = s.split_whitespace().nth(1).unwrap()
                .split('x')
                .map(|x| i16::from_str(x).unwrap());
            let x = i.next().unwrap();
            let y = i.next().unwrap();
            Ok(Instruction::Rect(x, y))
        } else if s.starts_with("rotate") {
            let mut i = s.split('=').nth(1).unwrap()
                .split(" by ")
                .map(|x| i16::from_str(x).unwrap());
            let coord = i.next().unwrap();
            let num = i.next().unwrap();
            if s.starts_with("rotate row y") {
                Ok(Instruction::RotateY(coord, num))
            } else if s.starts_with("rotate column x") {
                Ok(Instruction::RotateX(coord, num))
            } else {
                Err(InstructionParseError {})
            }
        } else {
            Err(InstructionParseError {})
        }
    }
}

pub fn day08(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    // let mut screen: Screen = [[false; 50]; 6];
    let rows = 6;
    let columns = 50;
    let mut screen: Screen = HashSet::new();
    let instructions = lines.iter().map(|x| Instruction::from_str(x).unwrap());
    
    for ins in instructions {
        match ins {
            Instruction::Rect(x, y) => {
                for i in 0..x {
                    for j in 0..y {
                        screen.insert((i, j));
                    }
                }
            },
            Instruction::RotateY(row, n) => {
                let new_row = screen.iter()
                    .filter(|(_, y)| *y == row) 
                    .map(|(x, y)| ((x + n) % columns, *y))
                    .collect::<Screen>();
                screen = screen.iter().filter(|(_, y)| *y != row)
                    .map(|x| *x)
                    .collect::<Screen>()
                    .union(&new_row)
                    .map(|x| *x)
                    .collect::<Screen>();
            }
            Instruction::RotateX(col, n) => {
                let new_col = screen.iter()
                    .filter(|(x, _)| *x == col) 
                    .map(|(x, y)| (*x, (y + n) % rows))
                    .collect::<Screen>();
                screen = screen.iter().filter(|(x, _)| *x != col)
                    .map(|x| *x)
                    .collect::<Screen>()
                    .union(&new_col)
                    .map(|x| *x)
                    .collect::<Screen>();
            }
        }
    }
    println!("{}", screen.len());

    let mut out = String::new();
    for i in 0..rows {
        for j in 0..columns {
            if screen.contains(&(j, i)) {
                out.push('#');
            } else {
                out.push(' ');
            }
        }
        out.push('\n');
    }
    print!("{}", out);

    Ok(())
}