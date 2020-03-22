#include <bits/stdc++.h>

using namespace std;

pair<int, pair<vector<int>::iterator, int>> max_diff(vector<int> a){
    int best_diff = 0;
    vector<int>::iterator best_diff_lb;
    int best_diff_el =0;
    
    for(auto i=a.begin();i < a.end();i++){
        if((*(i+1) - *i)> best_diff){
            best_diff = *(i+1) - *i; 
            best_diff_lb = i;
            best_diff_el = *i;
        }
    }
    return make_pair(best_diff, make_pair(best_diff_lb, best_diff_el));
}

int main(){
    int t;cin>>t;
    for(int it=0;it<t;it++){
        int n, k;cin>>n>>k;
        cout<<k<<" "<<n<<endl;
        vector<int> m;
        for(int i=0;i<n;i++){
            int c;cin>>c;
            m.push_back(c);
        }
        while(k--){
            pair<int, pair<vector<int>::iterator, int>> diff = max_diff(m);
            m.insert(diff.second.first,  diff.second.second + (int)diff.first / 2);
        }
        
        for(auto x: m){
            printf("%d\n", x);
        }
    }
    return 0;
}