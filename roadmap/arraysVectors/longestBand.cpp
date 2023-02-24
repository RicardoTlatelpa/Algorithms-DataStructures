#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

int longestChain(vector<int> arr){
    int n = arr.size();
    unordered_set<int> s;
    // O(N) operation, building the set...
    for(int x: arr){
        s.insert(x);
    }
    int largest_length = 0;
    // Iterate over the array
    
    for(auto element : s){
        int parent = element - 1;
        cout << "Current element: " << element << endl;        
        if(s.find(parent)==s.end()) // if parent of current element not found in unordered set
        {
            int next_no = element + 1;
            int cnt = 1;
            while(s.find(next_no) != s.end()){ // if next element found in ordered_set continue looping
                next_no++;
                cnt++;
            }
            if(cnt > largest_length){
                largest_length = cnt;
            }
        }
    }
    return largest_length;
}


int main()
{
    vector<int> v = {1,9,3,0,18,5,2,4,10,7,12,6};
    cout << longestChain(v) << endl;
    return 0;
}