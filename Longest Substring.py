class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0

        for right in range(n):
            if s[right] not in charMap or charMap[s[right]]<left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right

        return maxLength


# Follow me on instagram my insta id is - @codewithsomesh
