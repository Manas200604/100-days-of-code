class Solution:
    def stockBuySell(self, arr, n):
        min_price = arr[0]
        max_profit = 0

        for i in range(1, n):
            profit = arr[i] - min_price
            max_profit = max(max_profit, profit)

            min_price = min(min_price, arr[i])

        return max_profit