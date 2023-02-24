#include<iostream>
#include<vector>
using namespace std;

int highest_mountain(vector<int> a){
    int n = a.size();
    int largest = 0;
    for(int i = 1; i <= n -2; ){
        // check a[i] is peak or not
        if(a[i] > a[i-1] and a[i] > a[i+1]){
            // do some work
            int cnt = 1;
            // count backwards(left)
            int left = i-1;
            while(left >= 1 and a[left] > a[left - 1]){
                left++;
                cnt++;
            }
            // count forwards(right)
            while(i <= n - 2 and a[i] > a[i + 1]){
                i++;
                cnt++;
            }                       
        }
        else{
            i++;
        }
    }
    return largest;
}

int main()
{
    vector<int> arr{5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4};
    cout << highest_mountain(arr);
    return 0;
}