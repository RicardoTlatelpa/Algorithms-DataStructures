#include<iostream>
using namespace std;

void InsertionSort(int a[], int size)
{
    for(int i = 1; i < size; i++)
    {
        int j;
        int k = a[i];
        for(j = i-1; j >= 0; j--)
        {
            if(a[j] < k)
            {
                break;
            }else {
                a[j + 1] = a[j];// shift elements
            }
        }
        a[j + 1] = k; 
    }
}


int main()
{
    int a[15] = {7,8,10,2,6,4,11,5,3,12,13,26,16,19};
    InsertionSort(a, 15);
    for(int i = 0; i < 15; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}