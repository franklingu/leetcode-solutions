/**
 * Write a function that takes a string as input and returns the string reversed.
 *
 * Example:
 * Given s = "hello", return "olleh".
 */

import java.util.*;
class Solution {
    public String reverseString(String s) {
        StringBuilder input1 = new StringBuilder();
        input1.append(s);
        return input1.reverse().toString();
    }
}

