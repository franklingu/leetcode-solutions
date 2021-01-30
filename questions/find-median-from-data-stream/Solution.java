/**
 * Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle
 * value. So the median is the mean of the two middle value.
 * 
 * Examples: 
 * [2,3,4] , the median is 3
 * 
 * [2,3], the median is (2 + 3) / 2 = 2.5
 * 
 * Design a data structure that supports the following two operations:
 * 
 * void addNum(int num) - Add a integer number from the data stream to the data structure.
 * double findMedian() - Return the median of all elements so far.
 * For example:
 * 
 * add(1)
 * add(2)
 * findMedian() -> 1.5
 * add(3) 
 * findMedian() -> 2
 */

class MedianFinder {
    private PriorityQueue<Integer> smallers;
    private PriorityQueue<Integer> biggers;

    public MedianFinder() {
        this.biggers = new PriorityQueue<Integer>();
        this.smallers = new PriorityQueue<Integer>(Collections.reverseOrder());
    }    

    // Adds a number into the data structure.
    public void addNum(int num) {
        if (this.smallers.size() < this.biggers.size()) {
            if (this.smallers.peek() < num) {
                if (this.biggers.peek() > num) {
                    this.smallers.add(num);
                } else {
                    this.smallers.add(this.biggers.poll());
                    this.biggers.add(num);
                }
            } else {
                this.smallers.add(num);
            }
        } else if (this.smallers.size() > this.biggers.size()) {
            if (this.biggers.isEmpty()) {
                if (this.smallers.peek() > num) {
                    this.biggers.add(this.smallers.poll());
                    this.smallers.add(num);
                } else {
                    this.biggers.add(num);
                }
                return ;
            }
            if (this.biggers.peek() > num) {
                if (this.smallers.peek() < num) {
                    this.biggers.add(num);
                } else {
                    this.biggers.add(this.smallers.poll());
                    this.smallers.add(num);
                }
            } else {
                this.biggers.add(num);
            }
        } else {
            if (this.smallers.size() == 0) {
                this.smallers.add(num);
                return ;
            }
            if (this.smallers.peek() >= num) {
                this.smallers.add(num);
            } else {
                this.biggers.add(num);
            }
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if ((this.smallers.size() + this.biggers.size()) % 2 == 1) {
            return (this.smallers.size() > this.biggers.size()) ? (double)this.smallers.peek() : (double)this.biggers.peek();
        } else {
            return (this.smallers.peek() + this.biggers.peek()) / 2.0;
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();
