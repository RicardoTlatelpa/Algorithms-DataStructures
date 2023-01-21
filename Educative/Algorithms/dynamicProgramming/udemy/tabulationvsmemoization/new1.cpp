#include<iostream>
#include<vector>

#define int long long int
#define F first
#define S second
#define pb push_back

using namespace std;

int cnt = 0;
vector<int> memo; // memoization

int fib(int n){
    cnt++;    
    if(n <=2) return 1;
    // memoization part
    if(memo[n] != -1) return memo[n];
    // recursive relation
    return memo[n] = fib(n-1) + fib(n-2);
}

int32_t main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n = 10;
    memo.resize(n + 1, -1);
    cout << fib(n) << endl;
    cout << cnt << endl;
    return 0;
}