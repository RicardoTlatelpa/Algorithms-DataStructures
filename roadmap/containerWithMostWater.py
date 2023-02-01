class Solution:
    def maxArea(self, height):
        # BRUTE FORCE
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)
        return res 
    def maxArea_optimized(self,height):
        l = 0
        r = len(height) - 1
        max_area = 1
        while (l < r):
            width = abs(r-l)
            cHeight = min(height[l],height[r])
            area = width * cHeight
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        """
        In this solution, we want to keep the maximum height in each traversal of the heights
        Since the minimum height affects the area the most as we iterate through the list, it is 
        best to keep the largest height possible as we traverse further through the input list
        """
