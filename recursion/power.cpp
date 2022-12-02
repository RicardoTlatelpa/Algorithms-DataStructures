#include<iostream>
using namespace std;

int paower(int m, int n)
{
    if(n == 0){
        return 1;
    }
    else if(n % 2 == 0)
    {
        paower(m*m, n/2);
    }
    else{
        m * paower(m*m, (n-1)/2);
    }
}

int power(int m, int n)
{
    if(n == 0)
        return 1;
    return power(m, n-1) * m;
}

int main(){
    int r = power(2,9);
    cout << r << endl;
    return 0;
}