use std::error::Error;

fn parse_int(s: &[u8], mut ix: usize) -> (i32, usize) {
    let mut res: i32= 0;
    while '0' <= (s[ix] as char) && (s[ix] as char) <= '9' {
        res *= 10;
        res += (s[ix] - ('0' as u8)) as i32;
        ix += 1;
    }
    (res, ix)
}

fn parse_marker(b: &[u8], mut ix: usize) -> (i32, i32, usize) {
    let (advance, n1) = parse_int(b, ix+1);
    ix = n1;
    assert!(b[ix] as char == 'x');
    let (repeat, n2) = parse_int(b, ix+1);
    ix = n2;
    assert!(b[ix] as char == ')');
    ix += 1;
    (advance, repeat, ix)
}

fn p1(b: &[u8]) -> i32 {
    let mut n = 0;
    let mut ix: usize = 0;

    while ix < b.len() {
        match b[ix] as char {
            '(' => {
                let (advance, repeat, n1) = parse_marker(b, ix);
                ix = n1;
                ix += advance as usize;
                n += advance * repeat;
            }
            _ => {
                ix += 1;
                n += 1;
            }
        }
    }

    n
}

fn decomp_len(b: &[u8], start: usize, end: usize) -> i128 {
    let mut n = 0;
    let mut ix = start;

    while ix < end {
        match b[ix] as char {
            '(' => {
                let (advance, repeat, n1) = parse_marker(b, ix);
                let sublen = decomp_len(b, n1, n1+advance as usize);
                ix = n1 + advance as usize;
                n += sublen * repeat as i128;
            }
            _ => {
                ix += 1;
                n += 1;
            }
        }
    }

    n
}

pub fn day09(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let l = lines.get(0).unwrap();
    let b = l.as_bytes();

    println!("{}", p1(b));
    println!("{}", decomp_len(b, 0, b.len()));

    Ok(())
}
