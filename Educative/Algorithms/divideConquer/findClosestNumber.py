# Let's start off with writing a simple binary search algorithm
# That runs in Log(N), then we can build on top of that to
# solve the problem

def binary_search(lst, low, high, target, min, min_idx):
# Base case
    if low >= high: # binary search algorithm doesn't go out of bounds        
        curr_min = abs(lst[low] - target)
        if curr_min < min:
            return low
        return lst[min_idx]
    # Calculate mid
    mid = low + (high - low)//2
    curr_min = abs(lst[mid] - target)
    if curr_min < min:
        min = curr_min
        min_idx = mid
    if curr_min > min:
        return lst[min_idx]
    if lst[mid] == target:
        return lst[mid]
    elif target > lst[mid]:
       return binary_search(lst, mid + 1, high, target, min, min_idx)
    return binary_search(lst, low, mid - 1, target, min, min_idx)


def find_closest_number(lst, target):
    idx = binary_search(lst, 0, len(lst) - 1, target, float('inf'), -1)
    print(idx)
    pass

lst = [-9,-4,-2,0,1,3,4,10]
target = 5
find_closest_number(lst,target)
"""
What I can do is set a huge number called min_diff
min_diff will hold memory of the smallest difference that was found
it will initialize as a huge number, and as the binary search algorithm
traverses the sorted list, min_diff will be updated
The algorithm will return the correct number when the 
"""