#include<iostream>


using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    int a[n];
    int dp[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    dp[0] = a[0];
    dp[1] = a[1];
    dp[2] = a[2];

    for(int i = 3; i < n; i++)
    {
        dp[i] = min({dp[i-1], dp[i-2], dp[i-3]}) + a[i];
    }
    cout << min({dp[n-1], dp[n-2], dp[n-3]}) << endl;
    return 0;
}

/*
When making comparisons of elements in data structures,
specifically the array data structure, remember to wrap
the elements in brackets in order for the min function
to work properly.

Also initializing multiple variables in one line, requires
that each variable have a starting value, or else c++ will
give it a random value of its respective type.
*/