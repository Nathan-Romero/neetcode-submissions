class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> mp;

public:
    void set(string key, string value, int timestamp) {
        mp[key].emplace_back(timestamp, value);
    }

    string get(string key, int timestamp) {
        auto& vals = mp[key];
        int l = 0, r = vals.size() - 1;
        string res = "";

        while (l <= r) {
            int mid = l + (r - l >> 1);

            if (vals[mid].first <= timestamp) {
                res = vals[mid].second;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return res;
    }
};
