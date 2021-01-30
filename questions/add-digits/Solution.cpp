/**
 * Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
 * For example:
 * Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
 * Since 2 has only one digit, return it.
 *
 */

class Solution {
public:
    int addDigits(int num) {
        if (num/10 == 0) {
            return num;
        }
        
        int answer = 0;
        
        while (num > 0) {
            answer += num %10;
            num = num / 10;
        }
        
        return addDigits(answer);
    }
};

/**
 * Follow up:
 * Could you do it without any loop/recursion in O(1) runtime?
 */

 public class Solution {
    public int addDigits(int num) {
        if (num == 0) {
            return 0;
        }
        int answer = num%9;
        if (answer == 0) {
            return 9;
        } else {
            return answer;
        }
    }
};