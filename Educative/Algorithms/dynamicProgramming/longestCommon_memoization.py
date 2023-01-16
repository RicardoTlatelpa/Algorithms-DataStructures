def longest_common_substr_length_recursive(lookup_table, s1, s2, i1, i2, count):
    """
    Finds a longest common substring length
    :param lookup_table: Lookup Table
    :param s1: First string
    :param s2: Second string
    :param i1: Starting index of substring
    :param i2: Ending index of substring
    :param count: Common sequence count
    :return: Length of longest common substring
    """

    if i1 == len(s1) or i2 == len(s2):
        return count

    if lookup_table[i1][i2][count] == -10:
        c1 = count

        if s1[i1] == s2[i2]:
            c1 = longest_common_substr_length_recursive(lookup_table, s1, s2, i1 + 1, i2 + 1, count + 1)

        c2 = longest_common_substr_length_recursive(lookup_table, s1, s2, i1, i2 + 1, 0)
        c3 = longest_common_substr_length_recursive(lookup_table, s1, s2, i1 + 1, i2, 0)
        lookup_table[i1][i2][count] = max(c1, max(c2, c3))

    return lookup_table[i1][i2][count]


def longest_common_substr_length(s1, s2):
    """
    Finds a longest common substring length
    :param lookup_table: Lookup Table
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """
     
    # Declaring a lookup table with dimensions: lookup_table[len(s1)][len(s2)][max_length]
    # Declaring a vector of a vector of a vectors!
    max_length = max(len(s1), len(s2))
    lookup_table = [[[-10 for k in range(len(s1))] for j in range(len(s2))] for i in range(max_length)]
    print(lookup_table)
    #return longest_common_substr_length_recursive(lookup_table, s1, s2, 0, 0, 0)


# Driver code to test the above function
S1 = "0abc321"
S2 = "123abcdef"
print(longest_common_substr_length(S1, S2))

S1 = "www.educative.io/explore"
S2 = "educative.io/edpresso"
#print(longest_common_substr_length(S1, S2))