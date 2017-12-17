class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return int(min(len(candies) / 2, len(set(candies))))


        """
        题目要求平均分糖，而且糖的种类不一样，问一个人最多分到几种糖，
        这个解法很秒，首先如果所有种类都不相同，那么能分到len(candies)/2种，
        并且这也是理论上的最大值，但是如果有重复的，那就先set一下，如果set之后的数量
        小于len(candies)/2,那就取set之后的数量，如果set之后的数量大于，那也只能取len(candies)/2
        """