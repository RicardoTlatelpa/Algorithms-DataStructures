#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;

string unique_substring(string str){
    int i =0;
    int j = 0;
    int window_len = 0;
    int max_window_len = 0;
    int start_window = -1;
    unordered_map<char,int> m;
    while(j < str.length()){
        char ch = str[j];
        if(m.count(ch) and m[ch] >= i){
            //later on...
            i = m[ch] + 1;
            window_len = j - i;
        }
        // update the last occ
        m[ch] = j;
        window_len++;
        j++;

        // update max_window_len at every step
        if(window_len > max_window_len){
            max_window_len = window_len;
            start_window = i;
        }
    }
    return str.substr(start_window,max_window_len);
}
