# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        N = len(intervals)
        for i in range(N):

            if intervals[i].end < newInterval.start:
                res.append(intervals[i])

            elif newInterval.end < intervals[i].start:
                res.append(newInterval)
                k = i
                while k < N:
                    res.append(intervals[k])
                    k += 1
                return res

            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)

        res.append(newInterval)
        return res
