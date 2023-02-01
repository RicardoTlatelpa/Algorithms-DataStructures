class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count every number in hash table
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1            
        
        longest = 0        
        for key in d:
            sequence = 1
            next_key = key + 1
            last_key = key - 1            
            if last_key not in d:
                while next_key in d:                
                    sequence += 1
                    next_key += 1                
            if sequence > longest:
                longest = sequence

        return longest
    
    def neetCodeSolution(self,nums):
        numSet = set(len(nums))
        longest = 0
        for n in range(nums):
            if(n-1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
