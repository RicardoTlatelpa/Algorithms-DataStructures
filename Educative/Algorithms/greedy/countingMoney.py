def find_min_coins_util(v, coins, res):
    if v == 0:
        return res
    i = len(coins) - 1
    while(coins[i] > v):
        i-=1
    v = v - coins[i]
    res.append(coins[i])
    return find_min_coins_util(v,coins, res)
    

def find_min_coins(v, coins_available):
   largest_coins = []
   largest_coins = find_min_coins_util(v,coins_available,largest_coins)
   return largest_coins

print(find_min_coins(19, [1,5,10,25]))
