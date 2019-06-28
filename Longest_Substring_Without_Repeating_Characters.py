class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        result = 0
        substr = []
        
        for i in range(0, len(s)):
            if (len(substr) > 0):
                if (s[i] in substr):
                    substr = substr[substr.index(str(s[i])) + 1:]
                    count = len(substr)
            substr.append(str(s[i]))
            count += 1
            
            if (count >= result):
                result = count
        
        return result
            
