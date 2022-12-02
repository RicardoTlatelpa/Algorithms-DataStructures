#include<iostream>

using namespace std;

void selectionSort( int (&array)[6], int k ){ // where k are the number of passes
   for(int i = 0; i < k; i++){
        int j = i;
        int k = i;
        while( j < 6 ){
            if(array[j] < array[k]){
                k = j;
            }
            j++;
        }
        if(j != k){
            int temp = array[i];
            array[i] = array[k];
            array[k] = temp;
        }
   }
}
int main(){
    int array[6] = {8,6,3,2,5,4};
    selectionSort(array, 6);
    for(auto i = 0; i < 6; ++i){
        cout << i << " ";
    }

    cout << endl;
    return 0;
}
