# include <bits/stdc++.h>

using namespace std;

long long ds[12][2][2]; // index, tight, flag

long long getThreeCount(const string& s, int ind, int tight, int flag) {
    if(ind == s.size()) return flag;
    if(ds[ind][tight][flag] != -1) return ds[ind][tight][flag];
    int limit = (tight == 1 ? s[ind] - '0': 9);
    long long ans = 0;
    for(int i=0; i<=limit; i++) {
        int updateFlag = (flag | (i == 3));
        ans += getThreeCount(s, ind + 1, (tight & (i == s[ind] - '0')), updateFlag);
    }
    return ds[ind][tight][flag] = ans;
}

long long countDigitOne(int n) {
    memset(ds, -1, sizeof(ds));
    string s = to_string(n);
    return n - getThreeCount(s, 0, 1, 0);
}

int main() {
    long long n = 40;
    // cin >> n;
    cout << countDigitOne(n);
    return 0;
}