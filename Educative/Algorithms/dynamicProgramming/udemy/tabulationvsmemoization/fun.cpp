#include<iostream>

using namespace std;
// number of ways to fill an array of length n
int fun(int index, int n, bool one)
{
    // either place zero
    // or place one
    if(index == n + 1){
        return 1;
    }
    int ans = 0;
    ans += fun(index + 1, n, false);
    if(one == false){
        ans += fun(index + 1, n, true);
    }
    // ans for array [index ... n]
    return ans;    
}

int main()
{   
    freopen("intput.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    for(int i = 1; i <= 10; i++){
        cout << fun(1, i, false) << endl;
    }
    return 0;
}