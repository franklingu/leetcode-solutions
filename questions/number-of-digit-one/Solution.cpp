/**
 * Given an integer n, count the total number of digit 1 appearing in 
 * all non-negative integers less than or equal to n.
 *
 * For example:
 * Given n = 13,
 * Return 6, because digit 1 occurred in the following numbers: 
 * 1, 10, 11, 12, 13.
 */

 
class Solution {
private:
    const int DIGIT = 1;
public:
    int countDigitOne(int n) {
        if (n < 1) return 0;
        
        int powerOfTen = 1;
        int answer = 0;
        int nextN = n;
        do {
            // every iteration, we count the number of 
            // times a number has '1' in the powerOfTen's 
            // place. Ex: in the first iteration we count 
            // number of times '1' appears on the unit's place
            
            answer += (nextN/10) * powerOfTen;
            
            if (nextN % 10 > DIGIT) {
                answer += powerOfTen;
            } else if (nextN % 10 == 1) {
                answer += ((n%powerOfTen) + 1);
            }
            
            powerOfTen *= 10;
            nextN /= 10;
        } while (nextN > 0);
        
        return answer;
    }
};