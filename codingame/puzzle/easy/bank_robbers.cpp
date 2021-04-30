/**
 * https://www.codingame.com/training/easy/bank-robbers
 **/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int R;
    cin >> R; cin.ignore();

    vector<int> rr(R, 0);

    int V;
    cin >> V; cin.ignore();
    for (int i = 0; i < V; i++) {
        int C;
        int N;
        cin >> C >> N; cin.ignore();
        sort(rr.begin(), rr.end());
        rr[0] += pow(5, C - N) * pow(10, N);
    }
    sort(rr.begin(), rr.end());
    cout << rr[R-1] << endl;
}

/*
#include <bits/stdc++.h>
using namespace std;
int R,C,N,T[5];
int main()
{
    cin >> R >> C;
    while (cin >> C >> N) *min_element(T, T+R) += pow(10,N)*pow(5,C-N);
    cout << *max_element(T, T+R) << endl;
}


// init array with zeros
uint64_t robbers[R] = {};

*/