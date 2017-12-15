class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #主要是把初始坐标设为00，然后记下每一步，如果最终还是00，那就是一个circle
        x = 0
        y = 0
        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        if x == y == 0:
            return True
        else:
            return False