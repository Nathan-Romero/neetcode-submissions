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
        map<int, int> line;
        for (auto [start, end] : intervals) {
            ++line[start], --line[end];
        }

        int cur = 0, res = 0;
        for (auto [_, rooms] : line) {
            res = max(res, (cur += rooms));
        }

        return res;
    }
};
