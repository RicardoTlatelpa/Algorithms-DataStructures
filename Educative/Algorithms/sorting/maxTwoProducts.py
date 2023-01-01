from decimal import Decimal # for infinite numbers
def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """
    curr_min = float('inf')
    last_min = float('inf')
    curr_max = float('-inf')
    last_max = float('-inf')

    for i in range(len(lst)):
        current_num = lst[i]
        if current_num <= curr_min:
            last_min = curr_min
            curr_min = current_num
        if current_num >= curr_max:
            last_max = curr_max
            curr_max = current_num
    if(curr_min * last_min) > curr_max * last_max and (curr_min * last_min) != float('inf'):
        return [last_min,curr_min]
    return [last_max,curr_max]