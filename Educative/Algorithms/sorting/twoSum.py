def find_sum(lst,n):
    lst.sort()
    
    left = 0
    right = len(lst) - 1
    result_array = []
    while(left <= right):
        current_sum = lst[left] + lst[right]
        if current_sum == n:
            result_array.append(lst[left])
            result_array.append(lst[right])
            break
        elif(current_sum > n):
            right -= 1
        elif(current_sum < n):
            left += 1
    return result_array


print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))