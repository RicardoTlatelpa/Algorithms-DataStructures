/*
Implementing taylor series with Horner's Rule(factoring multiplication minimization)
*/
#include <iostream>
using namespace std;

double e(int x, int n){
    static double S = 1;
    if(n == 0)
    {
        return S;
    }
    S = 1 + S/n;
    return e(x, n-1);
}

double e_linear(int x, int n)
{
    double s = 1;
    int i;
    double num = 1;
    double den = 1;

    for(i = 1; i <= n; i++)
    {
        num *= x;
        den *= i;
        s+=num/den;
    }
    return s;
}

int main()
{
    double tv = e(1,10);
    cout << tv << endl;
    return 0;
}