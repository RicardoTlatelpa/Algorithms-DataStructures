#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;
/*
Given a string, write a function to find the 
largest substring with unique characters
(no duplicates)
*/

string unique_substring(string s)
{
    string largest_substring = "";
    int j = 0;
    string current_substring = "";
    map<char,int> dictionary;
    int i = 0;
    while(j < s.size()){               
        if(dictionary.count(s[j]) == 1){            
            if(current_substring.size() > largest_substring.size()){
                largest_substring.assign(current_substring);
            }
            current_substring = "";
            dictionary.clear();            
            i = j;
        }
        dictionary[s[j]] = 1;
        current_substring += s[j];
        j++; 
    }
    return largest_substring;
}


int main()
{
    cout << unique_substring("aaaaabc") << endl;
    return 0;
}
