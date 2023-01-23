#include<iostream>
#include<string>
using namespace std;

/*
With this recursive function we are leading the recursive statement into the right direction
by keeping track of the length of our generate string we output the proper base case string

by keeping track of how many open and closing paranthesis we have, we can generate two paths for each
recursive call, a path where 
*/

void generateBrackets(string output, int n, int open, int close, int i){
    if(i == 2*n){
        cout << output << endl;
        return;
    }
    if(open < n){
        generateBrackets(output + '(', n, open + 1, close, i + 1);
    }
    
    if(close < open){
        generateBrackets(output + ')',n, open, close + 1, i + 1);
    }
}


int main()
{
    string output;
    int n;
    cin >> n;
    generateBrackets(output, n, 0,0,0);
    return 0;
}


/*

I noticed with recursion that there are two types of problems that can occur when passing memory
down the recursive call stack.

If the datastructure is something like an array or a matrix, that is perfect for storing 
continguos memory, memory that won't be deleted from or forgotten about in future stack frames.

However, if the data structure is just a simple primitive data structure like an int or a char,
the data structure will change with the stack frame.

Depending on the context of the problem, in this case concatanating strings, future strings will require
different chars at different future stack frames.

In order to combat this and have the primitive data structure 'effect' with a string or array type data structure
you must purposefully pop from the array or delete the last appended element from the data structure.

This in turn will have a permutation effect, and when the base case is hit, the desired result will be the
outcome

So be aware of how data structures are being affected when they are passed recursively, and the desired result
in a specific context.
*/