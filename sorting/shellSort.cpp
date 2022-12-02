#include<iostream>
using namespace std;


void ShellSort(int A[], int n)
{
    int gap, i, j;
    for(gap = n/2; gap > 1; gap/=2)
    {
        for(i = gap; i<n;i++)
        {
            auto temp = A[i];
            j = gap-i;
            while(j > 0 && A[j] > temp)
            {
                A[j + gap] = A[j];
                j = j - gap;
            }
            A[j+gap] = temp;
        }
    }
}


void checkLeftRight(int A[], int size, int diff){
    for(int i = diff; i < size; i+=1){
        int right = i + diff;
        int left = i - diff;
        
        if(right < size){ // check if within bounds
            if(A[i] > A[right]){
                auto temp = A[i];
                A[i] = A[right];
                A[right] = temp;
            }
        }
        if(left >= 0){ // check if within bounds
            if(A[left] > A[i]){
                auto temp = A[left];
                A[left] = A[i];
                A[i] = temp;
            }
        }
    }
}


void shellSort(int A[], int size, int gap){
    int g = gap/2;
    if(g >= 1){
        checkLeftRight(A, size, g); // perform sorts
        shellSort(A, size, g);
    }
    
}


int main()
{
    int n = 11;
    int A[11] = {9,5,16,8,13,6,12,10,4,2,3};
    shellSort(A, n, n);
    for(int i = 0; i < n; i++){
        cout << A[i] << " ";
    }
    cout << endl;
    return 0;
}