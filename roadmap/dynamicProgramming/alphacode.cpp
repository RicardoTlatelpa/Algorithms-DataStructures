#include <iostream>
using namespace std;

string s;

int dp(int index){

  int ans = 0;
  if(index == s.size()) return 1;

  if(s[index] >= '1' && s[index] <= '9') {
    ans += dp(index + 1);
  }

  if(index + 1 < s.size() && s[index] == '1'){
    ans += dp(index+2); 
  }

  if (index + 1 < s.size() && (s[index] == '2' && s[index+1] <= '6')){
    ans += dp(index + 2);
  }

  return ans;

}

int main(){
  int w;
  cin>>s;
  while(1){
    cin >> s;
    if(s[0] == '0') break;
  
    cout << dp(0) << endl;
  }

  return 0;
}
