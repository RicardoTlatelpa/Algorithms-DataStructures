#include<iostream>
using namespace std;


float square_root(int N, int P)
{
    int s = 0;
    int e = N;
    float ans = 0;
    
    // Binary Search(Search Space 0...N)    
    while(s <= e){
        int mid = (s + e)/2;
        if(mid * mid == N){
            return mid;
        }
        else if(mid * mid < N){
            ans = mid;
            s = mid + 1;
        }else {
            e = mid - 1;
        }
    }    
    
    // Linear search(for floating part) - precision
    float inc = 0.1;
    for(int place = 1; place <= P; place++){
        while(ans * ans <= N){
            ans += inc;            
        }
        ans = ans - inc;
        inc = inc/10.0;
    }
    return ans;
}

int main()
{
    int n,p;
    cin >> n >> p;
    cout << square_root(n,p) << endl;
    return 0;
}

/*
Notes:
when working with different types of data in C++, make sure to
use the proper syntax of that data type or else the expected result
won't show.

I tried calculating 0.1, 0.01 by using powers of 10 
but this required more work than intended.

Instead I could have started the incrementation of 0.1
with 0.1 and incremented until the last digit 9
once 0.9 was reached, 10^-1 position was found and since
the original incrementation of 0.1 was not effected or changed
I can changed 0.1 into 0.01 simply by dividing the original 
incrementation memory by /10.0. and could have repeated this 
process easily with a loop of size P, where P is the desired
precision from the user's input.

*/