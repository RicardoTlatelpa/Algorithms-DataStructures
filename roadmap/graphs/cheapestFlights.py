class Solution:
    def findCheapestPrice(self,n,flights,src,dst,k):
        # we're going to implement bellman-ford's algorithm
        # O(E*K) time complexity

        prices = [float("inf")]*n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s,d,p in flights: # s=source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst] 

