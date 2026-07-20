from heapq import heappush, heapreplace

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        min_heap = []

        for interval in intervals:
            if min_heap and interval.start >= min_heap[0]:
                heapreplace(min_heap, interval.end)
            else:
                heappush(min_heap, interval.end)

        return len(min_heap)