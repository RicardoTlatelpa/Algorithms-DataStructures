#include<iostream>
#include<climits>
#include<string>
using namespace std;

string stringWindow(string s, string p){
    //Array as a Freq Map or you can hashmap
    int FP[256] = {0};
    int window[256] = {0};
    for(int i = 0; i < p.length();i++){
        FP[pat[i]]++;
    }
    int cnt = 0;
    //Sliding Window Algorithm
    for(int i = 0; i < s.length();i++){
        //expand the window by including curr char
        FS[s[i]]++;
    
    }
}

int main(){
    string s,p;
    cin >> s >> p;
    cout << find_window(s,p) << endl;
    return 0;
}
