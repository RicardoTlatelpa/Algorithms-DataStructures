'''
12.5 Find the nearest repeated entries in an array

Write a program which takes as input an array and finds the distance
between a closest pair of equal entries. For example, if 
s = [All, work, and, no, play, makes, for, no, work, no, fun, and, no, results]
'''

def findNearest(paragraph):
    distance_dict = {}
    stack_dict = {}
    ans = float('inf')
    for i in range(len(paragraph)):
        word = paragraph[i]
        if word not in distance_dict:
            distance_dict[word] = float('inf')
        if word not in stack_dict:
            stack_dict[word] = [i]
        elif word in stack_dict:  
            smallest_distance = min(distance_dict[word], abs(stack_dict[word][-1]-i))          
            distance_dict[word] = smallest_distance
            ans = min(ans, smallest_distance)
            stack_dict[word].append(i)
    return ans if ans != float('inf') else -1
print(findNearest(["All","work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]))

def find_nearest_repitition(paragraph):
    word_to_latest_index, nearest_repeated_distance  = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word)
        word_to_latest_index[word] = i
    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1

print(find_nearest_repitition(["All","work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]))

'''
The time complexity is O(n), since we perform a constant amount of work per entry.
The space complexity is O(d) where d is the number of distinct entries in the array
'''