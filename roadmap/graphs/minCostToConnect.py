import heapq


class Solution:
    def minCostConnectPoints(self,points):
        adj_list = {i:[] for i in range(len(points))} # i: list of [cost, node]
        # building the adjacency list
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i + 1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append([dist,j])
                adj_list[j].append([dist,i])

        visit = set()
        minHeap = []
        result = 0
        # traverse through the adjacency list 
        # 1. using the heap to get the shortest cost(greedy/dijkstra approach)
        # 2. visit set used to avoid infinte traversals
        
        heapq.heappush(minHeap, [0,0])

        # goal: every point on the input will get the shortest nearest point
        while(len(visit) < len(points)):
            cost,i = heapq.heappop(minHeap)
            if i in visit:
                continue
            result += cost
            visit.add(i)
            for neicost, nei in adj_list[i]:
                if nei not in visit:
                    heapq.heappush(minHeap,[neicost,nei])
        return result


# Testing function
s = Solution()

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s.minCostConnectPoints(points)

