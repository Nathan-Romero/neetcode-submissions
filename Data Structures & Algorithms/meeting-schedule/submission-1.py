"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        return all(a.end <= b.start for a, b in pairwise(sorted(intervals, key=lambda i: i.start)))