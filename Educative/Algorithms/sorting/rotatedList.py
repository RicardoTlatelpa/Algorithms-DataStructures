def find_pivot(lst, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = (low + high) // 2

    if mid < high and lst[mid] > lst[mid + 1]: # mid index iss less than the high index 
        # and the value of the mid is greater than the index to the right
        return mid

    if mid > low and lst[mid] < lst[mid - 1]:
        return mid - 1
    
    if lst[low] >= lst[mid]:
        return find_pivot(lst, low, mid-1)

    return find_pivot(lst, mid + 1, high)
    


def binary_search(lst, low, high, key):
    if(high < low): # base case
        return -1
    mid = (high + low) // 2
    if(lst[mid] == key):
        return mid
    if(key > lst[mid]):
        return binary_search(lst, mid + 1, high, key)
    else:
        return binary_search(lst, low, mid - 1, key)

def pivoted_binary_search(lst, n, key):
    # Write your code here!
    # 1. Find existing pivot
    # 2. binary search on pivot
    # Pivot - a number that has numbers greater to the right and left 
    # or numbers smaller to the right and left
    # don't include pivot as indice in binary search invocation
    pivot = find_pivot(lst, 0, n - 1)
    if pivot == -1:
        return binary_search(lst, 0, n - 1, key)
    
    if lst[pivot] == key:
        return pivot
    if lst[0] <= key: # key is greater
        return binary_search(lst, 0, pivot - 1, key)
    
    return binary_search(lst, pivot + 1, n - 1, key)
    

pivoted_binary_search([7, 8, 9, 0, 3, 5, 6], 7, 3)


lst = [6, 7, 8, 9, 10, 0, 1, 2, 3]
key = 0
print(pivoted_binary_search(lst, len(lst), key))
