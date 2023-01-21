#include <iostream>
using namespace std;

int power(int b, int e)
{
    if(e == 0)
    {
        return 1;
    }
    return b * power(b,e - 1);
}
/*
Is there any other way to break the power function?

*/

int power_faster(int b, int e)
{
    if (e == 0)
    {
        return 1;
    }
    int subProb = power_faster(b, e/2);
    int subProbSq = subProb * subProb;
    if(e&1){
        return b * subProbSq;
    }
    return subProbSq;
}


int main()
{
    int answer = power(10,3);
    cout << answer << endl;
    return 0;
}