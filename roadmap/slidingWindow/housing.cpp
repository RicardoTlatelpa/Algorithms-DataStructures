#include<iostream>
#include<vector>
using namespace std;
/*
Housing problem

Input: a sequence of plots of land and each index contains an area of land, 
an integer k, telling us how much area of land we want

Output: a pair of continguous indices telling us what subarray of the input 
area would sum to the amount of land we want
*/

vector<pair<int,int>> housing(vector<int> plots_of_land, int k)
{
    vector<pair<int,int>> results;
sda:    int i = 0;
    int j = 1;
    int sum = plots_of_land[0];
    while(j < plots_of_land.size() && i < j){
        cout << "index i: " << i << endl;
        cout << "index j: " << j << endl;
        sum += plots_of_land[j];
        if(sum < k){
            j+=1;
        }
        else if(sum > k){
            sum -= plots_of_land[i];
            i += 1;
        }
        if(sum == k){
            cout << "sum == k" << endl;
            results.push_back({i,j});
            i+=1;
        }
    }
    cout << results.size() << endl;
    return results;
}

int main()
{
    vector<int> plots_of_land = {1,3,2,1,4,1,3,2,1,1,2};
    vector<pair<int,int>> answer = housing(plots_of_land,8);
    for(int i = 0; i < answer.size(); ++i){
        cout << answer[i].first << "-" << answer[i].second << endl;
    }
    return 0;
}
