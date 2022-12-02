#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &array, int l, int r){
   
    int pivot = l;
    if(l == r){
        // 1 element case
        return pivot;
    }
    int i = l; // left hand side pointer
    int j = r; /// right hand side pointer
    // Arrange elements so that elements greater than pivot
    // are in right hand side, and less than pivot elements
    // are in the left hand side
    while(i < j){          
        while(array[i] <= array[pivot]){i++;}
        while(array[j] > array[pivot]){j--;}
        if(i < j){
            auto temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }   
    }
    auto temp = array[l];
    array[l] = array[j];
    array[j] = temp;
    return j;
}

void quickSort(vector<int> &array, int l, int r)
{
    if(l < r){
        int pivot = partition(array, l, r);
        quickSort(array, l, pivot - 1);
        quickSort(array, pivot + 1,  r);
    }
    

}

int main(){
    vector<int> array = {50,40,30,20,90,70,80};
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << " ";
    }
    cout << endl;
    quickSort(array, 0, array.size() - 1);
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << " ";
    }
    cout << endl;
    return 0;
}
