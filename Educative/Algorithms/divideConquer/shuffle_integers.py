import math

def shuffle_list_util(lst, low, mid, high):
    
    left_mid = low + (mid - low)//2
    right_mid = mid + 1
    print(left_mid, mid)
    while left_mid <= mid:
        lst[left_mid], lst[right_mid] = lst[right_mid], lst[left_mid]
        right_mid+=1        
        left_mid+=1
    
    #shuffle_list_util(lst, low, left_mid, mid)

def shuffle_list(lst):
    """
    Shuffles the list
    :param lst: list of integers
    """
    l = math.log2(len(lst))
    if l.is_integer() == False:
        return lst
    mid = (len(lst) - 1)//2
    print(lst)
    shuffle_list_util(lst, 0, mid ,len(lst)-1)
    return lst


lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(shuffle_list(lst))