#include<iostream>
#include<vector>
using namespace std;

int find_captured_water(vector<int> heights){
    int counter = 0;
    vector<int> left(heights.size(), 0);
    vector<int> right(heights.size(), 0);
    
    int largest_height = -1;
    for(int i = 0; i < heights.size(); i++){
        int height = heights[i];
        if (height > largest_height){
            largest_height = height;
        }
        left[i] = largest_height;
    }
    
    largest_height = -1;
    for(int i = heights.size()-1; i >= 0; i--){
        int height = heights[i];
        if(height > largest_height){
            largest_height = height;
        }
        right[i] = largest_height;
    }

    for(int idx = 0; idx < heights.size(); idx++){
        int current_min;
        if(left[idx] <= right[idx]){
            current_min = left[idx];
        }else{
            current_min = right[idx];
        }
        counter += (current_min - heights[idx]);
    }
    return counter;
}

int main(){
    vector<int> heights{0,1,0,2,1,0,1,3,2,1,2,1};
    cout << find_captured_water(heights) << endl;
    return 0;
}