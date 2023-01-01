def dutch_national_flag(lst):
    # Sort 0s, 1s, and 2s
    # in place and in linear time
    size = len(lst)
    i = 0
    j = size -1
    mid = 0
    while(mid <= j):
        if lst[mid] == 0:
            lst[mid], lst[i] = lst[i], lst[mid]
            i+=1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1
    return lst


print(dutch_national_flag([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]))
