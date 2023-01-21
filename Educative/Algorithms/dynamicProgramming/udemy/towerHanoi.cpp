#include <iostream>

using namespace std;

void TowerOfHanoi(int n, char from, char helper, char to)
{
    if(n == 0) return;
    TowerOfHanoi(n-1, from, to, helper);
    // reached here
    // nth rod to to
    cout << from << "->" << to << '\n';
    TowerOfHanoi(n-1, helper, from, to);
}

int main()
{
    TowerOfHanoi(1, 'A', 'B', 'C');
    return 0;
}