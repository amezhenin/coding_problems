/**
 * Docs: https://docs.rs/threadpool/1.8.1/threadpool/
 *       https://pkolaczk.github.io/multiple-threadpools-rust/
 */
use threadpool::ThreadPool;
use std::sync::mpsc::channel;
use std::{thread, time};


fn main() {
    let n_workers:usize = 4;
    let n_jobs:usize = 12;
    let pool = ThreadPool::new(n_workers);

    let (tx, rx) = channel();

    println!("Spawning threads");
    for i in 0..n_jobs {

        /**
            Arc can be used to share data between threads
            https://doc.rust-lang.org/beta/rust-by-example/std/arc.html

            use std::sync::Arc;
            let data = Arc::new(vec![1,2,3,4]);
            let data = Arc::clone(&data); <- for each thread
        */

        let tx = tx.clone();
        pool.execute(move || {
            println!("Thread {} started", i);
            thread::sleep(time::Duration::from_secs(3));
            tx.send((i, i*i)).expect("channel will be there waiting for the pool");
        });
    }

    // dropping tx will close rx as well, so it will be safe to iterate
    // this is not really needed in this particular code
    drop(tx);

    println!("Waiting for results");
    let mut results = vec![0; n_jobs];

    for _ in 0..n_jobs {
        let res = rx.recv().unwrap();
        let (idx, i_res) = res;
        println!("Main {} received {}", idx, i_res);
        results[idx] = i_res;
    }

    for i in 0..n_jobs {
        println!("Final {}", results[i]);
    }
}

/*
// Simple solution with Rayon, but tasks are executed at complete random with n_workers = number of CPU threads

use rayon::prelude::*;
fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter() // <-- just change that!
         .map(|&i| i * i)
         .sum()    // <-- or .collect()
}
*/