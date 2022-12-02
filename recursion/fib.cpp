#include <iostream>
#include <vector>
using namespace std;

int fib(int n){    
    static vector<int> f(n, -1); // fill n slots with -1, [-1,-1,-1,...,n]
    if(n <= 1){
        f[n] = n;
        return f[n];
    }
    else{
        if(f[n-2] == -1)
        {
            f[n-2] = fib(n-2);
        }
        if(f[n-1] == -1)
        {
            f[n-1] = fib(n-1);
        }
        return f[n-2] + f[n-1];
    }
}

int main()
{
    cout << fib(5) << endl;
    return 0;
}