class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        total = 0
        k = x
        while(x > 0):
            b = x % 10
            total = total * 10 + b
            x = x // 10
            
        if total == k:
            return True
        else:
            return False

# Follow me on instagram my insta id is - @codewithsomesh
