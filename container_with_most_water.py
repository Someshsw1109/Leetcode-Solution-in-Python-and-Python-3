class Solution:
    def maxArea(self, H: List[int]) -> int:
        
        ans = 0
        l = 0
        r = len(H) - 1
        
        while l < r:
            minH = min(H[l], H[r]) # Here minH stands for minimum height
            ans = max(ans, minH * (r - l))
            if H[l] < H[r]:
                l += 1
            else:
                r -= 1
        return ans

# Follow me on instagram my insta id is - @codewithsomesh
