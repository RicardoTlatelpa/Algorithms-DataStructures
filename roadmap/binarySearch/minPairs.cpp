#include<iostream>
#include<vector>
using namespace std;

int absolute_value(int n){
    if(n < 0){
        return -1 * n;
    }else{
        return n;
    }
}

pair<int,int> findMinPair(vector<int> a1, vector<int> a2){
    pair<int,int> smallest_pair{INT_MAX, INT_MAX};
    int s1 = 0,s2 = 0;
    int e1 = a1.size()-1, e2 = a2.size()-1;

    while(s1 <= e1){
        int mid1 = (s1 + e1)/2;
        int mid2 = (s2 + e2)/2;
        if(s1 == e1){            
            //perform binary search of second array
            smallest_pair.first = a1[mid1];
            int smallest_difference = absolute_value(smallest_pair.first - a2[mid2]);
            while(s2 <= e2){
                int traversing_mid = (s2 + e2)/2;

                if(a2[traversing_mid] > smallest_pair.first){                    
                    e2 = traversing_mid - 1;
                    // compute difference
                    int current_diff = absolute_value(smallest_pair.first - a2[traversing_mid]);
                    // compare to pair
                    if(current_diff < smallest_difference){
                        // update second index in pair
                        smallest_difference = current_diff;
                        smallest_pair.second = a2[traversing_mid];
                    }                                        
                }
                else if(a2[traversing_mid] < smallest_pair.first){
                    s2 = traversing_mid + 1;
                    int current_diff = absolute_value(smallest_pair.first - a2[traversing_mid]);
                    if(current_diff < smallest_difference){
                        smallest_difference = current_diff;
                        smallest_pair.second = a2[traversing_mid];
                    }
                }
                else{
                    smallest_pair.second = a2[traversing_mid];
                    return smallest_pair;
                }
            }
        }
        if(a1[mid1] < a2[mid2]){
            s1 = mid1 + 1;
        }
        else if(a1[mid1] > a2[mid2]){
            e1 = mid1 - 1;
        }
        else{
            smallest_pair.first = a1[mid1];
            smallest_pair.second = a2[mid2];
            return smallest_pair;
        }
    }
    return smallest_pair;
}


int main(){
    vector<int> a1{-1,5,10,20,3};
    vector<int> a2{26,134,135,15,17};
    sort(a1.begin(), a1.end());
    sort(a2.begin(),a2.end());
    pair<int,int> answer = findMinPair(a1,a2);
    cout << "[" << answer.first << "," << answer.second << "]" << endl;
    return 0;
}