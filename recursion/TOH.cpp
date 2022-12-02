#include <iostream>
using namespace std;

//static int totalCalls = 1;
void TOH(int n, int A, int B, int C)
{    
    
    if(n > 0){
        TOH(n-1, A,C,B);
        printf("(%d,%d)\n",A,C);// from-to
        TOH(n-1, B,A,C);
    }
}

int main()
{
    TOH(16,1,2,3);
    return 0;
}