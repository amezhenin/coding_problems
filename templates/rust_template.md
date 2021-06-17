### STDIO read helper
``` 
fn read<T: std::str::FromStr>() -> T {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().ok().unwrap()
}

fn main() {
    let mut r1: u32 = read();
    let mut r2: u32 = read();
}
```

### read line of ints
```
    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();

    for i in inputs.split_whitespace() {
        let t = parse_input!(i, i32);
    }
```

### Read line with array of strings and parse each position separately
```
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let x = parse_input!(inputs[0], i32);
    let y = parse_input!(inputs[1], i32);
```


### HashMap
```
use std::collections::HashMap;

let mut buffer: HashMap<i32, i32> = HashMap::new();
for i in 0..end_position-1 {
    match buffer.insert(key, value) {
        None => <some code>,     // None is returned is this key didn't exist
        Some(x) => <some code>,  // `x` in this case previous value for this key
    }
}
```

### Read and parse into HashMap
```
    let ext_mime = (0..n).map(|_| {
        let v = read_line().split(" ").map(|s| s.to_string()).collect::<Vec<_>>();
        (v.get(0).unwrap().to_string().to_lowercase(), v.get(1).unwrap().to_string())
    }).collect::<HashMap<String, String>>();
    //.collect::<Vec<String>>();
```

### Map and lambda functions
```
    let sumsq:i32 = s.bytes().map(|c| (c - b'0').pow(2) as i32).sum();
    let happy_sign = |h| if h { ":)" } else { ":(" };
```

### Take last element of the split
```
    let ext = fname.split('.').next_back().unwrap();
```

### Iterate vector and match particular position or do default action
```
//                                      <  condition here vvv  >
if let Some(pos) = vect.iter().position(|top| container <= *top) {
    // we have a match at position `pos` 
    vect[pos] = container;
} else {
    // no match, default action
    vect.push(container);
}
``` 


### Suppress warning
```
#[allow(dead_code)]
```
