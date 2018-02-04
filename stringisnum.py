class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            float(s)
            return True
        except:
            return False


	def isNumeric(self, s):
        # write code here
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)