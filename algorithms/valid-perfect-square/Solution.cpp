/**
 * Given a positive integer num, write a function which returns True if num is a perfect square else False.
 *
 * Note: Do not use any built-in library function such as sqrt.
 *
 * Example 1:
 *
 * Input: 16
 * Returns: True
 *
 * Example 2:
 *
 * Input: 14
 * Returns: False
 *
 */


class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num <= 0) {
             return false;
        }
        int guess = num, power = 1, next_guess, next_power, tmp, ret;
        while (guess > power) {
            next_guess = guess >> 1;
            next_power = power << 1;
            if (next_guess < next_power) {
                break;
            }
            guess = next_guess;
            power = next_power;
        }
        for (int i = power; i <= guess; i++) {
            if (i * i == num) {
                return true;
            } else if (i * i > num) {
                return false;
            }
        }
        return false;
    }
};
