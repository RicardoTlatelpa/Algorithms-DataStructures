#include <iostream>
using namespace std;

int fun1(int n){
    if(n > 0)
    {
        return fun1(n-1) + n;
    }
    return 0;
}


int main(){
    int r;
    r = fun1(5);
    printf("%d", r);
    return 0;
}