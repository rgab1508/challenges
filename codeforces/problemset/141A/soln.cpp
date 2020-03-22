#include <bits/stdc++.h>

using namespace std;

int main(){
    string guest, host, pile;
    cin>>guest>>host>>pile;
    if(guest.length() + host.length() != pile.length()){
        printf("NO\n");
        return 0;
    }
    bool flag = true;

    unordered_map<char, int> m;
    for(char c : pile){
        m[c]++;
    }
    for(char c: guest){
        if(m[c])
            m[c]--;
        else
            flag = false;
    }
    for(char c: host){
        if(m[c])
            m[c]--;
        else
            flag = false; 
    }
    if(flag) printf("YES\n");
    else printf("NO\n");
    return 0;
}