class Solution:
    def reverse(self, x: int) -> int:
        
        Total = 0
        Symbol = 1
        k = x
        
        if k < 0:
            x = abs(x)
            Symbol = -1
            
        while(x > 0):
            b = x % 10
            Total = Total * 10 + b
            
            x = x//10
            
        if Total > pow(2, 31):
            return 0
        
        else:
            return Total * Symbol

# Follow me on instagram my insta id is - @codewithsomesh.
