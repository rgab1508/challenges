#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main(){
    int t;cin>>t;
    while(t--){
        ll a, b;
        cin>>a>>b;
        if(a%b == 0) puts("0");
        else{
            ll c = b - (a%b);
            cout<<c<<"\n";
        }
    }
    return 0;
}