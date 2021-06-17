#include "thread_pool.hpp"

using namespace std;


int foo(int n) {
    cout << "Thread " << n << " started" << endl;

    // do some work
    this_thread::sleep_for(std::chrono::seconds(1);
    int res = n * n;

    cout << "Received result for " << n << ": " << res << endl;
    return res;
}


int main()
{
    int n_workers = 4;
    int n_jobs = 12;

    thread_pool pool(n_workers);

    vector<future<int>> results = vector<future<int>>(n_jobs);
    for (int i = 0; i < n_jobs; i++) {
        results[i] = pool.submit(foo, i);
    }

    // it is not necessary to wait for tasks to complete, but it can be done is necessary
    // pool.wait_for_tasks();
    for (int i = 0; i < n_jobs; i++) {
        cout << "Final " << results[i].get() << endl;
    }
    return 0;
}