"""

None
"""


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.shape = [(0, 0)]
        self.positions = set([(0, 0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        curr = self.shape[-1]
        mapping = {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        delta = mapping[direction]
        next_pos = (curr[0] + delta[0], curr[1] + delta[1])
        if next_pos[0] < 0 or next_pos[0] >= self.height or next_pos[1] < 0 or next_pos[1] >= self.width:
            return -1
        food_taken = False
        if self.food_index < len(self.food):
            if next_pos == tuple(self.food[self.food_index]):
                food_taken = True
                self.food_index += 1
        if not food_taken:
            tail = self.shape[0]
            self.shape.pop(0)
            self.positions.remove(tail)
        if next_pos in self.positions:
            return -1
        self.shape.append(next_pos)
        self.positions.add(next_pos)
        return len(self.shape) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)