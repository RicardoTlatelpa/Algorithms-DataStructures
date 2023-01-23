#include<iostream>
using namespace std;

int supw_u(int days, int durations[], int skips, int i, int count)
{
    if(i >= days){
        return count;
    }
    int path1 = 1000;
    int path2 = 1000;
    if(skips < 2){
        path1 = supw_u(days, durations, skips + 1, i + 1, count);
    }    
    count += durations[i];
    path2 = supw_u(days, durations, 0, i + 1, count);
    return min(path1, path2);
}

int supw(int days, int durations[]){
    return supw_u(days, durations, 0, 0, 0);
}


int main(){
    int days = 5;
    int durations[5] = {2,2,3,2,2};
    cout << supw(days, durations) << endl;
    return 0;
}