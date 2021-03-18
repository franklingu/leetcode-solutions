"""

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.
Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.


Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]


Example 2:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.


"""


import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        dx, dy = 0, 0
        while True:
            dx = self.radius * random.random()
            dy = self.radius * random.random()
            if dx * dx + dy * dy > self.radius * self.radius:
                continue
            if random.randint(0, 1) != 1:
                dx = -dx
            if random.randint(0, 1) != 1:
                dy = -dy
            break
        x = dx + self.x_center
        y = dy + self.y_center
        return x, y


class Solution2:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        l = math.sqrt(random.random()) * self.radius
        angle = random.random() * math.pi * 2
        return self.x_center + l * math.cos(angle), self.y_center + l * math.sin(angle)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()