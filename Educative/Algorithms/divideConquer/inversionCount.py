def count_inversions(lst,low,mid,high):
    inversions = 0
    i = low
    while i <= mid:
        j = mid + 1
        while j <= high:
            #print(lst[i], lst[j])
            if lst[i] > lst[j]:                
                inversions += 1
            j += 1
        i += 1
    return inversions

def inversion_util(lst,low,high):
    inv_count = 0 
    if low < high:            
        mid = low + (high - low)//2                                        
        inv_count += inversion_util(lst, low, mid)
        inv_count += inversion_util(lst, mid + 1, high)
        inv_count += count_inversions(lst,low,mid,high)
    return inv_count

def inversionCount(lst):        
    return inversion_util(lst, 0, len(lst)-1)
    
    
    
list1 = [3,2,8,4]
list2 = [7, 6, 5, 8]
list3 = [10, 9, 8, 7, 6]
list4 = [1, 2, 3, 4, 5]
list5 = [3,8,2,7,5,6]
diegolist = [5.4,17.20,10.2,-5.04, 3]
print(list1,inversionCount(list1))
print(list2,inversionCount(list2))
print(list3,inversionCount(list3))
print(list4,inversionCount(list4))
print(diegolist, inversionCount(diegolist))
print(list5, inversionCount(list5))