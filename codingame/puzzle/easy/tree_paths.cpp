/**
 * https://www.codingame.com/training/easy/tree-paths
 * */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int n, v, m;
    cin >> n; cin.ignore();
    cin >> v; cin.ignore();
    cin >> m; cin.ignore();

    vector<int> parent(n+1, -1);
    vector<int> left(n+1, -1);
    vector<int> right(n+1, -1);

    for (int i = 0; i < m; i++) {
        int p, l, r;
        cin >> p >> l >> r; cin.ignore();
        parent[l] = p;
        parent[r] = p;
        left[p] = l;
        right[p] = r;
    }

    vector<string> res;
    int cur = v;
    while (parent[cur] != -1) {
        int par = parent[cur];
        string nres = left[par] == cur ? "Left" : "Right";
        res.push_back(nres);
        cur = par;
    }

    if (res.size() == 0) {
        res.push_back("Root");
    }

    for (int i = res.size()-1; i >= 0; i--) {
        cout << res[i] << ((i > 0) ? " " : "");
    }
    cout << endl;
}