# include <bits/stdc++.h>

using namespace std;

long long ds[20][2][20];

long long getNonZeroLimit(const string& s, int ind, int tight, int cnt) {
    if(ind == s.size()) return 1;
    if(ds[ind][tight][cnt] != -1) return ds[ind][tight][cnt];
    int limit = (tight == 1 ? s[ind] - '0': 9);
    long long ans = 0;
    for(int i=0; i<=limit; i++) {
        int currentCnt = cnt + (i == 0 ? 0: 1);
        if(currentCnt <= 3) ans += getNonZeroLimit(s, ind+1, (tight & (i == s[ind] - '0')), currentCnt);
    }
    return ds[ind][tight][cnt] = ans;
}

int main() {
    long long l = 65536, r = 65536;
    memset(ds, -1, sizeof(ds));
    string ri = to_string(r);
    long long rightAns = getNonZeroLimit(ri, 0, 1, 0);
    memset(ds, -1, sizeof(ds));
    string le = to_string(l - 1);
    long long leftAns = getNonZeroLimit(le, 0, 1, 0);
    cout << rightAns - leftAns;
    return 0;
}