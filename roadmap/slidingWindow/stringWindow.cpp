#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;
/*
String Window
Given two strings, one big string and one small string, find the 
'smallest window' in the big string that contains all characters of 
the small string.

- Window can have additional characters than required
- If small string has duplicates, then those duplicates
must be present with same or higher count in window.
*/

string string_window(string s1, string s2){
    
    int smallest_window = -1;
    int largest_window = -1;
    int smallest_window_size = INT_MAX;
    unordered_map<char,int> m2;
    for(int i = 0; i < s2.size(); ++i){
        if(!m2.count(s2[i])){
            m2[s2[i]] = 1;
        }else{
            m2[s2[i]] += 1;
        }
        
    }
    
    for(int i = 0; i < s1.size(); ++i){
        char current_char = s1[i];
        
        if(m2.count(current_char)){
            // begin window
            unordered_map<char,int> tempHash;
            int window_size = 0;
            int j = i;
            while(j < s1.size()){
                char window_char = s1[j];
                if(m2.count(window_char) > 0){
                    if(!tempHash.count(window_char)){
                        tempHash[window_char] = 1;
                    }else{
                        tempHash[window_char] += 1;                        
                    }
                }

                if(tempHash == m2){
                    if(window_size < smallest_window_size){
                        smallest_window = i;
                        largest_window = j;
                    }
                    break;
                }
                window_size +=1;
                j+=1;
            }
        }    
    }
    return s1.substr(smallest_window,largest_window);
}

int main(){

    string s1 = "hello_world";
    string s2 = "lol";
    cout << string_window(s1,s2) << endl;
    return 0;
}