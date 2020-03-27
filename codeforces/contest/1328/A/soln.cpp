#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


void solve(){
    ll a, b;
    cin>>a>>b;
    ll c = 0;
    while(a % b != 0){
        a++;
        c++;
    }
    cout<<c<<"\n";
}


int main(){
    int t;cin>>t;
    while(t--)
        solve();
    return 0;
}