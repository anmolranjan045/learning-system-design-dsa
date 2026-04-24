# include <bits/stdc++.h>

using namespace std;

long long ds[10][2][80];

bool isPrime(int num) {
    if(num == 0 || num == 1) return false;
    for(int i=2; i<=num/2; i++) {
        if(num % i == 0) return false;
    }
    return true;
}

long long GOneNumber(const string& s, int ind, int tight, int sum) {
    if(ind == s.size()) {
        if (isPrime(sum)) return 1;
        return 0;
    }
    if(ds[ind][tight][sum] != -1) return ds[ind][tight][sum];
    int limit = (tight == 1 ? s[ind] - '0': 9);
    long long ans = 0;
    for(int i=0; i<=limit; i++) {
        long long currentSum = sum + i;
        ans += GOneNumber(s, ind + 1, (tight & (s[ind] - '0' == i)), currentSum);
    }
    return ds[ind][tight][sum] = ans;
}

int main() {
    long long l = 20, r = 29;

    memset(ds, -1, sizeof(ds));
    string ri = to_string(r);
    long long rightAns = GOneNumber(ri, 0, 1, 0);

    memset(ds, -1, sizeof(ds));
    string le = to_string(l - 1);
    long long leftAns = GOneNumber(le, 0, 1, 0);

    cout << rightAns - leftAns;
    return 0;
}