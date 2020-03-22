#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;cin>>t;
    for(int it=0;it<t;it++){
        int x, y, a, b;cin>>x>>y>>a>>b;
        int c = 0;
        bool meet = false;
        if (x == y) {
            meet = true;
        }
        while(x < y){
            x += a;
            y -= b;
            c++;
            if (x == y){
                meet = true;
            }
        }
        
        if(meet) printf("%d\n", c);
        else printf("-1\n");
    }
    return 0;
}