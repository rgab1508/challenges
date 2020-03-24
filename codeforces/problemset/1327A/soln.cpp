#include <bits/stdc++.h>

using namespace std;


void solve(){
	long long n, k;
	cin>>n>>k;
	long long count = k*k;
	if(n < count){
		puts("NO");
		return;
	}
	if((n % 2 == 0) && (k % 2==0) || (n % 2 == 1) && (k % 2 == 1)){
		puts("YES");
	}else{
		puts("NO");
	}
}


int main(int argc, char const *argv[])
{
	int t;cin>>t;
	while(t--)
		solve();
	return 0;
}