#include<bits/stdc++.h>
using namespace std;

void symmetricEncode(string str, int n){
    string r = str;
    sort(r.begin(), r.end());
    r.erase(unique(r.begin(), r.end()), r.end());

    string decoded = str;
    for (int i = 0; i < n; i++) {
        encodedString[i] = r[n - i - 1];
    }
    cout<<decoded<<endl;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string str;
        cin>>str;
        symetric(str,n);
    }
}
