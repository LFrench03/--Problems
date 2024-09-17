#66 Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        string = ''
        for x in digits:
            string+= str(x) 
        string = int(string) + 1
        return [int(x) for x in str(string)]
digits = [4,3,2,1]
x = Solution()
x.plusOne(digits)