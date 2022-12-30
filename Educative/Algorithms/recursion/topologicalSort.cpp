#include <iostream>
#include <vector>
class Graph{
    public:
   
    Graph(int n){ //creation of adjacency list
        this->numberOfVertices = n;
        for(int i = 0; i <= n; i++){
            std::vector<int> edgesTemp;
            vertices.push_back(edgesTemp);
        }
    }
    
    void addEdge(int v, int i){
        if(v > numberOfVertices || v < 0){
           std::cout << "Vertex does not exist" << std::endl;
           return;
        }
        vertices[v].push_back(i);
    }

    void printGraph(){
        for(int i = 1; i <= this->numberOfVertices; i++){
            std::cout << i << ": ";
            std::vector<int> edges = this->vertices[i];
            for(int j = 0; j < edges.size(); j++)
            {
                if(j < edges.size()-1){
                    std::cout << edges[j] << ",";
                }else{
                    std::cout << edges[j] << " ";
                }                
            }
            std::cout << std::endl;
        }
    }

    void topologicalSortUtil()
    {

    }
    std::vector<int> topologicalSort()
    {
        std::vector<int> stack;
        std::vector<bool> visited;
        int i,j;
        for(i = 0; i <= this->numberOfVertices; i++)
        {
            visited[i] = false;
        }
    }

    private:
    int numberOfVertices;
    std::vector<std::vector<int>> vertices;

};


int main(){
    Graph myGraph(8);
    myGraph.addEdge(1,3);
    myGraph.addEdge(1,2);
    myGraph.addEdge(3,4);
    myGraph.addEdge(5,6);
    myGraph.addEdge(6,3);
    myGraph.addEdge(3,8);
    myGraph.addEdge(8,11);
    myGraph.printGraph();
    return 0;
}
