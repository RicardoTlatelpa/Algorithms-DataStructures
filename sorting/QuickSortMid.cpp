#include<iostream>
using namespace std;


void quickSort(int arr[], int left, int right)
{
    int i = left, j = right;
    int tmp;
    int pivot = arr[(left + right)/2];
    // partition
    while(i <= j)
    {
        while(arr[i] < pivot){i++;}
        while(arr[j] > pivot){j--;}
        if(i <= j)
        {
            auto temp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    }
    if(left < j)
        quickSort(arr, left, j);
    if(right < right)
        quickSort(arr, i, right);
}

int main()
{
    return 0;
}