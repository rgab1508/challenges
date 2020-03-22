#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        vector<int> a, b;
        map<int, pair<int, int>> m;
        set<int> taken;
        for(int i=0;i<n;i++){
            int ii;cin>>ii;
            a.push_back(ii);
        }
        for(int i=0;i<n;i++){
            int ii;cin>>ii;
            b.push_back(ii);
        }
        m[0] = make_pair(a[0], b[0]);
        taken.insert(a[0]+b[0]);
        a.erase(a.begin());b.erase(b.begin());
        for(int i=1;i<n;i++){
            bool found = false;
            for(auto j=a.begin();j<a.end();j++){
                for(auto k=b.begin();k<b.end();k++){
                    int sum = *j + *k;
                    if(taken.find(sum) == taken.end()){
                        taken.insert(sum); 
                        m[i] = make_pair(*j, *k); 
                        a.erase(j);
                        b.erase(k);
                        found = true;
                        break;
                    }
                    if(found) break;
                }
                if (found) break;
            }
        }
        for(int it=0;it<n;it++){
            // cout<<m[it].first<<" "<<m[it].second<<endl;//<<" "<<m[it].second<<" "<<m[it].second.first+m[it].second.second<<endl;
            auto mm = m.find(it);
            cout<<mm->second.first<<" ";
            // cout<<it<<endl;
        }
        cout<<endl;
        for(int it=0;it<n;it++){
            // cout<<m[it].first<<" "<<m[it].second<<endl;//<<" "<<m[it].second<<" "<<m[it].second.first+m[it].second.second<<endl;
            auto mm = m.find(it);
            cout<<mm->second.second<<" ";
            // cout<<it<<endl;
        }
        cout<<endl;
        m.clear();
    }
    return 0;
}