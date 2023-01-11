def binary_search(lst, left, right, key):
    if right >= left:
        mid_element = left + (right - left) //2
        # if the required element is found at the middle index
        if lst[mid_element] == key:
            return mid_element
        # if the required element is smaller than the element at the middle index
        # it can only be present in the left sub-list
        if lst[mid_element] > key:
            return binary_search(lst,left, mid_element -1, key)
        # Otherwise, it would be present in the right sub-list
        return binary_search(lst, mid_element + 1, right, key)
    # if the element is not in the list
    return -1