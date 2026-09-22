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
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.empty()) {
            return 0;
        }

        ranges::sort(intervals, [](auto& x, auto& y) {
            return x.start < y.start;
        });
        priority_queue<int, vector<int>, greater<int>> pq;

        for (auto [start, end] : intervals) {
            if (!pq.empty() && pq.top() <= start) {
                pq.pop();
            }
                pq.push(end);
        }

        return pq.size();
    }
};
