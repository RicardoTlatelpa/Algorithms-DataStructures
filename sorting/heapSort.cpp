#include<iostream>
using namespace std;

void Insert(int A[], int n)
{
    int i = n, temp;
    temp = A[i];
    while(i > 1 && temp > A[i/2]){
        A[i] = A[i/2];
        i = i / 2;
    }
    A[i] = temp;
}

int Delete(int A[], int n)
{
    int i,j,x,val;
    val = A[1];
    x = A[n];
    A[1] = A[n];
    i=1;j=i*2;

    while(j<n-1)
    {
        if(A[j+1] > A[j])
        {
            j = j+1;
        }
        if(A[i] < A[j]){
            auto temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            i = j;
            j = 2 * j;
        }
        else {
            break;
        }
    }
    return val;
}



int main(){
    int H[] = {0,2,5,8,9,4,10,7};
    int i;
    for(i=2; i<=7; i++){
        Insert(H, i);
    }
    int t = 7;
    while( t > 0 ){
        cout << "Delete value is " << Delete(H,t) << endl;
        t--;
    }
    
    for(i = 1; i <= 7; i++){
        printf("%d ", H[i]);
    }
    cout << endl;
    return 0;
}

