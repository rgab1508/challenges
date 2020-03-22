#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        bool pal = false;
        vector<int> a;
        for(int i=0;i<n;i++){
            int c;cin>>c;
            a.push_back(c);
        }

        for(int i=0;i<n-2;i++){
            if(a[i] == a[i+2]){
                pal = true;
            }
        }
        if(pal) puts("YES");
        else puts("NO");
    }
    return 0;
}