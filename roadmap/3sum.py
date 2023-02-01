class Solution:
    def threeSum(self,nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            # prevent duplicates and check if i index is in bounds
            if i > 0 and a == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    # prevent similar sum
                    i += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                    """
                    After a solution has been, further indices are explored until the conditional
                    l < r is broken.

                    the l pointer, is the middle pointer and follows the same algorithm as the first iterator,
                    where if the same number is seen, it is skipped.
                    
                    The effect is, duplicates are prevented, and the sorting of the initial nums list allows
                    the duplicates to cluster up and the desired effect to take place.

                    The right pointer works as usual in this algorithm and decrements if the total sum is greater
                    than 0.
                    """
        return res

my = Solution()
lst = [2,2,2,0,0,0,-1,-1]
print(my.threeSum(lst))
