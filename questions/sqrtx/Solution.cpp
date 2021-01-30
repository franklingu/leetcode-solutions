/**
 * Implement int sqrt(int x).
 * Compute and return the square root of x.
 */
class Solution {
public:
    int mySqrt(int x) {
        int power = 1;
        int guess = 1;
        
        // check for overflow with power > 0
        while (x > power && power > 0) {
            power *= 4;
            guess *= 2;
        }

        guess /= 2;
        int odd = 2*guess + 1;
        int square = guess*guess;
        
        while (square <= x && square >= 0) {
            if (square == x) {
                return odd/2;
            }
            
            square += odd;
            odd += 2;
        }
        
        return (odd - 2)/2;
    }
};