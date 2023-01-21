#include <iostream>

int factorial(int n){

    if(n == 0){
        return 1;
    }
    return n * factorial(n-1);
}


int main(){
    int test = 5;
    int f = factorial(test);
    std::cout << f << std::endl;
    return 0;
}