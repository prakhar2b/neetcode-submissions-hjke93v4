class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_profit_day = -1
        # sell today
        # max profit if bought at lowest on previous day

        min_so_far = prices[0]
        for i in range(1, len(prices)):
            max_profit_today = prices[i] - min_so_far
            min_so_far = min(min_so_far, prices[i])
            if max_profit_today > max_profit:
                max_profit = max_profit_today
                max_profit_day = i

            print( prices[i],max_profit, max_profit_today)

        return max_profit
