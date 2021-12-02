use std::collections::HashSet;
use std::error::Error;

fn has_abba(input: &str) -> bool {
    let s: &[u8] = input.as_bytes();
    let mut is_outside = true;
    let mut found_outside = false;
    let mut found_inside = false;
    for i in 0..(s.len() - 3) {
        if s[i] == '[' as u8 {
            is_outside = false;
        } else if s[i] == ']' as u8 {
            is_outside = true;
        }

        if s[i] != s[i+1] && s[i] == s[i+3] && s[i+1] == s[i+2] {
            if is_outside {
                found_outside = true;
            } else {
                found_inside = true;
            }
        }
    }
    found_outside && !found_inside
}

fn find_aba_pairs(input: &str) -> bool {
    let s: &[u8] = input.as_bytes();
    let mut is_outside = true;
    let mut aba_outside: HashSet<(u8, u8)> = HashSet::new();
    let mut bab_inside: HashSet<(u8, u8)> = HashSet::new();
    for i in 0..(s.len() - 2) {
        if s[i] == '[' as u8 {
            is_outside = false;
        } else if s[i] == ']' as u8 {
            is_outside = true;
        }

        if s[i] != s[i+1] && s[i] == s[i+2] {
            if is_outside {
                aba_outside.insert((s[i], s[i+1]));
            } else {
                bab_inside.insert((s[i+1], s[i]));
            }
        }
    }

    aba_outside.intersection(&bab_inside).count() > 0
}

pub fn day07(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let n = lines.iter()
        .filter(|x| has_abba(x))
        .count();
    println!("{}", n);

    let p2 = lines.iter()
        .filter(|x| find_aba_pairs(x))
        .count();
    println!("{}", p2);

    Ok(())
}