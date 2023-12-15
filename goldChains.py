def can_delete_and_split(lst):
    values = set()
    total_sum = sum(lst)

    # Traversal from the left
    left_sum = lst[0]
    right_sum = total_sum - left_sum
    values.add(left_sum)

    for i in range(1, len(lst) - 1):
        values.add(lst[i])
        left_sum += lst[i]
        right_sum -= lst[i]

        if (left_sum - right_sum) in values:
            return True

    # Traversal from the right
    right_sum = lst[len(lst)-1]
    left_sum = total_sum - right_sum
    values.clear()
    values.add(right_sum)

    for i in range(len(lst) - 2, 0, -1):
        values.add(lst[i])
        right_sum += lst[i]
        left_sum -= lst[i]

      if (right_sum - left_sum) in values:
          return True

    return False
