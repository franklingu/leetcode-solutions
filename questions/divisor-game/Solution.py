"""

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.

Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.
 
Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

 
Constraints:

1 <= n <= 1000


"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        def can_win(n, cache):
            if cache[n] is not None:
                return cache[n]
            for i in range(1, n):
                if n % i == 0:
                    ret = can_win(n - i, cache)
                    if not ret:
                        cache[n] = True
                        return True
            cache[n] = False
            return False
        
        cache = [None for _ in range(n + 1)]
        cache[0] = True
        cache[1] = False
        return can_win(n, cache)