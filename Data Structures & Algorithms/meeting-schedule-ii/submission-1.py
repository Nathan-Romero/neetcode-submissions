"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = res = 0
        s = e = 0

        while s < n:
            if start[s] < end[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res