"""

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)
You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.
Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

 
Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15); // return 3
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3


 
Constraints:

0 <= startTime < endTime <= 109
At most 400 calls will be made to book.


"""


import bisect

class MyCalendarThree:

    def __init__(self):
        
        # [1] two lists for start and end points 
        #     that will be maintained sorted
        self.ss = []
        self.ee = []
        
        self.k_max = 0

    def book(self, s: int, e: int) -> int:
       
        # [2] insert start and end points into corresponding 
        #     lists while maintaining sort order
        bisect.insort_left(self.ss, s)
        bisect.insort_left(self.ee, e)
        
        # [3] calculate the number 'k_cur' of intervals 
        #     that remain open at point 's'
        opened = bisect.bisect_right(self.ss, s)
        closed = bisect.bisect_right(self.ee, s)
        k_cur = opened - closed
        self.k_max = max(self.k_max, k_cur)

        # [4] two-pointer iteration over start and end points 
        #     to update the number of intervals 'k_cur' that  
        #     remain open at each iteration
        while True:
            
            # [5] no need to continue if:
            #     - either all starting points were accounted for
            #     - or next starting point lies to the righe of 'e'
            if opened >= len(self.ss): break
            if self.ss[opened] >= e  : break
            
            if self.ss[opened] < self.ee[closed]:
                opened += 1
            else:
                closed += 1
            
            k_cur = opened - closed        
            self.k_max = max(self.k_max, k_cur)

        return self.k_max