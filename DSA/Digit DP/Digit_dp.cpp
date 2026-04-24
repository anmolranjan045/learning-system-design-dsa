# include <bits/stdc++.h>

using namespace std;

int ds[20][2][20]; // index, tight, count

class Solution {
    public: 
        long long countDigitsInRange(const string& s, int ind, int tight, int cnt) {
            if(ind == s.size()) return cnt;
            if(ds[ind][tight][cnt] != -1) return ds[ind][tight][cnt];
            int limit = (tight == 1 ? s[ind] - '0' : 9);
            long long ans = 0;
            for(int i=0; i<=limit; i++) {
                long long updateCnt = cnt + (i == 3 ? 1 : 0);
                ans += countDigitsInRange(s, ind + 1, (tight & (i == s[ind] - '0')), updateCnt);
            }
            return ds[ind][tight][cnt] = ans;
        }
};

int main() {
    long long l, r;
    cin >> l >> r;

    Solution S;

    memset(ds, -1, sizeof(ds));
    string ri = to_string(r);
    long long rightAns = S.countDigitsInRange(ri, 0, 1, 0);

    memset(ds, -1, sizeof(ds));
    string le = to_string(l - 1);
    long long leftAns = S.countDigitsInRange(le, 0, 1, 0);

    cout << rightAns - leftAns;
    return 0;
}