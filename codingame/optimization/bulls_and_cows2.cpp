#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
vector<string> all_tests;
vector<int> all_cows;
vector<int> all_bulls;
int n;

int match(string dest)
{
    for (int p=0; p<all_tests.size(); p++) {
        int b = 0;
        int c = 0;
        string src = all_tests[p];
        for (int i=0; i<n; i++){
            if (src[i] == dest[i]) b += 1;
            for (int j=0; j<n; j++){
                if (src[i] == dest[j]) c += 1;
            }
        }
        c -= b;
        cerr << "Match: " << dest << " " << src << " " << all_bulls[p] - b << " " << all_cows[p] - c << endl;

        if ((all_cows[p] != c) || (all_bulls[p] != b)) return 0;
    }

    return 1;
}
string dig = "0123456789";

string next(string last){
    do {
        string ns = dig.substr(0, n);
        if (dig.substr(0, 1) != "0" && ns!=last && match(ns) == 1){
            return ns;
        }
    } while (next_permutation(dig.begin(), dig.end()));

}

int main()
{
    int bulls;
    int cows;
    cin >> n; cin.ignore();
    cin >> bulls >> cows; cin.ignore();

    string cur = dig.substr(0, n);

    // game loop
    while (1) {
        cur=next(cur);

        cout << cur << endl;
        cin >> bulls >> cows; cin.ignore();

        all_tests.push_back(cur);
        all_cows.push_back(cows);
        all_bulls.push_back(bulls);
    }
}