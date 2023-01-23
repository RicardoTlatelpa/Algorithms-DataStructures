#include <iostream>
using namespace std;

bool isSafe(int mat[][9], int i , int j, int no, int n)
{
    // check for row and col
    for(int k = 0; k < n;k++)
    {
        if(mat[k][j] == no || mat[i][k] == no)
        {
            return false;
        }
    }
    // check for subgrid
    int sx = (i / 3) * 3;
    int sy = (j / 3) * 3;

    for(int x = sx; x < sx + 3; x++){
        for (int y = sy; y < sy + 3; y++)
        {
            if(mat[x][y] == no){
                return false;
            }
        }
    }
    return true;
}

bool solveSodoku(int mat[][9], int i, int j, int n)
{
    //base case
    if(i == n){
        //print the solution
        for(int row = 0; row < 9; row++){
            for(int col = 0; col < 9; col++)
            {
                cout << mat[row][col] << " ";
            }
            cout << endl;
        }
        return true;
    }
    //recursive case
    if(j == n){
        return solveSodoku(mat, i + 1, 0, n);
    }
    // skip the prefilled cell
    if(mat[i][j] != 0){
        return solveSodoku(mat, i, j+1, n);
    }
    for(int no = 1; no <= n; no++)
    {
        if(isSafe(mat,i,j,no,n)){
            mat[i][j] = no;
            bool solveSubproblem = solveSodoku(mat, i, j+1, n);
            if(solveSubproblem == true){
                return true;
            }

        }
    }
    // backtracking step
    mat[i][j] = 0;
    return false;
}

int main(){
    int n = 9;
    int mat[9][9] = 
    {
        {5,3,0,0,7,0,0,0,0},
        {6,0,0,1,9,5,0,0,0},
        {0,9,8,0,0,0,0,6,0},
        {8,0,0,0,6,0,0,0,3},
        {4,0,0,8,0,3,0,0,1},
        {7,0,0,0,2,0,0,0,6},
        {0,6,0,0,0,0,2,8,0},
        {0,0,0,4,1,9,0,0,5},
        {0,0,0,0,8,0,0,7,9}
    };

    if(!solveSodoku(mat,0,0,n)){
        cout << "sodoku not solvable" << endl;
    }
}