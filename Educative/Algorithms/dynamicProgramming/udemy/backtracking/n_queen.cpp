#include<iostream>
#include<vector>
using namespace std;

/*
N-Queen is the problem of placing N chess queens 
on an NxN chessboard so that no two queens attack each other.
*/
void printBoard(vector<vector<int>> board){
    for(int row = 0; row < board.size(); row++)
    {
        for(int col = 0; col < board[row].size();col++){
            cout << board[row][col] << " ";
        }
        cout << endl;
    }
}
bool queen_move(vector<vector<int>> &board, int row, int col){
    int i = row;
    int j = col;
    //up
    while(i >= 0){        
        if(board[i][j] == 1 && i!=row){
            return true;
        } 
        i--;
    }
    //down
    i = row;
    while(i < board.size()){        
        if(board[i][j] == 1 && i!=row){
            return true;
        }
        i--;
    }
    //left
    i = row;
    while(j >= 0){
        if(board[i][j] == 1 && j != col){
            return true;
        }
        j--;
    }
    //right
    j = col;
    while(j < board.size()){
        if(board[i][j] == 1 && j != col){
            return true;
        }
        j++;
    }    
    //diagnol-left
    j = col;    
    while(i >= 0 && j >= 0){
        if(board[i][j] == 1 && (i != row && j!= col)){
            return true;
        }
        i-=1;
        j-=1;
    }
    //diagnol-right
    i = row;
    j = col;
    while(i < board.size() and j < board.size()){
        if(board[i][j] == 1 && (i != row && j!= col)){
            return true;
        }
        i+=1;
        j+=1;
    }
    
    return false; // no queen detected
}


bool nQueens_rec(vector<vector<int>> &board, int row)
{
    if(row == board.size()){
        printBoard(board);
        return true;
    }

    while(row < board.size())
    {
        int cols = 0;
        while(cols < board.size()){
            // filling entry for queen
            bool detect = queen_move(board, row, cols);
            if(detect == false){
                board[row][cols] = 1;
                bool rec = nQueens_rec(board, row + 1);
                if(rec == true){
                    return true;
                }                
            }
            board[row][cols] = 0;            
        }
    }
    return false;
}


void nQueens(vector<vector<int>> board){
    // if queen doesn't touch any other queen
    nQueens_rec(board,0);
}



int main()
{
    int N = 4;
    vector<int> row(N, 0);
    vector<vector<int>> board(N, row);
    nQueens(board);
    cout << "N Queens = 4" << endl;
    printBoard(board);
    return 0;
}