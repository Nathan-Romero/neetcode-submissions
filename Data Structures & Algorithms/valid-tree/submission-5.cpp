class Solution {
    vector<vector<int>> adj;
    unordered_set<int> visit;

    bool dfs(int node, int prev) {
        if (visit.contains(node)) {
            return false;
        }
        visit.insert(node);

        for (const auto nei : adj[node]) {
            if (nei != prev && !dfs(nei, node)) {
                return false;
            }
        }
        return true;
    }

public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() > n - 1) {
            return false;
        }
        adj.resize(n);

        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        return dfs(0, -1) && visit.size() == n;
    }
};
