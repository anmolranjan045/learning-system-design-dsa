# include <bits/stdc++.h>

using namespace std;

void updateDiffArray(vector<int>& diff, int l, int h, int val) {
    diff[l] += val;
    if(h + 1 < diff.size()) diff[h + 1] -= val;
}

vector<int> diffArray(vector<int>& arr, vector<vector<int>>& queries) {
    int n=arr.size();
    vector<int> diff(n, 0), result=arr;
    for(auto& q: queries) {
        updateDiffArray(diff, q[0], q[1], q[2]);
    }
    result[0] += diff[0];
    for(int i=1; i<n; i++) {
        diff[i] += diff[i - 1];
        result[i] += diff[i];
    }
    return result;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<vector<int>> queries = {{1, 3, 10}, {2, 4, -5}};
    vector<int> res = diffArray(arr, queries);

    for (int num : res) {
        cout << num << " ";
    }
    return 0;
}