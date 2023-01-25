def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash:
            return [hash[diff], i]
        if nums[i] not in hash:
            hash[nums[i]] = i
    return [-1,-1]
