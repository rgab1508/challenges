#include <bits/stdc++.h>

using namespace std;

int main(){
    int d, sumTime;cin>>d>>sumTime;
    map<int, int> m;
    vector<int> ans;
    for(int id=0;id<d;id++){
        int minTime, maxTime;cin>>minTime>>maxTime;
        m.insert(make_pair(minTime, maxTime));
    }
    int tempSumTime = sumTime;
    // printf("%d", tempSumTime);
    for(auto x: m){
        tempSumTime -= x.second;
    }
    // printf("%d", tempSumTime);

    if(tempSumTime > 0){
        printf("NO\n");
        return 0;
    }
    tempSumTime = sumTime;
    for(auto x: m){
        tempSumTime -= x.first;
    }
    // printf("%d", tempSumTime);

    if(tempSumTime < 0){
        printf("NO\n");
        return 0;
    }

    printf("YES\n");
    return 0;
}