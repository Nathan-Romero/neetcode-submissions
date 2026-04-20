class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;

        for (const string& c : tokens) {
            if (c == "+") {
                int a = s.top(); s.pop();
                int b = s.top(); s.pop();
                s.push(a + b);
            } else if (c == "-") {
                int a = s.top(); s.pop();
                int b = s.top(); s.pop();
                s.push(b - a);
            } else if (c == "*") {
                int a = s.top(); s.pop();
                int b = s.top(); s.pop();
                s.push(a * b);
            } else if (c == "/") {
                int a = s.top(); s.pop();
                int b = s.top(); s.pop();
                s.push(b / a);
            } else {
                s.push(stoi(c));
            }
        }

        return s.top();
    }
};