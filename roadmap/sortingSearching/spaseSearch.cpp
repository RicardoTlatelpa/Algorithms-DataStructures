#include<iostream>
#include<vector>
#include<string>
using namespace std;

int sparseSearch(vector<string> ip, int s, int e, string key){    
    if(s <= e){
        int mid = (s + e)/2;
        if(ip[mid] == ""){
            // linear search for the nearest non-empty string
            int l = mid - 1;
            int r = mid + 1;
            while(l >= s && r < e){
                if(ip[l] != ""){
                    mid = l;
                    break;
                }
                if(ip[r] != ""){
                    mid = r;
                    break;
                }
            
                l -= 1;    
                r += 1;
            }
        }
        if(key > ip[mid]){
            return sparseSearch(ip, mid + 1, e, key);
        }
        else if (key < ip[mid]){
            return sparseSearch(ip, s, mid - 1, key);
        }
        else{
            return mid + 1;
        }        
    }
    else{
        return -1;
    }
}


int main()
{   
    vector<string> test = {"ai", "","","bat","","","car","cat","","","dog",""};
    cout << sparseSearch(test, 0, test.size(), "dog") << endl;
    return 0;
}