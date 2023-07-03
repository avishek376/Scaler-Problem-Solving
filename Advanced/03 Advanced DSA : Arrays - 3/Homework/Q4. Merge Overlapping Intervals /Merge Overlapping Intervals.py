# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)

        intervalsnew = []

        L = intervals[0].start
        R = intervals[0].end
        for i in range(1, len(intervals)):

            if R >= intervals[i].start:
                # although its sorted if left side interval's R is greater then we have to update it to
                # max R
                R = max(R, intervals[i].end)
            else:
                intervalsnew.append(Interval(L, R))
                L = intervals[i].start
                R = intervals[i].end
        intervalsnew.append(Interval(L, R))
        return intervalsnew