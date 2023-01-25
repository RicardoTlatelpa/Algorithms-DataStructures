"""
Subsets:
Given an integer array nums of unique elements,
return all possible subsets(the power set)
The solution set must not contain duplicate subsets.
Return the solution in any order.
"""

class Solution(object):
    def find_subsets(self, nums, lst, i, j):
        if i == len(nums) or j == len(nums):
            return -1
        if i == j:
            lst.append([nums[i]])
        elif i < j:
            lst.append([nums[i], nums[j]])
        self.find_subsets(nums, lst, i, j + 1)
        if(i == j):
            self.find_subsets(nums, lst, i + 1, i + 1)
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        answer = [[]]
        self.find_subsets(nums, answer, 0,0)
        answer.append(nums)
        return answer

mySolution = Solution()
lst = [1,2,3]
print(mySolution.subsets(lst))