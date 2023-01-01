def dutch_national_flag(lst):
    # Sort 0s, 1s, and 2s
    # in place and in linear time
    mid = len(lst) // 2
    i = 0
    j = len(lst) - 1
    print(lst)
    while(i < mid and j > mid):
        # i and j swap values if i holds a 2 or j holds a 0
        # both i and j shift any ones to the middle
        # lets first assume everything is sorted
        if(lst[i] == 0):
            i += 1
        if(lst[j] == 2):
            j -= 1
        if(lst[i] == 2 or lst[j] == 0):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
        if(lst[i] == 1):
            # shift towards the middle
            while(lst[i + 1] != 1 and i < mid):
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp
                i+=1
        if(lst[j] != 1):
            # shift towards the middle
            while(lst[j - 1] != 1 and j > mid):
                tmp = lst[j]
                lst[j] = lst[j - 1]
                lst[j - 1] = tmp
                j-=1
        i += 1
        j -= 1
    return lst


print(dutch_national_flag([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]))