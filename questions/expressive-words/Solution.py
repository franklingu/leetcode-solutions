"""

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
Given a list of query words, return the number of words that are stretchy. 
 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

 
Constraints:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters


"""


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        simplified = []
        for c in S:
            if not simplified or c != simplified[-1][0]:
                simplified.append([c, 1, 1])
            elif simplified[-1][2] == 1:
                simplified[-1][1] = 2
                simplified[-1][2] = 2
            else:
                simplified[-1][1] = 1
                simplified[-1][2] = simplified[-1][2] + 1
        cnt = 0
        for word in words:
            prev, ccnt, index = None, 0, 0
            for c in word:
                if c != prev and prev is not None:
                    if not (simplified[index][1] <= ccnt <= simplified[index][2]):
                        break
                    index += 1
                    ccnt = 0
                if c != simplified[index][0]:
                    break
                prev = c
                ccnt += 1
            if index == len(simplified) - 1 and simplified[index][1] <= ccnt <= simplified[index][2]:
                cnt += 1
        return cnt
                    