#322 Coin Change
'''
You are given an integer array coins represultenting coins of different denominations and an integer amount represultenting a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        amount +=1
        lista = [amount] * amount

        lista[0] = 0 

        for coin in sorted(coins):
            for i in range(coin,amount):
                eklenecek = lista[i-coin] + 1
                if eklenecek < lista[i]:
                    lista[i] = eklenecek
        return -1 if lista[-1] == amount else lista[-1]
        
        