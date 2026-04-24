# include <bits/stdc++.h>

using namespace std;

long long ds[12][12];

long long getNumbers(vector<int>& arr, int ind, int prev, int n) {
    if(ind == n) return 1;
    if(ds[ind][prev] != -1) return ds[ind][prev];
    long long ans = 0;
    for(int i=0; i<arr.size(); i++) {
        if(prev == 0 || abs(arr[i] - prev) <= n) {
            ans += getNumbers(arr, ind + 1, arr[i], n);
        }
    }
    return ds[ind][prev] = ans;
}

int main() {
    vector<int> arr = {1, 2, 3};
    int n = 2;
    memset(ds, -1, sizeof(ds));
    cout << getNumbers(arr, 0, 0, n);
    return 0;
}