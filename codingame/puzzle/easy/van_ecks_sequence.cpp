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
    int c[1000000];
    std::fill_n(c, 1000000, 0);

    for (int i=0; i<n-1; i++) {
        if (c[a] != 0) {
            int ca = c[a];
            c[a] = i;
            a = i - ca;
        } else {
            c[a] = i;
            a = 0;
        }
    }
    cout << a << endl;
}