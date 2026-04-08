#include <bits/stdc++.h>

using namespace std;

string reverseEachWord(string str) {
    string revStr = "";
    stringstream s(str);
    string word;
    
    while (s >> word) {
        reverse(word.begin(), word.end());
        revStr += word + " "; 
    }
    
    if (!revStr.empty()) {
        revStr.pop_back();
    }
    
    return revStr;
}

int main() {
    string s = "This is a house";
    cout << reverseEachWord(s) << endl; 
    return 0;
}