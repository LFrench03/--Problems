#1497- Check if Array paires  Are disivible
'''
'''
class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        frequency = [0] * k
        
        for num in arr:
            num %= k
            if num < 0:
                num += k
            frequency[num] += 1
        
        if frequency[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if frequency[i] != frequency[k - i]:
                return False
        
        return True