def knap_sack_recursive(profits, profits_length, weights, capacity, current_index):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each item
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :param current_index: Current index of the weights
    :return: Maximum value that can be put in a knapsack
    """

    # Base Case
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # If weight of the nth item is more than Knapsack, then
    # this item cannot be included in the optimal solution
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights,
                                                     capacity - weights[current_index], current_index + 1)

    profit2 = knap_sack_recursive(profits, profits_length, weights, capacity, current_index + 1)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    return max(profit1, profit2)


def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """
    return knap_sack_recursive(profits, profits_length, weights, capacity, 0)

# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, 4, weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, 4, weights, 6))
