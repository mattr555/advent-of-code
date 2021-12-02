use std::collections::HashMap;
use std::error::Error;
use num::clamp;

pub fn day02(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let directions: HashMap<char, (i64, i64)> = HashMap::from([
        ('D', (0, 1)),
        ('R', (1, 0)),
        ('U', (0, -1)),
        ('L', (-1, 0))
    ]);

    let numpad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']];
    let mut x = 1;
    let mut y = 1;

    let mut code = String::new();

    for line in &lines {
        for ch in line.chars() {
            let (dx, dy) = directions.get(&ch).unwrap();
            x = clamp(x + dx, 0, 2);
            y = clamp(y + dy, 0, 2);
        }
        code += &numpad[y as usize][x as usize].to_string();
    }

    println!("{}", code);

    let numpad_p2 = [
        [' ', ' ', '1', ' ', ' '],
        [' ', '2', '3', '4', ' '],
        ['5', '6', '7', '8', '9'],
        [' ', 'A', 'B', 'C', ' '],
        [' ', ' ', 'D', ' ', ' ']
    ];

    code.clear();
    x = 0;
    y = 2;

    for line in &lines {
        for ch in line.chars() {
            let (dx, dy) = directions.get(&ch).unwrap();
            let px = clamp(x + dx, 0, 4);
            let py = clamp(y + dy, 0, 4);
            if numpad_p2[py as usize][px as usize] != ' ' {
                x = px;
                y = py;
            }
        }
        code += &numpad_p2[y as usize][x as usize].to_string();
    }

    println!("{}", code);

    Ok(())
}