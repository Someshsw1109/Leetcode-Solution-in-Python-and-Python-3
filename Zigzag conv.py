class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if s is None and numRows <= 0:
            return ""
        
        if numRows == 1:
            return s
        
        result = ""
        
        step = 2 * numRows - 2
        
        for i in range(0, numRows):
            
            for j in range(i, len(s), step):
                result += s[j]
                
                if i != 0 and i != numRows - 1 and (j + step - 2 * i) < len(s):
                    result += s[j + step - 2 * i]
                    
        return result

# Follow me on instagram my insta id is - @codewithsomesh
