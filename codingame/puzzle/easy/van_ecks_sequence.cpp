/*
https://www.codingame.com/training/easy/van-ecks-sequence
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int a, n;
    cin >> a; cin.ignore();
    cin >> n; cin.ignore();

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    int c[10];
    std::fill_n(c, 10, -1);

    for (int i=0; i<n-1; i++) {
        if (c[a] != -1) {
            int ca = c[a];
            c[a] = i;
            a = i - ca;
        } else {
            c[a] = i;
            a = 0;
        }
    }
    /* SOLUTION WITH MAP

    map <int, int> keys;
    for (int n = 1; n < N; n++)
    {
        int* p = &keys[A1];
        A1 = (*p) ? (n - *p) : 0;
        *p = n;
    }
     VECTOR
     vector<int> An(N,-1);
    */

    cout << a << endl;
}