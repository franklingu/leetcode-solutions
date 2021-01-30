/**
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 */

class MinStack {
    private Stack<Integer> st = new Stack<Integer>();
    private Stack<Integer> minSt = new Stack<Integer>();
    
    public void push(int x) {
        st.push(x);
        if (minSt.isEmpty()) {
            minSt.push(x);
        } else {
            int val = minSt.peek().intValue();
            minSt.push(val < x ? val : x);
        }
    }

    public void pop() {
        minSt.pop();
        st.pop();
    }

    public int top() {
        return st.peek().intValue();
    }

    public int getMin() {
        return minSt.peek().intValue();
    }
}
