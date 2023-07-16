class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        Answer=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    if j-i+1 > len(Answer):
                        Answer = s[i:j+1]

        return Answer


# Follow me on instagram my insta id is - @codewithsomesh
