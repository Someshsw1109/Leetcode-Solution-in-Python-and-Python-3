class Solution(object):
    def intToRoman(self, num):
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        result = ""
        while num > 0:
            while num >= val[i]:
                num -= val[i]
                result += symbol[i]
            i += 1
        return result
# Follow me on instagram for more my insta id is - @codewithsomesh
