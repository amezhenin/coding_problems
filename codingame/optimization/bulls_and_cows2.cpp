#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
vector<string> cases;
vector<int> flags;
int n;

int match(string src, string dest, int bulls, int cows)
{
    int b = 0;
    int c = 0;
    for (int i=0; i<n; i++){
        if (src[i] == dest[i]) b += 1;
        for (int j=0; j<n; j++){
            if (src[i] == dest[j]) c += 1;
        }
    }
    c -= b;
    //cerr << "Match: " << src << " " << dest << " " << bulls - b << " " << cows - c << endl;


    if ((cows == c) && (bulls == b)) return 1;
    return 0;
}

int main()
{
    int bulls;
    int cows;
    cin >> n; cin.ignore();
    cin >> bulls >> cows; cin.ignore();

    string dig = "0123456789";
    // dig = dig.substr(0, n);
    string last = dig.substr(0, n);
    // cases.push_back(last);


    do {
        if (dig.substr(0, n) != last and dig.substr(0, 1) != "0"){
            last = dig.substr(0, n);
            cases.push_back(last);
            flags.push_back(1);
            //cerr << "Item: " << last << endl;
        }
    } while (next_permutation(dig.begin(), dig.end()));
    // cerr << "Dig: " << dig << endl;

    // permutations(dig, n, "");
    int prev = 0;


    // game loop
    while (1) {
        for (int i=prev; i<cases.size(); i++){
            if (flags[i] == 1){
                prev = i;
                break;
            }
        }
        // prev = cases[0];
        cout << cases[prev] << endl; // number with numberLength count of digits
        // cerr << "Size: " << cases.size() << endl;


        cin >> bulls >> cows; cin.ignore();

        for (int k=prev; k<cases.size(); k++){
            //flags[k] *= match(prev, cases[k], bulls, cows);
            if (match(cases[prev], cases[k], bulls, cows) == 0){
                flags[k] = 0;
                // cerr << "Removing: " << cases[k] << endl;

                // cases.erase(cases.begin() + k);
                // k-=1;
            }
        }



    }
}