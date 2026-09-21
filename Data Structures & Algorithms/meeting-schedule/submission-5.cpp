/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        if (intervals.empty()) {
            return true;
        }
        ranges::sort(intervals, [](auto& x, auto& y) {
            return x.start < y.start;
        });
        auto prev = intervals[0].end;
        for (auto&& [start, end] : span(intervals).subspan(1)) {
            if (prev > start) {
                return false;
            }
            prev = end;
        }
        return true;
    }
};
