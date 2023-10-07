#include<iostream>
#include<vector>
using namespace std;


class DisjointSet {
  vector<int> rank, parent;
public:
  Disjoint(int n){
    rank.resize(n+1,0);
    parent.resize(n+1)
    for(int i = 0; i <= n; i++){
      parent[i] = i;
    }
  }
  int findUPar(int node){
    if(node == parent[node]){
      return node;
    }
    return parent[node] = findUParent(parent[node]);
  }

  void unionByRank(int u, int v){
    int ulp_u = findUPar(u);
    int ulp_v = findUPar(v);
    if(ulp_u == ulp_v) return; // same parent
    if(rank[ulp_u] < rank[ulp_v]) {
      // higher rank gets the connection and gets to be the parent
      parent[ulp_u] = ulp_v;
    }
    else if(rank[ulp_v] < rank[ulp_u]){
      parent[ulp_v] = ulp_u;
    }
    else {
      // if their rank is equal, u becomes the parent and v is now connected
      // vector u's rank increases by 1 due to its connection
      parent[ulp_v] = ulp_u;
      rank[ulp_u]++;
    }
  }
};
