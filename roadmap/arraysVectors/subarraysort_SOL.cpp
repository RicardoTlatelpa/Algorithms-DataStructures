#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool outOfOrder(vector<int> array, int i){
    int x = array[i];
    if(i == 0){
        return array[i] > array[i + 1];
    }
    if(i == array.size()-1){
        return array[i] < array[i - 1];
    }
    return x < array[i - 1] || x > array[i + 1];
}

pair<int,int> subarraySort(vector<int> a){
    int smallest = INT_MAX;
    int largest = INT_MIN;
    pair<int,int> result;
    for(int i = 0; i < a.size(); i++)
    {
        int x = a[i];
        if(outOfOrder(a, i)){
            smallest = min(x, smallest);
            largest = max(x,largest);
        }
    }
    if(smallest == INT_MAX){
        // we can safely assume array is sorted
        return {-1,-1};
    }

    int left = 0;
    int right = a.size()-1;
    while(smallest >= a[left]){
        left += 1;
    }
    while(right <= a[right]){
        right -= 1;
    }
    result.first = left;
    result.second = right;
    return result;
}

int main()
{
    vector<int> arr = {1,2,3,4,5,8,6,7,9,10,11};
    auto p = subarraySort(arr);
    cout << p.first << " and " << p.second << endl;
    return 0;
}