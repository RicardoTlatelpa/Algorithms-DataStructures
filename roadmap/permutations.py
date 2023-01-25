"""
Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.
"""

class Solution(object):
    def permute(self, nums):
        """        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if(len(nums) == 1):            
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

mySolution = Solution()

print(mySolution.permute([1,2,3]))