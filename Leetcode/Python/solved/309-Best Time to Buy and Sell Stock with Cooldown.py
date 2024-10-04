#309 Best Time to Buy and Sell Stock with Cooldown
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lenght = len(prices)

        if lenght == 1: return 0

        buy = [-10 ** 9] * lenght
        sell = [0] * lenght

        for i in range(lenght):
            sell[i] = max(sell[i - 1], prices[i] + buy[i - 1])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        return sell[-1]
        
prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
x = Solution()
x.maxProfit(prices)