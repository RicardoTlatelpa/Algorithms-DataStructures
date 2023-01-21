#include<iostream>

#define int long long int
#define F first
#define S second
#define pb push_back

using namespace std;

int cnt = 0;
int32_t main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    // TABULATION
    int n = 20;
    int fib[n + 1];
    fib[1] = fib[2] = 1;
    for(int i = 3; i <= n; i++){
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    cout << fib[n] << endl;
    return 0;
}