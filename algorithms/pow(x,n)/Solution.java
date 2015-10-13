/**
 * Implement pow(x, n).
 */
public class Solution {
    public double myPow(double x, int n) {
        if (n == 0 || Double.compare(x, 1) == 0 || (Double.compare(x, -1) == 0 && n %2 == 0)) {
            return 1.00;
        } else if (Double.compare(x, 0) == 0) {
            return 0.00;
        } else if (n == 1) {
            return x;
        } else if (n < 0) {
            return myPow(1/x, -1*n);
        }
        
        
        if (n%2 == 0) {
            return myPow(x*x, n/2);
        } else {
            return x* myPow(x, n-1);
        }
    }
}