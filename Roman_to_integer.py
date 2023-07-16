class Solution:
    def romanToInt(self, s: str) -> int:
        
        R = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        number = 0
        
        for i in range(len(s) - 1):
            if R[s[i + 1]] > R[s[i]]:
                number -= R[s[i]]
            else:
                number += R[s[i]]
                
        number += R[s[len(s) - 1]]
        
        return number

# Follow om instagram for more my insta id is - @codewithsomesh
