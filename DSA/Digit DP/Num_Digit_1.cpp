// LC Hard

# include <bits/stdc++.h>

using namespace std;

long long ds[20][2][20];

long long getOneCount(const string& s, int ind, int tight, int cnt) {
    if(ind == s.size()) return cnt;
    if(ds[ind][tight][cnt] != -1) return ds[ind][tight][cnt];
    int limit = (tight == 1 ? s[ind] - '0': 9);
    long long ans = 0;
    for(int i=0; i<=limit; i++) {
        int currentCnt = cnt + (i == 1 ? 1: 0);
        ans += getOneCount(s, ind+1, (tight & (i == s[ind] - '0')), currentCnt);
    }
    return ds[ind][tight][cnt] = ans; 
}

long long countDigitOne(int n) {
    memset(ds, -1, sizeof(ds));
    string s = to_string(n);
    return getOneCount(s, 0, 1, 0);
}

int main() {
    long long n;
    cin >> n;
    cout << countDigitOne(n);
    return 0;
}