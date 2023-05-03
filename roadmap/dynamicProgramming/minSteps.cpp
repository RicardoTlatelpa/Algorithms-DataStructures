#include <iostream>

using namespace std;
const int N = 1e5;

int memo[N];
int dp(int n){
  if (n==1) return 0;
  int &ans = memo[n];

  if(ans!=-1) return ans;

  ans=INT_MAX;
  
  if (n % 2 == 0){
    ans = min(ans,dp(n/2));
  }
  if (n%3 == 0){
    ans = min(ans,dp(n/3));
  }
  ans = min(ans,dp(n-1));

  return ans;
}

int main(){

  int n;
  cout << "Please enter a value: " << endl;
  cin >> n;
  cout << "value you have entered: " << n << endl;
  cout << dp(n) << endl;
}
