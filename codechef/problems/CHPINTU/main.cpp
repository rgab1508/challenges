#include <bits/stdc++.h>

using namespace std;

bool comp(pair<int, int> &x, pair<int, int> &y){
    return x.second < y.second;
}

int main(){
    int t;
    map<int,int>a;
    vector<pair<int,int>> vec;
    cin>>t;
    for(int i=0;i<t;i++){
        int m, n;
        cin>>m>>n;
        // cout<<m<<"\n";
        vector<int> f;
        vector<int> p;
        for(int j=0;j<m;j++){
            int tt; cin>>tt;
            f.push_back(tt);
        }
        // printf("---\n");
        for(int k=0;k<m;k++){
            int tt; cin>>tt;
            p.push_back(tt);
        }

        for(int im=0;im<p.size();im++){
            // printf("%d -> %d\n", f[im], p[im]);
            a[f[im]] += p[im];
        }
        
        auto it = a.begin();
        int best_min = 10000;
        while(it != a.end()){
            if(it->second < best_min){
                best_min = it->second;
            }
            it++;
        }
        cout<<best_min;
    }
    return 0;
}