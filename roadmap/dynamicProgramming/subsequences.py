def printSubsequences(a):
    def subs(subsequence,i):
        if i >= len(a):
            print(subsequence)
            return
        # pick
        subs(subsequence + str(a[i]), i+1)
        # not pick
        subs(subsequence, i+1)
    subs("", 0)

printSubsequences([1,2,3])

