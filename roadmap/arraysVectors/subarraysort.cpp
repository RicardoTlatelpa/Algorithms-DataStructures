#include<iostream>
#include<vector>
#include<string>
using namespace std;


void solution(vector<int> input)
{
    vector<int> s; // O(1) solution memory
    for(int i = 0; i < input.size() - 1; i++) // average case is O(N), best case is O(N) and worst case O(N^2) 
    {
        if(input[i] > input[i + 1]){
            s.push_back(i);
            int number_looking_for = input[i] - 1;            
            while(s.size() < 2){
                int traverse = i;
                while(traverse < input.size()){
                    if(input[traverse] == number_looking_for){
                        s.push_back(traverse);
                    }
                    traverse+=1;                    
                }
                // find next possible sorted number
                number_looking_for-=1;
            }
            break;
        }
    }
    
    if(s.size() == 0){
        cout << -1 << " " << -1 << endl;
    }
    else{
        cout << s[0] << " " << s[1] << endl;
    }
}

int main(){
    vector<int> a1 = {1,2,3,4,5,6,6,7,9,10,11};
    solution(a1);
    return 0;
}