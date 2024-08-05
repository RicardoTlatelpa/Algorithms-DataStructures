class DisjointSet:
    def __init__(self,n):
        self.rank = [0] * (n+1)
        self.parent = [0] * (n+1)
        self.size = [0] * (n+1)

        for i in range(n+1):
            self.parent[i] = i

        def findUPar(self,node):
            if node == self.parent[node]:
                return node
            self.parent[node] = self.findUPar(self.parent[node])
            return self.parent[node]

        def unionByRank(self,u,v):
            ulp_u = self.findUPar(u)
            ulp_v = self.findUPar(v)
            if ulp_u == ulp_v:
                return
            if self.rank[ulp_u] < self.rank[ulp_v]:
                self.parent[ulp_u] = ulp_v
            elif self.rank[ulp_v] < self.rank[ulp_u]:
                self.parent[ulp_v] = ulp_u
            else:
                self.parent[ulp_v] = ulp_u
                self.rank[ulp_u]+=1

        def unionBySize(self,u,v):
            ulp_u = self.findUPar(u)
            ulp_v = self.findUPar(v)
            if ulp_u == ulp_v:
                return
            if self.size[ulp_u] < self.size[ulp_v]:
                self.parent[ulp_u] = ulp_v
                self.size[ulp_v] += self.size[ulp_u]
            else:
                self.parent[ulp_v] = ulp_u
                self.size[ulp_u] += self.size[ulp_v]
def main():
    ds = DisjointSet(7)
    ds.unionByRank(1,2)
    ds.unionByRank(2,3)
    ds.unionByRank(4,5)
    ds.unionByRank(6,7)
    ds.unionByRank(5,6)
    if(ds.findUPar(3) == ds.findUPar(6)):
        print("True")
    else:
        print("Not true; Striver is the best")
    ds.unionByRank(3,6)
