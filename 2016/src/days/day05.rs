use md5::{Md5, Digest};
use std::error::Error;

pub fn day05(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let room_id = lines.get(0).unwrap();
    let mut attempt = 0;
    let mut p1 = String::new();
    let mut p2: [i16; 8] = [-1; 8];

    while p1.len() < 8 || p2.contains(&-1) {
        let mut hasher = Md5::new();
        hasher.update(format!("{}{}", room_id, attempt));
        let result = hasher.finalize();

        if result[0] == 0 && result[1] == 0 && result[2] & 0xf0 == 0 {
            p1 += &format!("{:x}", result[2] & 0xf);

            let pos = result[2] & 0xf;
            if pos < 8 && p2[pos as usize] == -1 {
                p2[pos as usize] = (result[3] >> 4) as i16;
            }
        }

        attempt += 1;
    }

    println!("{}", &p1[..8]);
    for ch in p2 {
        print!("{:x}", ch);
    }
    println!();

    Ok(())
}