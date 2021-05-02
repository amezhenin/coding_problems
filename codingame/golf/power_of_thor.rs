use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}
fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let x = parse_input!(inputs[0], i32); // the X position of the light of power
    let y = parse_input!(inputs[1], i32); // the Y position of the light of power
    let mut h = parse_input!(inputs[2], i32); // Thor's starting X position
    let mut v = parse_input!(inputs[3], i32); // Thor's starting Y position

    // game loop
    loop {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let remaining_turns = parse_input!(input_line, i32);

        let mut d = "".to_string();
        if y<v {d=[&d, "N"].concat();v-=1;}
        if y>v {d=[&d, "S"].concat();v+=1;}
        if x<h {d=[&d, "W"].concat();h-=1; }
        if x>h {d=[&d, "E"].concat();h+=1;}

        // A single line providing the move to be made: N NE E SE S SW W or NW
        println!("{}", d);
    }
}
