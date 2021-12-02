use lazy_static::lazy_static;
use regex::Regex;
use std::collections::HashMap;
use std::error::Error;
use std::str::FromStr;

#[derive(Debug)]
struct Room {
    name: String,
    sector: i64,
    checksum: String
}

#[derive(Debug)]
struct RoomParseError {}

impl Room {
    pub fn verify_checksum(&self) -> bool {
        let mut counts: HashMap<char, i64> = HashMap::new();
        for ch in self.name.chars() {
            if ch == '-' {
                continue
            }
            counts.entry(ch)
                .and_modify(|x| *x += 1)
                .or_insert(1);
        }

        let mut items = counts
            .iter()
            .map(|(k, v)| (v, k))
            .collect::<Vec<(&i64, &char)>>();
        items.sort_by(|a, b| b.0.cmp(a.0).then(a.1.cmp(b.1)));
        items.iter()
            .take(5)
            .map(|(_, ch)| ch)
            .zip(self.checksum.chars())
            .all(|(a, b)| **a == b)
    }

    pub fn decrypt(&self) -> String {
        let mut out = "".to_string();
        for ch in self.name.chars() {
            if ch == '-' {
                out += "-";
            } else {
                let n = (ch as u8) as i64;
                out += &((((n - 97 + self.sector) % 26) + 97) as u8 as char).to_string();
            }
        }
        out
    }
}

lazy_static! {
    static ref RE: Regex = Regex::new(r"([a-z-]+)-([0-9]+)\[([a-z]+)\]").unwrap();
}

impl FromStr for Room {
    type Err = RoomParseError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let caps = RE.captures(s).unwrap();
        let name = caps[1].to_string();
        let sector = i64::from_str(&caps[2]).unwrap();
        let checksum = caps[3].to_string();
        Ok(Room{name, sector, checksum})
    }
}

pub fn day04(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let rooms: Vec<Room> = lines.iter().map(|x| Room::from_str(x).unwrap()).collect();

    let ct: i64 = rooms.iter()
        .filter(|r| r.verify_checksum())
        .map(|r| r.sector)
        .sum();
    println!("{}", ct);

    rooms.iter()
        .filter(|r| r.decrypt() == "northpole-object-storage")
        .for_each(|r| println!("{}", r.sector));

    Ok(())
}
