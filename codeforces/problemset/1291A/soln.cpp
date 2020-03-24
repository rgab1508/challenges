#include <bits/stdc++.h>

using namespace std;


int calc_sum(vector<int> a){
    int sum = 0;
    for(auto x: a){
        sum += x;
    }
    return sum;
}

vector<int> fix_sum(vector<int> a){
    if(calc_sum(a) % 2 == 0){
        return a;
    }else{
        for(auto it= a.begin();it != a.end();it++){
            if(*it %2 != 0){
                a.erase(it);
                return fix_sum(a);
            }
        }
        return {-1};
    }
}

vector<int> fix_last(vector<int> a){
    if(a.size() != 0){
        auto last = a.end()-1;
        cout<<*last<<" ";
        if(*last % 2 != 0){
            return a;
        }
        else if(*last % 2 == 0){
            a.erase(last);
            return fix_last(a);
        }
    }else{
        return {-1};
    }
}

void solve(){
    int n;
    vector<int> a;
    int sum = 0;
    for(int i=0;i<n;i++){
        int c;cin>>c;
        a.push_back(c);
        sum += c;
    }
    vector<int> b;
    b = fix_sum(a);
    if(b[0] == -1){
        printf("not sum\n");
        puts("-1");
        return;
    }else{
        a = b;
        vector<int> c;
        c = fix_last(a);
        if(c[0] = -1){
            printf("no last\n");
            puts("-1");
        }else{
            a =c;
            for(auto x: a)
                cout<<x<<" ";
            cout<<"\n";
        }
    }
    
}


int main(){
    int t;cin>>t;
    while(t--)
        solve();
    return 0;
}