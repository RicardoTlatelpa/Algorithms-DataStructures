class Solution:
    def minWindow(self, s:str, t:str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have,need = 0, len(countT)
        res,resLen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r] # c for char
            # updating the dynamic hash
            window[c] = 1 + window.get(c,0)
           
            if c in countT and window[c] == countT[c]:
                have += 1
            # contracting window -> updating have variable
            while have == need:
                # checking if current window is min window
                if (r-l + 1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                # pop from left of our window
                windows[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""
