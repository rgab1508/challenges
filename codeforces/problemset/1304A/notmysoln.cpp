#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        int x, y, a, b;cin>>x>>y>>a>>b;
        if((y - x) % (a + b) == 0){
            int T = (y - x) / (a + b);
            printf("%d\n", T);
        }else{
            printf("-1\n");
        }
    }
    return 0;
}