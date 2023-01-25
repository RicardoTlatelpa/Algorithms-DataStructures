"""
Pythonic way to create a copy: 
copy[::]
"""


def subsets_with_duplicates(nums):
    answers = []
    subset = []
    def backtrack(i, subset):
        if i == len(nums):
            answers.append(subset[::])
            return
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        # prevents generation of duplicate subset
        while(i + 1 < len(nums) and nums[i] == nums[i + 1]):
            i += 1
        backtrack(i + 1, subset)
    backtrack(0, subset)
    return answers

print(subsets_with_duplicates([1,2,3]))
        

