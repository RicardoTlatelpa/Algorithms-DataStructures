#include <iostream>

long binom_co(int n, int m)
{
    int i, j;
    std::cout << n << " " << m << std::endl;
    long bc[n][n];
    for(i = 0; i <= n; i++) bc[i][0] = 1;
    for(j = 0; j <= n; j++) bc[j][j] = 1;
    for(i = 1; i <= n; i++)
        for (j = 1; j < i; j++)
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j];
            
    for(int k = 0; k < n; k++)
        for(int d = 0; d < n; d++)
            std::cout << bc[k][d];
        std::cout << std::endl;
  
    return (bc[n][m]);
}

int main(){
    long answer = binom_co(5,4);
    std::cout << answer << std::endl;
    return 0;
}