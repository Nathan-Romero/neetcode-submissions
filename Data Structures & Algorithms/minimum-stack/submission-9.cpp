class MinStack {
    stack<long> s;
    long min;

public:
    MinStack() {}

    void push(int val) {
        if (s.empty()) {
            s.push(0);
            min = val;
        } else {
            s.push(val - min);
            if (val < min) min = val;
        }
    }

    void pop() {
        long val = s.top();
        s.pop();

        if (val < 0) min = min - val;
    }

    int top() {
        long val = s.top();
        return val > 0 ? min + val : int(min);
    }

    int getMin() { return int(min); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */