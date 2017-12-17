class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set('qwertyuiop')     #先生成三个键盘集合，然后把每一个词也转换成集合
        set2 = set('asdfghjkl')      #然后判断词集合和键盘集合的交集是不是词集合本身
        set3 = set('zxcvbnm')        #如果是则说明在一行。
        wordlist = []
        for word in words:
            if set(word.lower())&set1 == set(word.lower()):
                wordlist.append(word)
            elif set(word.lower())&set2 == set(word.lower()):
                wordlist.append(word)
            elif set(word.lower())&set3 == set(word.lower()):
                wordlist.append(word)
            else:
                continue
        
        return wordlist