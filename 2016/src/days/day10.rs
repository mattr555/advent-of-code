use lazy_static::lazy_static;
use regex::Regex;
use std::cmp;
use std::collections::HashMap;
use std::error::Error;
use std::str::FromStr;

#[derive(Debug, Clone, Copy)]
enum Location {
    Bot(u8),
    Output(u8)
}

#[derive(Debug, Clone, Copy)]
enum Instruction {
    Input(u8, Location),
    Gives(u8, Location, Location)
}

#[derive(Debug)]
struct InstructionParseError {}

type BotState = (Option<u8>, Option<u8>);

lazy_static! {
    static ref INPUT_RE: Regex = Regex::new(r"value (\d+) goes to bot (\d+)").unwrap();
    static ref GIVES_RE: Regex = Regex::new(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)").unwrap();
}

impl FromStr for Instruction {
    type Err = InstructionParseError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let input_res = INPUT_RE.captures(s);
        match input_res {
            Some(caps) => {
                let val = u8::from_str(&caps[1]).unwrap();
                let bot = u8::from_str(&caps[2]).unwrap();
                Ok(Instruction::Input(val, Location::Bot(bot)))
            }
            None => {
                let caps = GIVES_RE.captures(s).unwrap();
                let bot = u8::from_str(&caps[1]).unwrap();
                let low_loc = match &caps[2] {
                    "bot" => Location::Bot(u8::from_str(&caps[3]).unwrap()),
                    "output" => Location::Output(u8::from_str(&caps[3]).unwrap())
                };
                let high_loc = match &caps[3] {
                    "bot" => Location::Bot(u8::from_str(&caps[4]).unwrap()),
                    "output" => Location::Output(u8::from_str(&caps[4]).unwrap())
                };
                Ok(Instruction::Gives(bot, low_loc, high_loc))
            }
        }
    }
}

fn add_number(inp: u8, to: Option<BotState>) -> BotState {
    match to {
        None => (Some(inp), None),
        Some((None, None)) => (Some(inp), None),
        Some((Some(a), None)) => (Some(a), Some(inp)),
        Some(x) => x
    }
}

pub fn day10(lines: Vec<String>) -> Result<(), Box<dyn Error>> {
    let instructions = lines.iter().map(|x| Instruction::from_str(x).unwrap());
    let mut bot_state: HashMap<u8, BotState> = HashMap::new();
    let mut bot_programs: HashMap<u8, Instruction> = HashMap::new();
    let mut outputs: HashMap<u8, u8> = HashMap::new();

    for ins in instructions {
        match ins {
            Instruction::Input(val, Location::Bot(bot)) => {
                bot_state.insert(bot, add_number(val, bot_state.get(&bot)));
            },
            ref g @ Instruction::Gives(bot, _, _) => {
                bot_programs.insert(bot, g);
            },
            _ => {}
        }
    }

    let mut done = false;
    while !done {
        done = true;
        for (bot, st) in bot_state.iter_mut() {
            match st {
                (Some(a), Some(b)) => {
                    let ins = bot_programs.get(bot).unwrap();
                    match ins {
                        Instruction::Gives(_, low_loc, high_loc) => {
                            match low_loc {
                                Location::Bot(to_bot) => {
                                    bot_state.insert(*to_bot, add_number(cmp::min(a, b), bot_state.get(to_bot)));
                                },
                                Location::Output(to_box) => {
                                    outputs.insert(*to_box, cmp::min(a, b));
                                }
                            };
                            match high_loc {
                                Location::Bot(to_bot) => {
                                    bot_state.insert(*to_bot, add_number(cmp::max(a, b), bot_state.get(to_bot)));
                                },
                                Location::Output(to_box) => {
                                    outputs.insert(*to_box, cmp::max(a, b));
                                }
                            };
                            if cmp::min(a, b) == 17 && cmp::max(a, b) == 61 {
                                println!("{}", bot);
                            }
                            *st = (None, None);
                            done = false;
                        },
                        _ => {}
                    }
                },
                _ => {}
            }
        }
    }

    Ok(())
}