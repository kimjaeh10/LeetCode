class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = str(s)
        open_paren = ["(", "{", "["]
        close_paren = [")", "}", "]"]
        
        stack = []
        
        for i in range(0, len(s)):
            if s[i] in open_paren:
                stack.append(s[i])
            elif s[i] in close_paren:  
                if len(stack) == 0:
                    return False
                pop = stack[-1]
                
                index1 = open_paren.index(pop)
                index2 = close_paren.index(s[i])
                
                if index1 == index2:
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True
        
