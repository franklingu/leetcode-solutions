"""

A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.

Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.
 
Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

 
Constraints:

num1 and num2 are valid complex numbers.


"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_num(num):
            real, imaginary = num.split('+')
            return int(real), int(imaginary[:len(imaginary) - 1])
        
        real1, imaginary1 = parse_num(num1)
        real2, imaginary2 = parse_num(num2)
        real = real1 * real2 - imaginary1 * imaginary2
        imaginary = real1 * imaginary2 + real2 * imaginary1
        return str(real) + '+' + str(imaginary) + 'i'