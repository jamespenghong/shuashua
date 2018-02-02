class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1] - prices[i],0) for i in range(len(prices) - 1))
        """
        股票交易策略，如果明天价格大于今天就交易。