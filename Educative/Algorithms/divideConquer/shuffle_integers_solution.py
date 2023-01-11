import math

def shuffle_list_recursive(lst, left, right):
    if right - left > 1:
        mid = (left + right) //2 # Compute mid of the list
        temp = mid + 1
        middle = (left + mid) //2 
        # swapping elements of the sub list
        # print(left, right)
        # print(middle + 1, mid + 1)
        for i in range(middle + 1, mid + 1):            
            lst[i], lst[temp] = lst[temp],lst[i]
            temp += 1
        shuffle_list_recursive(lst, left, mid)
        shuffle_list_recursive(lst, mid + 1, right)

def shuffle_list(lst):
    # Check if size of array is 2^n
    log = math.log2(len(lst) % 2)
    if len(lst) != 2 and (log == 0 or log == 1 or log == 0):
        shuffle_list_recursive(lst, 0, len(lst)-1)
lst = [1,2,3,4,5,6,7,8]
shuffle_list_recursive(lst, 0, len(lst)-1)