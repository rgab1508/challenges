#include <bits/stdc++.h>
 
using namespace std;

typedef long long ll;

void solve(){
    ll n, k;
    cin>>n>>k;
    string s;
    for(auto i=0;i<n-2;i++){
        s += "a";
    }
    s+= "bb";
    cout<<s<<"\n";
}

int main(){
   int t;cin>>t;   
    while(t--)
        solve();
}