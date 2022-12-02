#include<iostream>
using namespace std;

int f(int &x, int c){
    cout << "( " << x << ", " << c << " )" << endl;
    c = c-1;
    if(c==0) return 1;
    x = x + 1;
    return f(x,c)*x;   
}

int main(){
    int p = 5;

    cout << f(p,p) << endl;
    return 0;
}