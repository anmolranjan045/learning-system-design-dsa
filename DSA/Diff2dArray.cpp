# include <bits/stdc++.h>

using namespace std;

vector<vector<int>> applyDiff2D(vector<vector<int>>& mat, vector<vector<int>>& opr) {
    int n=mat.size(), m=mat[0].size();
    vector<vector<int>> diff(n, vector<int> (m, 0));
    for(auto o: opr) {
        int r1 = o[1], r2 = o[3], c1 = o[2], c2 = o[4];
        int val = o[0];
        diff[r1][c1] += val;
        if(r2 + 1 < n) diff[r2 + 1][c2] -= val;
        if(c2 + 1 < m) diff[r2][c1 + 1] -= val;
        if(c2 + 1 < m && r2 + 1 < n) diff[r2 + 1][c2 + 1] += val;
    }

    for(int i=0; i<n; i++) {
        for(int j=1; j<m; j++) {
            diff[i][j] += diff[i][j-1];
        }
    }

    for(int j=0; j<m; j++) {
        for(int i=1; i<n; i++) {
            diff[i][j] += diff[i-1][j];
        }
    }

    vector<vector<int>> res = mat;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            res[i][j] += diff[i][j];
        }
    }
    return res;
}

int main() {
    vector<vector<int>> mat = {
        {1, 2, 3},
        {1, 1, 0},
        {4, -2, 2}
    };

    vector<vector<int>> opr = {
        {2, 0, 0, 1, 1},   
        {-1, 1, 0, 2, 2} 
    };

    vector<vector<int>> res = applyDiff2D(mat, opr);

    for (auto& row : mat) {
        for (int val : row) cout << val << " ";
        cout << endl;
    }
    return 0;
}