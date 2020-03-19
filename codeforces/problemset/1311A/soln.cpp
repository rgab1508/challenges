#include <bits/stdc++.h>

using namespace std;

int pickX(int a, int b){
    int x = 0;
    while (a <= b){
        x++;
        a++;
    }
    if (x%2 != 0) return x;
    else return --x;
}

int pickY(int a, int b){
    int y = 0;
    while(a >= b){
        y++;
        a--;
    }
    if(y %2 == 0) return y;
    else return --y;
}

int main(){
    int t;cin>>t;

    while(t--){
        int a, b;cin>>a>>b;
        int c=0;
        // printf("%d %d\n", a, b);
        while(a != b){
            if (a<b){
                int x = pickX(a, b);
                // printf("ADD %d\n", x);
                a += x;
                c++;
            }else{
                int y = pickY(a, b);
                // printf("SUB %d\n", y);
                a -= y;
                c++;
            }
        }
        // printf("%d %d\n", a, b);
        printf("%d\n", c);
    }
    return 0;
}