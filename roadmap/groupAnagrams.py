class Solution:
    def groupAnagrams(self,strs):
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in a:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()

    #O(m * n) time complexity
