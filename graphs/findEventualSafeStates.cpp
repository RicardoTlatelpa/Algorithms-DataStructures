#include <iostream>
#include <vector>
using namespace std;

class Solution {
  private:
  bool dfsCheck(int node, vector<int> adj, vector<int> vis, vector<int> pathVis, vector<int> check){
      vis[node] = 1;
      pathVis[node] = 1;
      for(auto it : adj[node]){
        // depth first search recursive call
        if(!vis[it]){
          if(dfsCheck(it,adj,vis,pathVis) == true){
            // if cycle detected from recursive call
            check[node] = 0;
            return true;
          }
        }
        // cycle detected
        else if(pathVis[it]){
          return true;
        }
      }
      // no cycles detected while traversing its neighbors
      pathVis[node] = 0;
      return false;
    }

  public:
  vector<int> eventualSafeNodes(int V, vector<int> adj){
      // code here
      vector<int> vis(V,0);
      vector<int> pathVis(V,0);
      vector<int> check(V,0);
      vector<int> safeNodes = {};
      // assuming graph input are graph components
      for(int i = 0; i < V; i++){
        if(!vis[i]){
          dfsCheck(i,adj,vis,pathVis);
        }
      }
      for(int i = 0; i < V; i++){
        if (check[i] == 1) safeNodes.push_back(i);
      }
      return safeNodes;
  }  
};


int main(){
  return 0;
}
