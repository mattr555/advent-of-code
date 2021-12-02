use std::collections::HashMap;
use std::error::Error;

pub fn day06(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let mut maps: Vec<HashMap<char, i32>> = Vec::new();
    for _ in 0..(lines.get(0).unwrap().len()) {
        maps.push(HashMap::new());
    }

    for l in lines {
        for (ix, ch) in l.chars().enumerate() {
            maps.get_mut(ix).unwrap().entry(ch)
                .and_modify(|ct| *ct += 1)
                .or_insert(1);
        }
    }

    let mut p1 = String::new();
    let mut p2 = String::new();
    for m in maps {
        let mut v = m.iter().map(|(k, v)| (v, k)).collect::<Vec<(&i32, &char)>>();
        v.sort();
        let (_, most) = v.last().unwrap();
        let (_, least) = v.get(0).unwrap();
        p1.push(**most);
        p2.push(**least);
    }

    println!("{}", p1);
    println!("{}", p2);

    Ok(())
}