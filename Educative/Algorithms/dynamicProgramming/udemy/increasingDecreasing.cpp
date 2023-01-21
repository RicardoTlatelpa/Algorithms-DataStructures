#include<iostream>

void increasingDecreasing(int arr[], int n, int i){
    if (i == n){
        return;
    }
    std::cout << "increasing: " << arr[i] << std::endl; // before recursive call
    increasingDecreasing(arr, n, i+1);
    std::cout << "decreasing: " << arr[i] << std::endl; // recursive call back
}

void inc(int n){
    if (n < 0){
        return;
    }

    inc(n -1);
    std::cout << n << std::endl;
}
void dec(int n){
    if (n < 0) {
        return;
    }
    std::cout << n << std::endl;
    dec(n-1);
}


int main(){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    //increasingDecreasing(arr, 10, 0);
    inc(10);
    std::cout << "Decreasing now:~!" << std::endl;
    dec(10);
    return 0;
}