/**
https://stepik.org/lesson/541855/step/2?unit=535316

Use Binary Lifting (Kth Ancestor of a Tree Node) to solve this problem
Single-threaded version

https://www.youtube.com/watch?v=oib-XsjFa-M
https://www.youtube.com/watch?v=dOAxrhAUIhA
*/
#pragma GCC optimize "O3,omit-frame-pointer,inline"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");

const int L = 19;
//const int L = 3;

vector<vector<int>> up;
vector<int> ic;
vector<vector<int>> d;
vector<int> depth;


void build_up(const vector<int>& parent) {
    int n = parent.size();
    up = vector<vector<int>>(n, vector<int>(L));
    depth = vector<int>(n);
    // up[v][j] is 2^j -th ancestor of node v
    //parent[0] = 0;
    for(int v = 0; v < n; v++) {
        up[v][0] = parent[v];
        if(v != 0) {
            depth[v] = depth[parent[v]] + 1;
        }
        for(int j = 1; j < L; j++) {
            up[v][j] = up[ up[v][j-1] ][j-1];
        }
    }
}


int get_lca(int a, int b) { // O(log(N))
    if(depth[a] < depth[b]) {
        swap(a, b);
    }
    // 1) Get same depth.
    int k = depth[a] - depth[b];
    for(int j = L - 1; j >= 0; j--) {
        if(k & (1 << j)) {
            a = up[a][j]; // parent of a
        }
    }
    // 2) if b was ancestor of a then now a==b
    if(a == b) {
        return a;
    }
    // 3) move both a and b with powers of two
    for(int j = L - 1; j >= 0; j--) {
        if(up[a][j] != up[b][j]) {
            a = up[a][j];
            b = up[b][j];
        }
    }
    return up[a][0];
}

int max_ic(int pq, const vector<int>& dm) {
    int best = -11111;
    for (int i : dm) {
        int r = get_lca(pq, i);
        int ric = ic[r];
        if (best < ric) {
            best = ric;
        }
    }
    return best;
}

int calculate(const vector<int>& p) {
    int best = -22222;
    long best_val = -33333;
    for (int d_idx=0; d_idx<d.size(); d_idx++) {
        vector<int> dm = d[d_idx];
        long cur_val = 0;
        for (int pq : p){
            int m_ic = max_ic(pq, dm);  // slowest <<<<<<<<<<<<<<<<<<<<
            cur_val += m_ic;
        }
        if (best_val < cur_val) {
            best_val = cur_val;
            best = d_idx + 1;
        }
    }

    return best;
}


int main()
{
    // num of graph vertices
    int _n;
    in >> _n;
    // graph parents
    vector<int> n(_n);
    n[0] = 0;
    for (int i=1; i<_n; i++) {
        int x;
        in >> x;
        n[i] = x-1;
    }

    build_up(n);  // BUG
    ic = vector<int>(_n);
    for (int i=0; i<_n; i++) {
        in >> ic[i];
    }

    // diseases
    int _d;
    in >> _d;
    d = vector<vector<int>>(_d);
    for (int i=0; i<_d; i++) {
        int dsize = 0;
        in >> dsize;
        vector<int> dm(dsize);
        for (int ds=0; ds < dsize; ds++) {
            int x;
            in >> x;
            dm[ds] = x-1;
        }
        d[i] = dm;
    }

    // patients
    int _p;
    in >> _p;
    for (int _pi=0; _pi < _p; _pi++) {
        int psize = 0;
        in >> psize;
        vector<int> p(psize);
        for (int ps=0; ps < psize; ps++) {
            int x;
            in >> x;
            p[ps] = x - 1;
        }

        int best = calculate(p);
        cout << "[" << _pi << "/" << _p << "]> " << best << endl;
        out << best << endl;
    }
}
