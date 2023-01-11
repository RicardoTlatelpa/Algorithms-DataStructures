"""
We have n jobs , where every job is scheduled to be done from startTime[i] to endTime[i]
obtaining a profit [i].
return the maximum profit
"""

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        maximum_profit = 0
        i = 0
        j = 1



