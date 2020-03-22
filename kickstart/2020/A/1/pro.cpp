#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;cin>>t;
    for(int it=0;it<t;it++){
        int n, b;cin>>n>>b;
        vector<int> a;
        int bought = 0;
        for(int i=0;i<n;i++){
            int c;cin>>c;
            a.push_back(c);
        }
        sort(a.begin(), a.end());
        // cout<<a[0]<<" "<<a[n-1];
        auto i=a.begin();
        while(i != a.end()){
            if(b >= *i){
                b -= *i;
                // cout<<*i<<"\n";
                bought++;
            }
            i++;
        }
        printf("Case #%d: %d\n", it+1, bought);
    }
}